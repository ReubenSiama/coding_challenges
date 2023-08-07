# Given an array k, find the special integer x such that there are x integers in the array that are larger than or equal to x. The special integer doesn't have to exist in the array k.
numbers = [2,4,1,0,4]
count = 0
specialNumber = 2
for k in numbers:
    if k >= specialNumber:
        count += 1

print(count)
