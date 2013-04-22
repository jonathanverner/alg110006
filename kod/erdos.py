# -*- coding: utf-8 -*-
from collections import deque
from timeit import Timer

class stack(list):
    def popleft(self):
        return self.pop()
    
G = { 'erdos':['shelah','hajnal','blass'],
      'shelah':['erdos','hajnal','blass','juhasz'],
      'hajnal':['erdos','juhasz','shelah'],
      'blass':['erdos','shelah','hajnal','hrusak'],
      'hrusak':['blass','juhasz','balcar'],
      'balcar':['hrusak'],
      'juhasz':['shelah','hajnal','hrusak']}

def erdos( e, graf, dtype = deque ):
    prace = dtype( [ e ] )
    ret = { e: 0 }
    while( len(prace) > 0 ):
        v = prace.popleft()
        e_num = ret[v]
        for s in graf[v]:
            if ( s in ret and ret[s] > e_num + 1 ) or ( s not in ret ):
                ret[s] = e_num+1
                prace.append(s)
    return ret
            

def cesty( start, graf, dtype = deque ):
    prace = dtype( [ (start,0,start) ] )
    prev = start
    navstiveno = {}
    while ( len(prace) > 0 ):
        v,l,prev = prace.popleft()
        if v in navstiveno:
            if navstiveno[v][0] > l:
                navstiveno[v][0] = l
                navstiveno[v][1] = prev
        else:
            navstiveno[v] = [l,prev]
            for s in graf[v]:
                prace.append((s,l+1,v))
    return navstiveno

def min_cesta( kam, cesty ):
    if kam not in cesty:
        return None
    ret=[kam]
    while( not cesty[kam][1] == kam ):
        kam = cesty[kam][1]
        ret.append(kam)
    return ret
        
            
                
        
    
    
