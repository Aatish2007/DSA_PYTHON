class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        def date_to_day_of_year(date_str: str) -> int:
            """Converts 'MM-DD' string to 1-indexed day of the year."""
            month, day = map(int, date_str.split('-'))
            return sum(days_in_months[:month - 1]) + day
        alice_start = date_to_day_of_year(arriveAlice)
        alice_end = date_to_day_of_year(leaveAlice)
        bob_start = date_to_day_of_year(arriveBob)
        bob_end = date_to_day_of_year(leaveBob)
        together_start = max(alice_start, bob_start)
        together_end = min(alice_end, bob_end)
        return max(0, together_end - together_start + 1)