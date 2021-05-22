def main():
    nums = [int(x) for x in input().split()]
    nums = list(dict.fromkeys(nums))
    nums.sort()
    
    for x in check_diff(nums):
        print(x[0],x[1])
    
def check_diff(nums):
    list_of_diff = []
    for i, num in enumerate(nums):
        try:
            if num + 1 == nums[i+1]:
                list_of_diff.append([num, nums[i+1]])
        except IndexError:
            break
    return list_of_diff

if __name__ == "__main__":
    main()