def dijkstra( start, cil, graf ):
    """ Funkce dijkstra dostane na vstupu startovni a koncovy vrchol
        (start,cil) a graf, který je reprezentován jako modifikovaný
        seznam sousedů: k sousedům si navíc pamatujeme délky hran, t.j.
        například graf odpovídající obdélníku s hranami délky 2 a 4
        by byl reprezentován takto:

        >>> g = [ [(1,4),(3,2)],
                  [(0,4),(2,2)],
                  [(1,2),(3,4)],
                  [(0,2),(2,4)] ]

        Vrátí nejkratší cestu z vrcholu start do vrcholu cil jako
        posloupnost vrcholu, pokud existuje, jinak vrati None.

        >>> dijkstra(0,2,g)
        [0,1,2]
    """

    # Zde si ukládáme informace o tom, které
    # vrcholy jsme již navštívili
    navstiveno = [False] * len(graf)

    # Zde si ukládáme informace o délkách nejkratších
    # dosud nalezených cest. Na začátku neznáme žádnou
    # cestu mimo cestu ze start do start. Délky jsou tedy
    # nekonečné.
    cesty = [(float('inf'),start)]*len(graf)
    cesty[start]=(0,start)

    v = start
    delka_do_v = 0
    while v is not None:
        navstiveno[v] = True
        for (u,delka_vu) in graf[v]:
            # Pokud je cesta do u přes vrchol v
            # kratší, než dosud nejlepší nalezená
            # cesta do u, musíme upravit cesty
            if cesty[u][0] > delka_do_v+delka_vu:
                cesty[u]=(delka_do_v+delka_vu,v)

        # Vyber z nenavštívený vrcholů ten vrchol, do kterého
        # z vrcholu start vede dosud nejkratší nalezená cesta.
        delka_do_v, v = min([
            (d,u) for (u,(d,prev)) in enumerate(cesty) if not navstiveno[u]
        ])

        # Pokud každý z nenavštívených vrcholů má nejlepší cestu
        # nekonečně dlouhou, pak to znamená, že do žádného nich
        # nevede cesta. Protože vrchol cil je jednim z nich, vrátíme None
        if delka_do_v == float('inf'):
            return None

        if v == cil:
            # Zrekonstruujeme nejkratší cestu z údajů uložených
            # v seznamu cesty a vrátíme ji
            return postav_cestu(cesty,v)

def postav_cestu(cesty, v):
    current = v
    cesta = []
    while True:
        cesta.append(current)
        delka, prev = cesty[current]
        if prev == current:
            cesta.reverse()
            return cesta
        current = prev

