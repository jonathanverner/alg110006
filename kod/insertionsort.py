def insertion_sort(seznam):
    last_sorted = 0
    while last_sorted < len(seznam)-1:
        j = last_sorted + 1
        while j > 0 and seznam[j] < seznam[j-1]:
            seznam[j-1],seznam[j] = seznam[j], seznam[j-1]
            j = j - 1
        last_sorted = last_sorted + 1