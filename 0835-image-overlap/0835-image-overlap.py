class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        translation_count = Counter()
      
        for row in range(n):
            for col in range(n):
                if img1[row][col] == 1:

                    for row2 in range(n):
                        for col2 in range(n):
                            if img2[row2][col2] == 1:

                                translation_vector = (row - row2, col - col2)
                                translation_count[translation_vector] += 1
      
        return max(translation_count.values()) if translation_count else 0
