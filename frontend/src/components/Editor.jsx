import React, { useState } from 'react';

import { fetchWordSuggestions } from '../services/api';

import SuggestionBox from './SuggestionBox';

export default function Editor() {
    const [inputText, setInputText] = useState('');
    const [activeWord, setActiveWord] = useState('');
    const [suggestions, setSuggestions] = useState([]);
    const [loading, setLoading] = useState(false);

    const handleCheck = async () => {
        if (!inputText.trim()) return;

        setLoading(true);

        try {
            const data = await fetchWordSuggestions(inputText.trim());

            setActiveWord(data.original);
            setSuggestions(data.suggestions);
        } catch (err) {
            alert('Failed to connect to VakyaSiddhi backend.');
        } finally {
            setLoading(false);
        }
    };

    return (
        <div>
            <input
                type="text"
                value={inputText}
                onChange={(e) => setInputText(e.target.value)}
                placeholder="Enter a word (e.g. hte, writng)..."
                onKeyDown={(e) => e.key === 'Enter' && handleCheck()}
            />

            <button onClick={handleCheck} disabled={loading}>
                {loading ? 'Checking...' : 'Correct'}
            </button>

            <SuggestionBox
                suggestions={suggestions}
                originalWord={activeWord}
            />
        </div>
    );
}