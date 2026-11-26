class Solution:
    def canAliceWin(self, n: int) -> bool:
        if n < 10:
            return False

        n -= 10
        turn = 9
        person = "Alice"

        while n >= turn:
            n -= turn
            turn -= 1
            person = "Alice" if person == "Bob" else "Bob"

        return person == "Alice"
