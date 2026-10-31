class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = []
        spaces_count = 0
        word = ""

        for ch in text:
            if ch == " ":
                spaces_count += 1
                if word:
                    words.append(word)
                    word = ""
            else:
                word += ch
        
        if word:
            words.append(word)
            word = ""
        
        k = len(words)
        if k == 1:
            return words[0] + " " * spaces_count
        else:
            extra_spaces = spaces_count % (k - 1)
            dis_spaces = spaces_count // (k - 1)
            result = words[0] + dis_spaces * " "

            for idx in range(1, k):
                result += words[idx]
                if idx < k - 1:
                    result += dis_spaces * " "

            return result + extra_spaces * " "
