#coding: utf-8
def gcdE_nre(n,m):
    if n > m:
        n,m = m,n
    z = m % n

    while not (z == 0):
      m = n
      n = z
      z = m % n

    return n
