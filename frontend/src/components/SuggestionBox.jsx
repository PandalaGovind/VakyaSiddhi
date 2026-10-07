import React from 'react';

export default function SuggestionBox({ suggestions, originalWord }) {

    if (!suggestions || suggestions.length === 0) return null;

    return (
        <div>
            <h3>Suggestions for "{originalWord}":</h3>

            {suggestions.map((item, index) => (
                <div key={index}>
                    {item.word} Score: {item.score.toFixed(5)}
                </div>
            ))}
        </div>
    );
}