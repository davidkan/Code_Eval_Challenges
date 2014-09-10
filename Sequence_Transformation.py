import sys


def boolit(perm, seq):
    if perm == '0':
        return 'B' not in seq
    if perm == '1':
        a = 'A' in seq
        b = 'B' in seq
        return not (a and b)


def check_seqing(perm, seq, seqing_list, row=0, col=0):
    if seqing_list[-1][-1]:
        return

    if row >= len(seqing_list) or col >= len(seqing_list[row]):
        return

    if seqing_list[row][col]:
        return
    for c in xrange(col, len(seq)):

        seqing_list[row][c] = False

        if boolit(perm[row], seq[col:c + 1]):
            seqing_list[row][c] = True

            check_seqing(perm, seq, seqing_list, row + 1, c + 1)


def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        perm, seq = test.strip().split(' ')
        lm, lp = len(seq), len(perm)
        seqing_list = [[None for m in xrange(lm)] for p in xrange(lp)]
        check_seqing(perm, seq, seqing_list)
        print 'Yes' if seqing_list[-1][-1] else 'No'
    test_cases.close()


if __name__ == '__main__':
    main()
