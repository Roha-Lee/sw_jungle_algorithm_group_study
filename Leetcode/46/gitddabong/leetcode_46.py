def dfs(temp, depth = 0):
    if depth == len(nums):
        result.append(temp[:])
        return
    
    for i in range(len(nums)):
        if visited[i] == False:
            visited[i] = True
            temp[depth] = nums[i]
            dfs(temp, depth + 1)
            # print(temp, visited, depth)
            visited[i] = False
        
nums = [1,2,3]

visited = [False] * len(nums)
result = []
temp = [0] * len(nums)
dfs(temp)

print(result)