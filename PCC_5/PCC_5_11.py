nums = list(range(1, 10))
for num in nums:
    print(num)

for num in nums:
    if num <= 3:
        if num == 1:
            print("\n" + str(num) + "st")
        if num == 2:
            print("\n" + str(num) + "nd")
        if num == 3:
            print("\n" + str(num) + "rd")
    else:
        print("\n" + str(num) + "th")
    