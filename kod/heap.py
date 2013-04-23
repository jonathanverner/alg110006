# -*- coding:utf-8 -*-

# Jednoduché funkce pro počítání pozic dětí a rodičů
def left_child_index(n):
  return 2*n + 1

def right_child_index(n):
  return 2*n + 2

def parent_index(n):
  return (n-1)/2

def last_index(halda):
  return len(halda)-1

# Projde stromem od uzlu s indexem index ke kořeni
# a zajistí, že hodnoty potomků jsou vždy
# menší než hodnoty rodičů
def check_up(halda, index):
  p = parent_index(index)
  if halda[p][1] < halda[index][1]:
    halda[p],halda[index] = halda[index],halda[p]
    check_up(halda,p)

# Podobně jako předchozí funkce, ale prochází
# od uzlu s indexem index naopak k listům
def check_down(halda, index):
  l,r = left_child_index(index), right_child_index(index)
  if halda[l][1] < halda[r][1]:
    c = r
  else:
    c = l
  if halda[index][1] < halda[c][1]:
    halda[index],halda[c] = halda[c],halda[index]
    check_down(halda, c)

# Zjistí největší prvek v haldě
def peek(halda):
  if len(halda) == 0:
    return None
  return halda[0]

# Přidá prvek do haldy
def push( halda, data, hodnota ):
  halda.append((data,hodnota))
  check_up(halda, last_index(halda))

# Odebere největší prvek z haldy
def pop( halda ):
  if len(halda) == 0:
    return None
  ret = peek(halda)
  halda[0] = halda[-1]
  del halda[-1]
  check_down(halda, 0)
  return ret
