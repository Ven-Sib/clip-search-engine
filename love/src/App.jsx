import React, { useState } from 'react';
import bgImage from './assets/lovely.jpg'; // make sure the image is in /src/assets/

function App() {
  const [results, setResults] = useState([]);
  const [image, setImage] = useState(null);
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!image) return;

    setLoading(true);
    setMessage('');
    setResults([]);

    const formData = new FormData();
    formData.append('image', image);

    try {
      const res = await fetch('http://127.0.0.1:8000/search/', {
        method: 'POST',
        body: formData,
        credentials: 'include',
      });

      if (!res.ok) {
        setMessage('❌ Something went wrong with the upload.');
        setLoading(false);
        return;
      }

      const data = await res.json();

      if (data.results && data.results.length > 0) {
        setResults(data.results);
        setMessage('✅ Matches found!');
      } else {
        setMessage('No matches found.');
      }
    } catch (error) {
      console.error('Fetch failed:', error);
      setMessage('❌ Could not connect to server.');
    }

    setLoading(false);
  };

  return (
    <div
      className="min-h-screen bg-cover bg-center text-white flex items-center justify-center px-4 py-10"
      style={{ backgroundImage: `url(${bgImage})` }}
    >
      <div className="w-full max-w-5xl bg-black/70 backdrop-blur-lg shadow-2xl rounded-3xl p-10 border border-gray-600">
        <h2 className="text-4xl font-extrabold text-center mb-8 tracking-wide">
          🔍 Visual Search Engine
        </h2>

        <form onSubmit={handleSubmit} className="flex flex-col gap-6 px-4 sm:px-8">
          <input
            type="file"
            onChange={(e) => setImage(e.target.files[0])}
            className="text-white bg-gray-800 border border-gray-600 px-4 py-3 rounded-lg cursor-pointer file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-yellow-400 file:text-black hover:file:bg-yellow-500"

          />

          <button
            type="submit"
            disabled={loading}
            className={`px-6 py-3 rounded-lg font-semibold text-black ${
              loading ? 'bg-gray-400 cursor-not-allowed' : 'bg-yellow-400 hover:bg-yellow-500'
            } transition-all`}
          >
            {loading ? 'Searching...' : 'Search 🔍'}
          </button>
        </form>

        {message && (
          <p className="mt-6 text-center font-medium text-green-400">{message}</p>
        )}

        <div className="mt-10 grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6 px-2">
          {results.map((url, idx) => (
            <div key={idx} className="bg-gray-800 rounded-xl overflow-hidden shadow-md">
              <img
                src={`http://127.0.0.1:8000${url}`}
                alt={`Match ${idx}`}
                className="w-full h-48 object-cover"
              />
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

export default App;
