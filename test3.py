def median(list):
    result = 0.0
    list.sort()
    if len(list) == 1:
        result = list[0]
    elif len(list) % 2 == 1:
        result = list[len(list)/2]
    else:
        result = float(sum([list[len(list)/2-1], list[len(list)/2]]))
        result /= 2
    return result


print median([4,5,5,4])