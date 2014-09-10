import sys
import collections
import time

start_time = time.clock()


def far(s1, s2):
    if len(s1) < len(s2):
        return far(s2, s1)
    if len(s2) == 0:
        return len(s1)
    prior = xrange(len(s2) + 1)
    for i, c1 in enumerate(s1):
        now = [i + 1]
        for j, c2 in enumerate(s2):
            dna_append = (prior[j + 1] + 1)
            dna_remove = (now[j] + 1)
            dna_pop = (prior[j] + (c1 != c2))
            now.append(min(dna_append, dna_remove, dna_pop))
        prior = now
        # print prior
    return prior[-1]


def confirm(dna_trans1, dna_trans0, dna_incr):
    dna_conf = collections.defaultdict(list)

    for i in xrange(len(dna_trans0)):
        seg = dna_trans0[i:i + len(dna_trans1)]
        if len(seg) != len(dna_trans1):
            break
        trans_error = far(dna_trans1, seg)
        if trans_error <= dna_incr:
            dna_conf[trans_error].append(seg)
    return dna_conf


def main():
    test_cases = open(sys.argv[1], 'r')
    # test_cases[
    # 'CCC 1 CGCCCGAATCCAG',
    # 'GCGAG 2 CCACGGCCTATGTATTTGCAAGGATCTGGGCCAGCTAAATCAGCACCCCTGGAACGGCAAGGTTCATTTT         GTTGCGCGCATAG',
    #     'CGGCGCC 1 ACCCCCGCAGCCATATGTCCCCAGCTATTTAATGAGGGCCCCGAACACGGGGAGTCTTACACGATCTG         CCCTGGAATCGC']
    for test in test_cases:
        test = test.strip()
        if len(test) == 0:
            continue
        dna_trans1 = test.split(' ')[0]
        dna_trans0 = test.split(' ')[2]
        dna_incr = int(test.split(' ')[1])
        dna_conf = confirm(dna_trans1, dna_trans0, dna_incr)

        if len(dna_conf) > 0:
            list_0 = []
            for trans_error in sorted(dna_conf.keys()):
                for seg in sorted(dna_conf[trans_error]):
                    list_0.append(seg)
            print " ".join(list_0)
        else:
            print 'No match'
    tt = start_time - time.clock()
    # print tt
    test_cases.close()


if __name__ == '__main__':
    main()
