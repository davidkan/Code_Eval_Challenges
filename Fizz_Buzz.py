import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
test = test.split(' ')
    a = int(test[0])
    b = int(test[1])
    n = int(test[2])
    e = 0

    for i in range(n):
        if e > 0:
            print(" ", end="")
            e += 1
            i += 1

            if i % a == 0 and i % b == 0:
                print("FB", end="")
                elif i % a == 0:
                print("F", end="")
                elif i % b == 0:
                print("B", end="")
                else:
                print(i, end="")
            print("")
        test_cases.close()
