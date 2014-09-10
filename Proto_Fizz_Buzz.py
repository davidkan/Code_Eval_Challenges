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
            ii = i + 1
            if ii % a == 0 and ii % b == 0:
                print("FB", end="")
                elif ii % a == 0:
                print("F", end="")
                elif ii % b == 0:
                print("B", end="")
                else:
                print(i, end="")
                print("")
            test_cases.close()
