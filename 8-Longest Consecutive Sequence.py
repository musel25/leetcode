# Thoughts
    # I create set. Then sort it. or use directly sorted set.
    # Then a for loop over the sorted set to verify continuous
    # you have to iterate over all array otherwise doesnt work because soution could be ahead, not in the beginning, cannot brea
    # Use a hasmap to save, lenghts and indices dont need both indices can recover by length, sort dict by length
    # Given we want only max value, then not need hasmap

# Extra that I missed
    # Hash set and map



nums=[0,3,2,5,4,6,1,1]

set_nums = set(nums)
sorted_set = sorted(set_nums)
curr = 1
len_sol  = 1
prev = sorted_set[0]
indices ={}
for i in range(1,len(sorted_set)):
    if sorted_set[i] == prev+1:
        curr +=1
        prev = sorted_set[i] 
    else:
        len_sol = max(len_sol, curr)
        curr = 1
        prev = sorted_set[i] 
print(max(len_sol, curr))

