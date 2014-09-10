import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.replace('\n', '')
    test = test.split(' ')
    b = []
    b.extend(test)
    b = b[::-1]
    for i in b:
        print i,
    print '\n'
test_cases.close()
