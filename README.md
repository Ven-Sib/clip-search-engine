# 🔍 Visual Search Engine — React + Django + OpenAI CLIP

A powerful, AI-powered visual search engine that allows users to upload an image and instantly find visually similar images using OpenAI’s CLIP model. Built from scratch with a beautiful UI, smooth performance, and full-stack integration.

---

## 🚀 Features

- 🔎 Upload any image to search against a dataset of sample images
- 🎯 Returns top 3 visually similar matches using FAISS and CLIP
- 🧠 Built on OpenAI’s CLIP (ViT-B/32) for deep semantic + visual encoding
- 🖥️ Frontend built with React + Tailwind CSS (fully responsive)
- 🐍 Backend powered by Django + PyTorch + FAISS
- 🧊 Reloadable index without server restart
- 🎨 Beautiful UI with background image, styled buttons, and responsive grid

---

## 🛠️ Tools & Technologies Used

| Stack        | Technologies                                                                 |
|--------------|-------------------------------------------------------------------------------|
| Frontend     | React, Tailwind CSS, Vite, JSX, GitHub Pages                                 |
| Backend      | Django, Python, CLIP (PyTorch), FAISS                 |
| AI/ML        | OpenAI CLIP model (`ViT-B/32`), Torch, NumPy, PIL                             |
| Deployment   | Git, GitHub, GitHub Pages (React only version)                               |
| Utilities    | CSRF handling, custom reload endpoint, dynamic embedding updates             |

---

## 🧠 Skills Demonstrated

- ✅ Full-stack application development (frontend + backend)
- ✅ REST API creation and integration with React
- ✅ Implementing and working with pretrained AI models
- ✅ Image embedding, normalization, and similarity search (cosine similarity via FAISS)
- ✅ State management in React with `useState`
- ✅ Tailwind CSS for responsive, modern styling
- ✅ Git/GitHub workflow, deployment with GitHub Pages
- ✅ Clean UI/UX, loading states, error handling, and file upload

---

## 🖼️ Demo Screenshot

![demo](![Screenshot 2025-04-14 211707](https://github.com/user-attachments/assets/eec14247-f28f-40e4-8020-30229b6e71b8)
) <!-- Replace with an actual screenshot path or GitHub URL -->

---

## 📦 How to Run Locally

```bash
# Clone the repo
git clone https://github.com/your-username/clip-search-engine.git
cd clip-search-engine

# Frontend
cd frontend
npm install
npm run dev

# Backend
cd ../backend
pip install -r requirements.txt
python manage.py runserver
