def prohod(seznam, pos):
    seznam[pos+1],seznam[pos]=seznam[pos],seznam[pos+1]

def bubble(seznam):
    prohozeno = False
    last_prohod=1
    mez = len(seznam)
    while mez > 1:
        for i in range(last_prohod-1,mez-1):
            if (seznam[i] > seznam[i+1]):
                if not prohozeno:
                    last_prohod = i
                prohozeno = True
                prohod( seznam, i )
        if not prohozeno:
            return
        mez = mez - 1

def mingeq(seznam, dolni_mez):
    nsez = filter((lambda x: x > dolni_mez), seznam)
    for s in seznam:
        if s > dolni_mez and s < mn:
            mn = dolni_mez
    return mn

                
