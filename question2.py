import math
def minEatingSpeed(piles,h):
    left , right = 1, max(piles)

    while left < right:
        mid = (left+right)//2

        hours = sum(math.ceil(pile/mid)for pile in piles)

        if hours <= h:
            right = mid
        else:
            left = mid+1
        
    return left

piles = list(map(int,input().split()))
h = int(input())
print(minEatingSpeed(piles,h))