def fun(N):
    
    binarny = bin(int(N))

    
    binary_break = 0
    binary_break_max = 0
    for i in range(2, len(binarny)):
        if binarny[i] == '0':
            binary_break += 1
        else:
            if binary_break > binary_break_max:
                binary_break_max = binary_break
            binary_break = 0
    return binary_break_max
    
print(fun(input("Podaj liczbę: ")), " - rozmiar największej przerwy binarnej")