class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        maxCandies = max(candies)
        result = []
        for i in range(len(candies)):            
            result.append(candies[i] + extraCandies >= maxCandies)
        return result