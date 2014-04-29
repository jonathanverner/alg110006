def find(text, s):
    found=[]
    for tpos in range(len(text)):
          f = True
          for spos in range(len(s)):
                if not text[tpos+spos] == s[spos]:
                    f = False
                    break
          if f:
              found.append(tpos)
    return found