def merge_sort(letters_list, start=0, end=None):
    if end is None:
        end = len(letters_list)
    if (end - start) > 1:
        mid = (start + end) // 2
        merge_sort(letters_list, start, mid)
        merge_sort(letters_list, mid, end)
        merge(letters_list, start, mid, end)
    return letters_list


def merge(letters_list, start, mid, end):
    left = letters_list[start:mid]
    right = letters_list[mid:end]

    left_index, right_index = 0, 0

    for general_index in range(start, end):
        if left_index >= len(left):
            letters_list[general_index] = right[right_index]
            right_index += 1
        elif right_index >= len(right):
            letters_list[general_index] = left[left_index]
            left_index += 1
        elif left[left_index] < right[right_index]:
            letters_list[general_index] = left[left_index]
            left_index += 1
        else:
            letters_list[general_index] = right[right_index]
            right_index += 1


def is_anagram(first_string, second_string):
    if not first_string and not second_string:
        return ("", "", False)
    first_letters_list = list(first_string.lower())
    second_letters_list = list(second_string.lower())
    first_string_sorted = "".join(merge_sort(first_letters_list))
    second_string_sorted = "".join(merge_sort(second_letters_list))
    if first_string_sorted == second_string_sorted:
        return (first_string_sorted, second_string_sorted, True)
    else:
        return (first_string_sorted, second_string_sorted, False)
