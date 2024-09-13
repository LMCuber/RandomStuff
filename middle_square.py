def middle_square(seed, iterations, middle=4):
    nums = []
    num = seed
    for _  in range(iterations):
        num **= 2
        num = str(num)
        if len(num) % 2 == 0:
            num = "0" + num
        num = num[(len(num) - 4) // 2: len(num) - (len(num) - 4) // 2]
        num = int(num)
        nums.append(num)
    nums = "".join([str(n) for n in nums])
    return nums
    
    
print(middle_square(42846, 518 // 5, 5))
