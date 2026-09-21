class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        score = 0
        counter = 0

        for event in events:
            if event in ("0", "1", "2", "3", "4", "5", "6"):
                score += int(event)
            elif event == "W":
                counter += 1
                if counter == 10:
                    return [score, counter]
            elif event in ("WD", "NB"):
                score += 1
        
        return [score, counter]