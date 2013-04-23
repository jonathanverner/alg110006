# coding: utf-8
def extract_key(start_cifra, end_cifra, klic):
    """Vrátí část klíče od start_cifra do end_cifra
       >>> extract_key(1,4,12345)
       234
       >>> extract_key(0,2,123445)
       45
    """
    return (klic % (10**end_cifra))/(10**start_cifra)

def var_buck_sort(seznam, scf, ecf):
    """ Provede bucket sort ale místo všech cifer klíče uvažuje pouze
        cifry od místa scf do místa ecf. Přihrádky mají velikost 1 tudíž
        odpadá krok třídění jednotlivých přihrádek."""

    # Nalezení nejmenšího a největšího prvku
    min = max = extract_key(scf,ecf,seznam[0])
    for p in seznam:
        k = extract_key(scf,ecf,p)
        if k > max: max = k
        elif k < min: min = k

    # Vyrobení přihrádek
    poc_prihradek = (max-min)+1
    prihradky = []
    for i in range(poc_prihradek):
        prihradky.append([])

    # Roztřídění do přihrádek
    for p in seznam:
        k = extract_key(scf,ecf,p)
        prih = (k-min)
        prihradky[prih].append(p)

    # "Slití" přihrádek zpátky do seznamu
    pos = 0
    for prih in prihradky:
        for p in prih:
            seznam[pos] = p
            pos += 1

from math import log, ceil
def radix_sort(seznam, d):
    mx = max(seznam)
    delka_klice = int(ceil(log(mx,10)))
    delka_casti = delka_klice/d
    ecf = delka_casti
    while ecf <= delka_klice:
        var_buck_sort(seznam, ecf-delka_casti, ecf)
        ecf += delka_casti
