def left( node ):
    return 2*node+1

def right( node ):
    return 2*node+2

def parent( node ):
    return (node-1)/2

def isLeaf( heap, node ):
    return left(node) >= len(heap)

def isRoot( heap, node ):
    return node == 0

def isNode( heap, node ):
    return node < len(heap)

def minChild( heap, node ):
    l = left(node)
    r = right(node)

    if isNode(heap, r):
        lv = heap[l][0]
        rv = heap[r][0]
        if ( lv <= rv ):
            return l
        else:
            return r

    return l


def upheap( heap, node ):
    if isRoot(heap, node):
        return
    p = parent( node )
    pval = heap[p][0]
    nval = heap[node][0]
    if pval <= nval:
        return
    else:
        heap[p],heap[node] = heap[node],heap[p]
        upheap( heap, p )

def insert( heap, value, data ):
    sz = len(heap)
    heap.append( [value, data] )
    upheap( heap, sz )
    

def downheap( heap, node ):
    if isLeaf( heap, node ):
        return

    c = minChild( heap, node )
    nv = heap[node][0]
    cv = heap[c][0]
    if ( nv <= cv ):
        return
    else:
        heap[node],heap[c]=heap[c],heap[node]
        downheap( heap, c )
    
def pop( heap ):
    if len(heap) == 0:
        return None
    ret = heap[0]
    heap[0] = heap[-1]
    del heap[-1]
    downheap( heap, 0 )
    return ret

def height( heap ):
    from math import log, ceil
    return int(ceil(log(len(heap)+1,2)))

def printHeap( heap ):
    for level in range(0,height(heap)):
        printLevel( heap, level )

def getStrNode( heap, node ):
    if isLeaf( heap, node ):
        return str( heap[node] )

    l = left( node )
    children = getStrNode( heap, l )

    r = right( node )
    if isNode( heap, r ):
        children += " " + getStrNode( heap, r )

    return str( heap[node] ).center(len(children))

def printLevel( heap, level ):
    ret = " "
    for n in range(2**level-1,min(2**(level+1)-1,len(heap))):
        ret = ret + getStrNode( heap, n ) + " "
    print ret

        
def listInsert( l, value, data ):
    l.append( [value, data] )

def listPop( l ):
    if len(l) == 0:
        return None
    min_val = l[0][0]
    min_ind = 0
    
    for i in range( 1, len(l) ):
        if l[i][0] < min_val:
            min_val = l[i][0]
            min_ind = i

    v,d = l[min_ind]
    del l[min_ind]
    return v,d

    
def bench_list(prob_insert,ops=100000):
    l = []
    msize = 0
    sumsize = 0
    from random import uniform, randint, seed
    seed(0)
    for i in range(ops):
        r = uniform(0,1)
        if r <= prob_insert:
            listInsert(l, randint(0,100), 'DATA')
            lsize = len(l)
            if ( lsize > msize ):
                msize = lsize
            sumsize += lsize
        else:
            tmp = listPop(l)
            sumsize += len(l)
    del l
    print "Max size: ", msize, " Avg size: ", float(sumsize)/ops

def bench_heap(prob_insert,ops=100000):
    h = []
    msize = 0
    sumsize = 0
    from random import uniform, randint, seed
    seed(0)
    for i in range(ops):
        r = uniform(0,1)
        if r <= prob_insert:
            insert(h, randint(0,100), 'DATA')
            hsize = len(h)
            if ( hsize > msize ):
                msize = hsize
            sumsize += hsize
        else:
            tmp = pop(h)
            sumsize += len(h)
    del h
    print "Max size: ", msize, " Avg size: ", float(sumsize)/ops

        
        
