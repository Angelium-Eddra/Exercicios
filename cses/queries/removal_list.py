
n = int(input())

nums = [int(x) for x in input().split(" ")]
index_removals = [int(x) for x in input().split(" ")]
removed_nums = []

for index in index_removals:
    removed_nums.append(nums[index -1])
    nums.pop(index -1)

print(removed_nums)