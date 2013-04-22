def l(u):
    return 2*u + 1

def p(u):
    return 2*u + 2

def o(u):
    return (u-1)/2

def isList( halda, u ):
    return l(u) >= len(halda)

def append( halda, elem, value ):
    halda.append( (elem,value) )
    u = len(halda)-1
    while( u > 0 ):
        if ( halda[o(u)][1] < halda[u][1] ):
            return
        halda[o(u)],halda[u] = halda[u],halda[o(u)]
        u = o(u)

def pop( halda ):
    ret = halda[0]
    halda[0] = halda[-1]
    del halda[-1]
    u = 0
    while( not isList(halda, u) ):
        if ( p(u) >= len(halda) ):
            v = l(u)
        else:
            if ( halda[l(u)][1] <= halda[p(u)][1] ):
                v = l(u)
            else:
                v = p(u)
        if halda[u][1] <= halda[v][1]:
            return ret
        halda[u],halda[v] = halda[v],halda[u]
        u = v
    return ret

def compute_cesta( start, cil, cesty ):
    if not cil in cesty:
        return None
    cesta = []
    while( not cil == start ):
        cesta.append(cil)
        cil = cesty[cil][0]
    cesta.append(start)
    return cesta

def min_cesta( start, cil, G ):
    cesty = {}
    prace = []
    append(prace, (start,start), 0 )
    while( len(prace) > 0 ):
        ((v,odkud),l) = pop( prace )
        if v in cesty:
            continue
        cesty[v] = ( odkud, l )
        if ( v == cil ):
            return compute_cesta( start, cil, cesty )
        for (s,d) in G[v]:
            if s in cesty:
                continue
            else:
                append( prace, (s,v), d+l )
    return compute_cesta( start, cil, cesty )

G = { 'a':[('b',10),('c',20)],
      'b':[('a',10),('c',5),('d',20)],
      'c':[('a',20),('e',10),('f',10)],
      'd':[('b',20),('f',5)],
      'e':[('c',10)],
      'f':[('c',10),('d',5)] }


from collections import deque
def erdos( e, graf ):
    prace = deque( [ (e,e,0) ] )
    cisla = {}
    while( len(prace) > 0 ):
        (prev, cur, num) = prace.popleft()
        if cur not in cisla:
            cisla[cur]=(prev,num)
            for (s,l) in graf[cur]:
                if s not in cisla:
                    prace.append( (cur,s,num+1) )
    return cisla
 
def cesta(e, v, cisla):
    ret = []
    if v not in cisla:
        return None
    while( not v == e ):
        ret.append(v)
        v = cisla[v][0]
    ret.append(v)
    return ret


