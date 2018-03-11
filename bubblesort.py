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
        c[i] = input('Number: ')


def print_list(b):
    for i in range(0, len(b)):
        print(b[i])


size = input('list size: ')
a = [0] * int(size)

fill_list(a)

bubble_sort(a)

print_list(a)
