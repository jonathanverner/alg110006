# coding: utf-8
# Očíslování posloupností délky 2
# (uvažujeme pouze řetězce ze znaků 'a' a 'b')
seqnum = {
  'aa':0,
  'ab':1,
  'bb':2,
  'ba':3
}

# Tabulka odpovídající hledání
# řetězce 'aab'
tabulka = {
  (0,'a'):(False,0),
  (0,'b'):(True,1),
  (1,'a'):(False,3),
  (1,'b'):(False,2),
  (2,'a'):(False,3),
  (2,'b'):(False,2),
  (3,'a'):(False,0),
  (3,'b'):(False,1)
}

def smartfind(text, tabulka, lens):
    """ text    ... řetězec, ve kterém se vyhledává
        tabulka ... vyhledávací tabulka
        lens    ... délka hledaného řetězce """
    found = []
    # přečti prvních lens znaků a zjisti číslo této 
    # posloupnosti
    np = seqnum[text[:lens-1]]
    
    for tpos in range(lens,len(text)):
        # dle tabulky urči, zda následující znak (text[tpos])
        # zakončuje hledanou posloupnost a zároveň
        # aktualizuj číslo posloupnosti np
        f, np = tabulka[(np,text[tpos])]
        if f:
            found.append(tpos-lens+1)
    return found
            