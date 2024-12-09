from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # Find the maximum candies any kid has
        max_candies = max(candies)
        
        # Create the result list
        result = []
        
        # For each kid, check if they can have the most candies
        for candy in candies:
            if candy + extraCandies >= max_candies:
                result.append(True)
            else:
                result.append(False)
        
        return result

