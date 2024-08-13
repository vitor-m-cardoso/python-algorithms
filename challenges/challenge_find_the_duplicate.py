def validate_list(numbers_list):
    if not numbers_list or len(numbers_list) < 2:
        return False
    for number in numbers_list:
        if not isinstance(number, int) or number < 0:
            return False
    return True
    if start < end:
        p = partition(numbers_list, start, end)
        quick_sort(numbers_list, start, p - 1)
        quick_sort(numbers_list, p + 1, end)
    return numbers_list


def find_duplicate(nums):
    if not validate_list(nums):
        return False

    nums.sort()

    for index in range(len(nums) - 1):
        if nums[index] == nums[index + 1]:
            return nums[index]
    return False
