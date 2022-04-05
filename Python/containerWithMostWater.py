"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

"""

#solution
1. Time Complexity: O(N) : Space Complexity: O(1)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Two Pointer
        # Time Complexity: O(N) Space Complexity: O(1)
        start,end,MaxArea=0,len(height)-1,0
        while(start<end):
            ContainerWidth = end - start
            ContainerHeight = 0
            if (height[start] > height[end]):
                ContainerHeight = height[end]
                end -= 1
            else:
                ContainerHeight = height[start]
                start += 1
            TempArea = ContainerWidth * ContainerHeight
            MaxArea = max(MaxArea,TempArea)
        return (MaxArea)
2. Brute Force Method:
Time Complexity: O(N^2) : Space Complexity: O(1)

In this we will simply try to make all pair of combination and find the area and if it bigger then update the MaxArea variable.


        MaxArea=0
        for i in range (len(height)-1):
            for j in range (i+1,len(height)):
                ContainerWidth = j - i
                ContainerHeight = min(height[i],height[j])
                TempArea = ContainerWidth * ContainerHeight
                MaxArea = max(MaxArea,TempArea)
        return (MaxArea)
