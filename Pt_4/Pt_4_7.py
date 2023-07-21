from itertools import permutations
nums = list(map(int, input("Введите список чисел: ").split()))
all_permutations = list(permutations(nums))
print(all_permutations)
