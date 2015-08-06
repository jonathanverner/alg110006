# coding: utf-8

def build_automaton(retezec):
    """ Vrátí automat rozpoznávající řetězec retezec.
        
        Funkce ve skutečnosti vrátí seznam stavů, kde stav stav s indexem 0 je počáteční 
        a stav poslední stav je koncovým stavem. Každý stav je seznamem šipek, které z 
        něj vedou, t.j. dvojice (znak, index_následujícího_stavu_pro_daný_znak)
    """
    c_state_num = 0                # index aktuálně vytvářeného stavu
    help_state = []                # pomocný stav pro podřetězec r[1:]
    c_state = []                   # aktuálně vytvářený stav 
    A = [None]*(len(retezec)+1)    # Inicializujeme automat
    for c in retezec:
        A[c_state_num] = c_state
              
        # Přidáme dopřednou šipku do aktuálního stavu
        c_state.append((c,c_state_num+1))
        
        # Přidáme zpětné šipky, t.j. zkopírujeme šipky z pomocného stavu do aktuálního stavu.
        # Pokud z pomocného stavu vede šipka označená znakem c pak příslušně aktualizujeme 
        # pomocný stav, jinak nastavíme pomocný stav na 0
        next_help_state = A[0]
        for sipka in help_state:
            char, target_state_num = sipka
            if char == c:
                next_help_state = A[target_state_num]
            else:
                c_state.append((char,target_state_num))
        
        help_state = next_help_state
        c_state_num += 1
        c_state = []
    
    # Přidáme koncový stav
    for sipka in help_state:
        char, target_state_num = sipka
        c_state.append((char,target_state_num))
    A[-1]=c_state
    return A
    
def optimalfind(text, s):
    A = build_automaton(s)
    c_state = A[0]             # aktuální stav nastavíme na počáteční stav automatu
    found_state_num = len(A)-1 # index koncového stavu
    found = []                 # seznam výskytů
    
    # Protože výskyt řetězce s na pozici p najdeme teprve když přečteme znak
    # na pozici p+len(s), musíme len(s) odečíst
    pos = -len(s)
    
    for c in text:
        pos = pos+1
        # Najdi šipku odpovídající načtenému písmenu. Pokud taková je, přesuň se do odpovídajícího
        # stavu, jinak se přesuň do počátečního stavu
        move_to_zero = True
        for sipka in c_state:
            char, target_state_num = sipka
            if char == c:
                # pokud jsme v koncovém stavu, máme výskyt
                if target_state_num == found_state_num:
                    found.append(pos)
                c_state = A[target_state_num]
                move_to_zero = False
                break
        if move_to_zero:
            c_state = A[0]        
    return found