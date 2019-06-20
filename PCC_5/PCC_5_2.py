a = "Today is a good day."
b = "Today Is A Good Day."
print("Is a == b? I predict false.")
print(a == b)

a = a.lower()
b = b.lower()
print("Is a == b? I predict Ture.")
print(a == b)

test_a = 14
test_b = 23
if test_a == test_b:
    print("test_a equals test_b.")

if test_a > test_b:
    print("test_a is bigger than test_b.")

if test_a < test_b:
    print("test_a is smaller than test_b.")

if test_a != test_b:
    print("test_a is not equal to test_b")

a = 14
b = 23
c = 3
if a > c and b > c:
    print("c is the smaller one.")

if a > c or b > c:
    print("We cannot say that c is the smaller one.")

a = [1, 3, 44, 23, 43, 22, 12]
b = 3
c = 53
if b in a:
    print("b is in list a.")
else:
    print("b is not in list a.")

if c not in a:
    print("c is not in list a.")
else:
    print("c is in list a.")
