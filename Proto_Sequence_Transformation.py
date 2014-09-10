import sys


def whol(l):
    num = []
    wrd = []

    dic = {}
    cnt = 1
    for items in l:
        l = items.split(" ")
        num = [l[0]]
        wrd = [l[1]]
    x = wrd, num
    perm(x)


def perm(i):
    nw = ''
    wrd = i[0]
    wrdc = wrd[0]

    cnt = -1
    cntn = -1
    num = i[1]
    a = 'A'
    b = 'B'
    nn = ''

    for chars in wrdc:
        cnt += 1

    while nn != wrd[0] and cntn <= cnt:

        for items in num[0]:

            if items == '1' and wrdc[cntn] != 'A' and cntn <= cnt:


                nn = nn + 'B'
                b = b + 'B'
                cntn += 1
            elif items == '0' and wrdc[cntn] == 'A' and cntn <= cnt:
                nn = nn + a
                cntn += 1

            if cntn == cnt and nn == wrdc[0]:
                print "Yes"
                return
            if cntn == cnt and nn != wrdc[0]:
                print "No"

                return


test_cases = open(sys.argv[1], 'r')
whol(test_cases)

test_cases.close()
