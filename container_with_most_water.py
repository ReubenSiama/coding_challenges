# Container with most water
# Given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
height = [1,8,6,2,5,4,8,3,7]
# height = [1,8,6,2,5,4,7,3,8]
# height = [1,1]

def findMaxCapacity():
    maxCapacity = 0
    for i in range(len(height)):
        length = len(height) - 1
        while length >= 0:
            min = height[i] if height[i] < height[length] else height[length]
            dist = length - i
            capacity = min * dist
            if capacity > maxCapacity:
                maxCapacity = capacity
            length -= 1
        i -= 1
    return maxCapacity

print(findMaxCapacity())
