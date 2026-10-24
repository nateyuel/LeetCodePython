class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        calend = defaultdict(bool)
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        alice_arrive_month = int(arriveAlice[:2])
        alice_leave_month = int(leaveAlice[:2])
        alice_arrive_day = int(arriveAlice[3:])
        alice_leave_day = int(leaveAlice[3:])

        bob_arrive_month = int(arriveBob[:2])
        bob_leave_month = int(leaveBob[:2])
        bob_arrive_day = int(arriveBob[3:])
        bob_leave_day = int(leaveBob[3:])

        while alice_arrive_month <= alice_leave_month:
            calend[(alice_arrive_month, alice_arrive_day)] = True
            if alice_arrive_month < alice_leave_month:
                if alice_arrive_day < days[alice_arrive_month - 1]:
                    alice_arrive_day += 1
                else:
                    alice_arrive_month += 1
                    alice_arrive_day = 1
            else:
                if alice_arrive_day < alice_leave_day:
                    alice_arrive_day += 1
                else:
                    break

        result = 0

        while bob_arrive_month <= bob_leave_month:
            if calend[(bob_arrive_month, bob_arrive_day)]:
                result += 1
            if bob_arrive_month < bob_leave_month:
                if bob_arrive_day < days[bob_arrive_month - 1]:
                    bob_arrive_day += 1
                else:
                    bob_arrive_month += 1
                    bob_arrive_day = 1
            else:
                if bob_arrive_day < bob_leave_day:
                    bob_arrive_day += 1
                else:
                    break
        
        return result 

        
        
        



