# Functions: *args, **kwargs (arguments, keyword args)
# =============================================================================
print(sum((1, 2, 3, 4, 5)))


def my_sum_fixed(a, b, c):
    return a + b + c

def my_sum_dynamic(*args):
    return(sum(args))

def key_value_dict(**kwargs):
    print(kwargs.get("weight"))
    return((kwargs.values()))

# Client
# =============================================================================
print(my_sum_fixed(1, 2, 3))
print()

print(my_sum_dynamic(1, 2, 3, 4, 5))
print(my_sum_dynamic(1, 2, 3))
print(my_sum_dynamic(1, 2, 3, 9, 6, 5, 4, 3))
print()

print(key_value_dict(name='Ray', weight=145, age=35))
print()

# Exercises
# =============================================================================
def merge_lists(list1, list2):
    return list1 + list2
print(merge_lists([1, 2, 3], [4, 5, 6]))
print()

def separate(str):
    return list(str)
print(separate("apple"))
print()

def multi_merge(list1, str):
    return list1 + str.split() + list(str)
print(multi_merge([1, 2, 3,], 'hello world'))
print()

def last_list(*args):
    # return args[-1 :len(args)]
    return args[-1]
print(last_list([1, 2, 3], [4, 5, 6], [7, 8, 9]))
print()

def key_list_items(key, **kwargs):
    value_list = kwargs[key]
    closing_price = value_list[-1]
    return closing_price
result = key_list_items("amzn", msft=[245.03, 246.13, 242.92, 243.70], goog=[2104.36, 2152.68, 2104.36, 2121.90], amzn=[3254.05, 3308.30, 3253.59, 3268.95])
print(result)
print()