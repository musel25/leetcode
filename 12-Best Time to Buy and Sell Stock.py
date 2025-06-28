'''You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

Example 1:

Input: prices = [10,1,5,6,7,1]

Output: 6
Explanation: Buy prices[1] and sell prices[4], profit = 7 - 1 = 6.

Example 2:

Input: prices = [10,8,7,5,2]

Output: 0
Explanation: No profitable transactions can be made, thus the max profit is 0.
'''

# Thoughts
    # Greedy aproach is not optimal
        # I will have 2 pointers, i will move them inwards depending wich optimize more the profit
        # At each iteration i will keep the max profit. 

# Extra that I missed
    # Two pointers was correct, but initialization was wrong. It is sliding window problem

# prices = [1,2,11,4,7]

# l = 0
# r = len(prices)-1 
# max_profit = max(0, prices[r]- prices[l])

# while l<r:
#     # moving r    
#     if prices[r]- prices[l+1]< prices[r-1]- prices[l]:
#         r -= 1
#     else:
#     # moving l
#         l += 1
#     max_profit = max(prices[r]- prices[l], max_profit)

# print(max_profit)

