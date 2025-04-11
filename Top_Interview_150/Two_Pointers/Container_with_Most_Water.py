class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

        Find two lines that together with the x-axis form a container, such that the container contains the most water. Notice that you may not slant the container.

        Return the maximum amount of water a container can store.

        Input: height = [1,8,6,2,5,4,8,3,7]
        Output: 49
        """

        lp = 0
        rp = len(height) - 1
        max_volume = 0

        while lp < rp: 
            dist = rp - lp 
            curr_volume = dist * min(height[lp], height[rp]) 
            max_volume = max(curr_volume, max_volume) 
            if height[lp] < height[rp]:
                lp += 1
            else:
                rp -= 1

        return max_volume