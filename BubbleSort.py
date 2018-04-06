 /*
  * .Sort() is better
  */
    def position_swap(x, bigger, smaller):
    x[bigger] = int(x[bigger]) + int(x[smaller])
    x[smaller] = int(x[bigger]) - int(x[smaller])
    x[bigger] = int(x[bigger]) - int(x[smaller])


def bubble_sort(d):
    for j in range(0, len(d)):
        for i in range(0, len(d) - 1):
            if int(d[i]) > int(d[i + 1]):
                position_swap(d, i, i + 1)


def fill_list(c):
    for i in range(0, len(c)):
        c[i] = input('{0}'.format(i + 1) + st_nd_rd_or_else(i + 1) + ' Number: ')


def print_list(b):
    for i in range(0, len(b)):
        print(b[i])


def st_nd_rd_or_else(var_int):
    if var_int == 1 or 1 == var_int % 10 or var_int == 11 or var_int == 12 or var_int == 13:
        string = "st"
    elif var_int == 2 or 2 == var_int % 10:
        string = "nd"
    elif var_int == 3 or 3 == var_int % 10:
        string = "rd"
    else:
        string = "th"
    return string


size = input('list size: ')
a = [0] * int(size)

fill_list(a)

bubble_sort(a)

print_list(a)
