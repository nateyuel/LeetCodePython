class Solution:
    def haveConflict(self, event1: list[str], event2: list[str]) -> bool:
        start_time_one = int(event1[0][:2]) * 60 + int(event1[0][3:5])
        end_time_one = int(event1[1][:2]) * 60 + int(event1[1][3:5])
        start_time_two = int(event2[0][:2]) * 60 + int(event2[0][3:5])
        end_time_two = int(event2[1][:2]) * 60 + int(event2[1][3:5])

        return (start_time_one >= start_time_two and start_time_one <= end_time_two) or (end_time_one >= start_time_two and end_time_one <= end_time_two) or (start_time_two >= start_time_one and start_time_two <= end_time_one) or (end_time_two >= start_time_one and end_time_two <= end_time_one)