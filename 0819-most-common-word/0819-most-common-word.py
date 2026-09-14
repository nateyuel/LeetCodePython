class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned_set = set(banned)
        clean_paragraph = paragraph.translate(str.maketrans(string.punctuation, " " * len(string.punctuation)))
        words = clean_paragraph.lower().split(" ")

        count = Counter(word for word in words if word not in banned_set and word != "")

        freq_word = ""
        max_freq = 0
        print(count)

        for word, freq in count.items():
            if freq > max_freq:
                freq_word = word
                max_freq = freq
        
        return freq_word