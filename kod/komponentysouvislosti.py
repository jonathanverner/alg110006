def komponenta(vrchol, graf):
    k = []
    prace = [vrchol]
    navstiveno = []
    while( len(prace) > 0):
        v = prace.pop()
        if not v in navstiveno:
            k.append(v)
            navstiveno.append(v)
            for w in graf[v]:
                if not w in navstiveno:
                    prace.append(w)
    return k