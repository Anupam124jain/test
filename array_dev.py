nums = [3,3]
target = 6

def two_sum(nums, target):
    print("--------nums--------")
    print(nums)
    print("------------nums------")

    print("-------target----------")
    print(type(target))
    print("--------target---------")
    add_idx = []

    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if j == len(nums) - 1:
                break
            sum = nums[i] + nums[j+1]
            if sum == target:
                add_idx.append(i)
                add_idx.append(j + 1)

    return add_idx

# try:
#     my_list = []
#     while True:
#         my_list.append(int(input()))
# except:
#     print(my_list)


# target = int(input())

my_list = [1, 9, 6, 3]
target = 14
s = two_sum(my_list, target)
print(s)