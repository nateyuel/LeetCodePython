class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        
        distance_x = max(x1, min(xCenter, x2))
        distance_y = max(y1, min(yCenter, y2))

        dx = xCenter - distance_x
        dy = yCenter - distance_y
    
        return dx ** 2 + dy ** 2 <= radius ** 2