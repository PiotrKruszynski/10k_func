from time import sleep


# Napisz generator liczb od 1 do nieskończoności, z krokiem 1
def outer_fn(index=1):
    def inner_fn(new_index=None):
        nonlocal index
        if new_index is not None:
            index = new_index

        result = index
        index += 1
        return result

    return inner_fn


gen_id = outer_fn()
print(gen_id())
print(gen_id())
print(gen_id())
print(gen_id())

#bez nonlocal

def outer_fn(index=1):
    def inner_fn(new_index=None):
        if new_index is not None:
            inner_fn.index = new_index

        result = inner_fn.index
        inner_fn.index += 1
        return result

    inner_fn.index = index

    return inner_fn

# napisz funkcje, która w zależności od pierwszego elementu kolekcji,
# będzie dzielić nst elementy bądź mnożyć

def calculate():
    predicate = None

    def inner(item):
        nonlocal predicate

        if predicate is None:
            predicate = item >= 0

        if predicate:
            return item * 2
        return item / 2

    return inner


r1 = list(map(calculate(), [1,2,3,4]))
r2 = list(map(calculate(), [-1,2,3,4]))

print(r1,r2)

# memoizing lever -1
# zapamiętywanie wyniku funkcji, żeby reużyć, aby nie liczyć ponownie
# to technika cach'owania
# Zasady:
# - fn musi być pure
# - relatywnie niewielka ilość różnych kombinacji parametrów




# def memoize():
#     cache = {}
#
#     def inner(a, b):
#         key = f"{a}{b}"
#         if key not in cache:
#             # intensive CPU task
#             sleep(3)
#             cache[key] = a + b
#         return cache[key]
#
#     return inner

#----------------------------------------------------------------------------------------

def memoize(cb):
    cache = {}

    def inner(*args):
        if args not in cache:
            cache[args] = cb(*args)
        return cache[args]

    return inner


def calculate_magic(a,b,/):
    # intensive CPU task
    sleep(3)
    return a + b

def calculate_tribonacci(a, b, c,/):
    # intensive CPU task
    sleep(3)
    return a + b + c

calculate_magic_cache = memoize(calculate_magic)
calculate_tribonachi_cache = memoize(calculate_tribonacci)

print(calculate_magic_cache(1,2))
print(calculate_magic_cache(2,2))
print(calculate_tribonachi_cache(1,2,4))
print(calculate_tribonachi_cache(2,2,3))

#-----------------------------------------

# def power10(base):
#     return base **10
#
# print(power10(2))
#
# # factory function (factory design pattern)
# def power_n(exponent):
#     def inner(base):
#         return base ** exponent
#
#     return inner
#
# power_2 = power_n(2)
#
# print(power_2(2))