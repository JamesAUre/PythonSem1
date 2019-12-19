def quick_sort(a_list):
    if len(a_list) < 2: return a_list
    lesser = quick_sort([x for x in a_list[1:] if x <= a_list[0]])
    bigger = quick_sort([x for x in a_list[1:] if x > a_list[0]])
    return sum([lesser, [a_list[0]], bigger], [])

a_list = [1,4,7,5,2,8,9,43,22]

print(quick_sort(a_list))