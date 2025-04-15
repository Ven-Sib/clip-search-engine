from django.http import JsonResponse
from .forms import ImageUploadForm
import torch, clip, faiss, numpy as np
from PIL import Image
import os
from django.views.decorators.csrf import csrf_exempt

# Determine path two levels up to reach the project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SAMPLE_IMAGES_PATH = os.path.join(BASE_DIR, 'media', 'sample_images')

device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)

# Load dataset embeddings once
def load_embeddings(folder=SAMPLE_IMAGES_PATH):
    if not os.path.exists(folder):
        print(f"❌ Folder not found: {folder}")
        return None, []

    image_files = [f for f in os.listdir(folder) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp'))]
    if not image_files:
        print("⚠️ No images found in sample_images.")
        return None, []

    embeddings, paths = [], []

    for fname in image_files:
        try:
            path = os.path.join(folder, fname)
            image = preprocess(Image.open(path).convert('RGB')).unsqueeze(0).to(device)
            with torch.no_grad():
                emb = model.encode_image(image)
                emb /= emb.norm(dim=-1, keepdim=True)
            embeddings.append(emb.cpu().numpy())
            paths.append(path)
        except Exception as e:
            print(f"❌ Error loading {fname}: {e}")

    index = faiss.IndexFlatIP(embeddings[0].shape[1])
    matrix = np.vstack(embeddings).astype("float32")
    index.add(matrix)
    return index, paths


index, image_paths = load_embeddings()
if index is None:
    index = faiss.IndexFlatIP(512)
    image_paths = []

# ✅ API-based view for React
@csrf_exempt
def search_view(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)

    form = ImageUploadForm(request.POST, request.FILES)
    if not form.is_valid():
        return JsonResponse({'error': 'Invalid form data'}, status=400)

    img = Image.open(request.FILES['image'])
    img_tensor = preprocess(img).unsqueeze(0).to(device)

    with torch.no_grad():
        query = model.encode_image(img_tensor)
        query /= query.norm(dim=-1, keepdim=True)

    D, I = index.search(query.cpu().numpy().astype("float32"), 3)

    print("🔎 FAISS returned indices:", I)
    print("📁 image_paths length:", len(image_paths))

    if len(I) == 0 or len(I[0]) == 0:
        return JsonResponse({'results': [], 'message': 'No matches found.'})

    result_paths = [
        '/media/sample_images/' + os.path.basename(image_paths[i])
        for i in I[0]
        if 0 <= i < len(image_paths)
    ]

    return JsonResponse({'results': result_paths})

@csrf_exempt
def reload_index(request):
    global index, image_paths
    index, image_paths = load_embeddings()
    
    if index is not None:
        print(f"✅ Reloaded index with {len(image_paths)} images.")
        return JsonResponse({'status': 'success', 'message': f'Reloaded {len(image_paths)} images.'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Failed to reload images.'}, status=500)

