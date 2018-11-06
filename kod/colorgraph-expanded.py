# -*- Coding:utf-8 -*-

# vrchol = ( cislo_vrcholu, seznam_sousedu, seznam_barev )
# graf = { v_1:sousedi_v1, v_2:sousedi_v2, ..., v_n:sousedi_vn }
def deg(v):
    return len(v[1])

def sat(v):
    return len(v[2])

def can_color( vertex, color ):
    if color in vertex[2]:
        return False
    return True

def choose(g):
    """ Odebere z grafu g vrchol, s nejvetsi
        saturovanosti a spolus grafem ho vrati
    """
    g_sorted = sorted(g,key=sat)
    v = g_sorted.pop()
    return (g_sorted,v)


def color(graf):
    # Setridi graf podle stupne
    g_sorted = sorted(graf.items(), key=deg)

    g = []
    g_dict = {}
    # Pridame seznam barev sousedu
    for v in g_sorted:
        nv = [v[1],[]]
        g.append( [v[0]]+nv )
        g_dict[v[0]] = nv

    coloring = {}

    # zde si uchovavame nejvetsi
    # dosud pouzitou barvu
    max_color = -1

    while( len(g) > 0 ):
        # Z grafu g odebereme vrchol s
        # nejvetsi saturovanosti
        (g,v) = choose(g)

        # Prochazime postupne barvy od
        # nejmensi do nejvetsi dosud pouzite
        for c in range(0,max_color+2):
            if can_color(v,c):
                coloring[v[0]]=c
                # projdeme sousedy vrcholu v
                # a u kazdeho si poznacime,
                # ze sousedi s c-barevnym vrcholem
                for s in v[1]:
                    if c not in g_dict[s][1]:
                        g_dict[s][1].append(c)
                # pokud jsme pouzili novou barvu,
                # zvetsime max_color
                if c > max_color:
                    max_color = c
                break
    return coloring

### Line 64 (Previous lines will be included in src-code listings)

###############################################
# Example graphs & TeX printing functions     #
###############################################

g = {
    1:[6,7,8],
    2:[5,7,8],
    3:[5,6,8],
    4:[5,6,7],
    5:[2,3,4],
    6:[1,3,4],
    7:[1,2,4],
    8:[1,2,3]
}
ga = {
    1:[2,6,8],
    2:[1,3,6,8],
    3:[2,4,8,6],
    4:[3,8,7],
    5:[],
    6:[3,2,1,7],
    7:[6,4,8],
    8:[7,4,3,2,1],
}

def print_colored(graf,coloring):
    colors = {
        0:'red',
        1:'blue',
        2:'green',
        3:'yellow',
        4:'white',
        5:'purple',
        6:'navy'
    }
    print r"""
\begin{center}
\begin{tikzpicture}[node distance=1cm]
          """
    for c in coloring.values():
        style = chr(ord('A')+c)
        print r"\tikzstyle{vertex%s}=[draw,circle,fill=%s"%(style,colors[c])

    for v in graf.keys():
        print r"\node [vertex%s,] (%s){%s};" % (chr(ord('A')+coloring[v]),
                                               chr(ord('A')+v),
                                               v)
    print r"""
\path[every node/.style={font=\sffamily\small}]
"""
    for (v,s) in graf.items():
        for n in s:
            print " (%s) edge node {} (%s) " % ( chr(ord('A')+v),
                                                 chr(ord('A')+n))
    print ";"
    print r"""
\end{tikzpicture}
\end{center}
"""

