def b_sort(seznam, m):
    # Nalezení nejmenšího a největšího prvku
    min = max = seznam[0]
    for p in seznam:
        if p > max: max = p
        elif p < min: min = p

    # Vyrobení přihrádek
    poc_prihradek = (max-min)/m
    prihradky = [[]]*poc_prihradek

    # Roztřídění do přihrádek
    for p in seznam:
        prih = (p-min)/m
        prihradky[prih].append(p)

    # Setřízení přihrádek
    for prih in prihradky:
        # Sort je nějaký vhodný klasický třídící
        # algoritmus, který setřídí zadané pole
        sort(prih) 

    # "Slití" přihrádek zpátky do seznamu
    pos = 0
    for prih in prihradky:
        for p in prih:
        seznam[pos] = p
        pos += 1