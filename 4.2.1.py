"""def strcounter(s):
    for sym in set(s) :
        counter = 0
        for sub_sym in s:
            if sym == sub_sym:
                counter += 1
        print(sym, counter)
strcounter('abcdaa')"""


def strcounter(s):
    syms_counter = {}
    for sym in s:
        syms_counter[sym] = syms_counter.get(sym, 0) + 1
print('Излачлоаи')