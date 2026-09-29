class Solution:
    def removeAnagrams(self, words: list[str]) -> list[str]:
        ans = [words[0]]
        n = len(words)

        def compare(word1, word2):
            freq = [0] * 26
            for ch in word1:
                freq[ord(ch) - ord("a")] += 1
            for ch in word2:
                freq[ord(ch) - ord("a")] -= 1

            return all(x == 0 for x in freq)

        for i in range(1, n):
            if compare(words[i], words[i - 1]):
                continue
            ans.append(words[i])

        return ans
