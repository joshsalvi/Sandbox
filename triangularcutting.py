def all_triangle_numbers(n):
    x = []
    for i in range(1, n + 1):
        x.append(str((i ** 2 + i) // 2))
        x[i - 1] = int(x[i - 1])
        if int(x[i - 1]) > n:
            return x


def is_consecutive(number_list, j):
    start_index = number_list.index(j[0])
    end_index = number_list.index(j[-1])
    if start_index + len(j) - 1 == end_index:
        return True
    else:
        return False


def checkio(number):
    numberlist = all_triangle_numbers(number)
    length = len(numberlist)
    result = 0
    while length > 1:
        for ind in range(len(numberlist) - length + 1):
            if sum(numberlist[ind:ind + length]) == number and is_consecutive(numberlist, numberlist[ind:ind + length]):
                return numberlist[ind:ind + length]

        length -= 1
    else:
        return []


print checkio(882)

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(64) == [15, 21, 28], "1st example"
    assert checkio(371) == [36, 45, 55, 66, 78, 91], "1st example"
    assert checkio(225) == [105, 120], "1st example"
    assert checkio(882) == [], "1st example"
