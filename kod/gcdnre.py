#coding: utf-8
def gcdE_nre(n,m):
    if n > m:
        n,m = m,n
    d = m % n

    while not (d == 0):
      m = n
      n = d
      d = m % n

    return n
