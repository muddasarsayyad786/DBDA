def increment(n):
    n += 1
    return n


def increment_list(lst):
    lst[0] += 1


num = 10
incremented = increment(num)
print(incremented)

my_lst = [10]
increment_list(my_lst)
print(my_lst[0])