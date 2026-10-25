class Solution:
    def findLatestTime(self, s: str) -> str:
        time = list(s)

        for idx, ch in enumerate(time):
            if ch == "?":
                if idx == 0:
                    if time[idx + 1] == "?" or int(time[idx + 1]) <= 1:
                        time[idx] = "1"
                    else:
                        time[idx] = "0"
                elif idx == 1:
                    if time[idx - 1] == "1":
                        time[idx] = "1"
                    else:
                        time[idx] = "9"
                elif idx == 3:
                    time[idx] = "5"
                else:
                    time[idx] = "9"
        
        return "".join(time)