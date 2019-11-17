a = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]


def remove_duplicate(input_list):
    print("This should remove duplicate values and return the result array")
    result_list = []
    for item in input_list:
        if item not in result_list:
            result_list.append(item)
    return result_list


print(remove_duplicate(a))  # [10, 20, 30, 50, 60, 40, 80]
