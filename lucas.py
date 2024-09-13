import matplotlib.pyplot as plt

nums = [2, 1]
for i in range(100 - len(nums)):
    nums.append(nums[-2] + nums[-1])

verh = []
for i in range(2, len(nums)):
    verh.append(nums[i] / nums[i - 1])

print(verh)
plt.plot(verh)
plt.show()
