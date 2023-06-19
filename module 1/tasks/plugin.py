def get_unique(lists):
    sm = 0
    for a in lists:
        sm = sm + int(a.pop())
    return sm
