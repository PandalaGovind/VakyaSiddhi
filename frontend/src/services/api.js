const API_BASE_URL = 'http://127.0.0.1:8000/api';

export async function fetchWordSuggestions(word) {
  try {
    const response = await fetch(`${API_BASE_URL}/correct`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ word }),
    });

    if (!response.ok) {
      throw new Error(`Server returned error: ${response.status}`);
    }

    return await response.json();
  } catch (error) {
    console.error('API Error:', error);
    throw error;
  }
}