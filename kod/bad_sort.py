def minGE( pole, lb = None ):
    i = 0
    if not lb is None:
        while( i<len(pole) and pole[i]<=lb ):
            i = i + 1
        if i == len(pole):
            return None
    min = pole[i]
    cnt = 1
    for j in range(i+1,len(pole)):
        if pole[j] < min:
            if lb is None or pole[j] > lb:
                cnt = 1
                min = pole[j]
        elif pole[j] == min:
            cnt = cnt + 1
    return (min, cnt)

def sort( pole ):
    (m, cnt) = minGE( pole )
    ret = [m] * cnt
    sz = len(pole)-cnt
    while( sz > 0 ):
        (m, cnt) = minGE( pole, m )
        ret = ret + [ m ] * cnt
        sz = sz - cnt
    return ret
