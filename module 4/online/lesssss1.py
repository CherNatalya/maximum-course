# O (N ** 2)
'''def str_counter(s):
    for sym in set(s):
        count = 0
        for sub_sym in s:
            if sym == sub_sym:
                count += 1
        print(f'{sym} - {count}')'''


# O (N)
'''def str_counter(s):
    for sym in set(s):
        print(f'{sym} - {s.count(sym)}')'''


# O (2 * N)
def str_counter(s):
    sym_dict = {}
    for sym in s:
        sym_dict[sym] = sym_dict.get(sym, 0) + 1
    for sym, count in sym_dict.items():
        print(f'{sym} - {count}')


str_counter('aaaaaaaaaaaaaa')
