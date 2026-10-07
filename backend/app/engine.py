import string
from collections import Counter
from app.utils import extract_words

class AutocorrectEngine:
    def __init__(self, corpus_path: str):
        self.vocab = set()
        self.word_counts = Counter()
        self.total_words = 0
        self.probabilities = {}
        self.load_corpus(corpus_path)

    def load_corpus(self, path: str):
        try:
            with open(path, "r", encoding="utf-8") as f:
                words = extract_words(f.read())
            self.word_counts = Counter(words)
            self.vocab = set(self.word_counts.keys())
            self.total_words = sum(self.word_counts.values()) or 1
            self.probabilities = {w: count / self.total_words for w, count in self.word_counts.items()}
        except FileNotFoundError:
            print(f"Warning: Corpus file not found at {path}. Starting with empty vocabulary.")

    def _edit_distance_one(self, word: str) -> set[str]:
        letters = string.ascii_lowercase
        splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
        deletes = [L + R[1:] for L, R in splits if R]
        transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
        replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
        inserts = [L + c + R for L, R in splits for c in letters]
        return set(deletes + transposes + replaces + inserts)

    def get_corrections(self, word: str, top_n: int = 3) -> list[dict]:
        word = word.lower()
        
        # If word exists in vocabulary, return it as top candidate
        if word in self.vocab:
            return [{"word": word, "score": self.probabilities.get(word, 0.0)}]

        # Generate candidates at Edit Distance 1
        candidates = self._edit_distance_one(word).intersection(self.vocab)

        # Fallback to level 2 candidates if distance 1 is empty
        if not candidates:
            candidates = {
                cand2 
                for cand1 in self._edit_distance_one(word) 
                for cand2 in self._edit_distance_one(cand1)
            }.intersection(self.vocab)

        sorted_candidates = sorted(
            [(c, self.probabilities.get(c, 0.0)) for c in candidates],
            key=lambda x: x[1],
            reverse=True
        )[:top_n]

        return [{"word": cand, "score": prob} for cand, prob in sorted_candidates]