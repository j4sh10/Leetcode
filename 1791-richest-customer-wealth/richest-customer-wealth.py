from typing import List
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        person_acc = []  # To store total wealth of each account
        for account in accounts:
            total_in_acc = 0  # Reset total for each account
            for money in account:
                total_in_acc += money  # Add money to the total
            person_acc.append(total_in_acc)  # Append the total wealth to the list
        max_wealth = person_acc[0]  # Assume the first wealth is the maximum
        for wealth in person_acc:
            if wealth > max_wealth:
                max_wealth = wealth  # Update if a larger wealth is found
            else:
                continue  # Do nothing if the current wealth is smaller
        return max_wealth
