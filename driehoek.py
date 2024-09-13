from itertools import combinations, permutations


num = 0


def has_consecutive(starting):
    return any(starting[i + 1] - starting[i] == 1 for i in range(len(starting)) if i <= len(starting) - 2)


def calculate_sum(starting):
    global num
    num += 1
    if num % 200_000 == 0:
        print(num)
    last = starting
    sum_ = max(starting) - min(starting)
    for _ in range(len(starting) - 1):
        last = [last[i] + last[i + 1] for i in range(len(last) - 1)]
        diff = (max(last) - min(last)) if len(last) > 1 else last[0]
        sum_ += diff
    return sum_


starting = range(-5, 6)
max_sum = float("-inf")
max_starting = None
for comb in combinations(starting, 9):
    for perm in permutations(comb):
        if not has_consecutive(perm):
            sum_ = calculate_sum(perm)
            if sum_ > max_sum:
                max_sum = sum_
                max_starting = perm
print(max_starting, max_sum)