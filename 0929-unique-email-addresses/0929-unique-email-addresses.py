class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        unique_email = set()

        for email in emails:
            n = len(email)
            idx = 0
            valid = True
            curr = ""
            at_occured = False

            while idx < n:
                
                if email[idx] == "+" and not at_occured:
                    valid = False
                elif email[idx] == "@":
                    valid = True
                    at_occured = True

                if valid:
                    if at_occured:
                        curr += email[idx]
                    elif email[idx] != ".":
                        curr += email[idx]
                
                idx += 1
            
            unique_email.add(curr)

        return len(unique_email)
            
            