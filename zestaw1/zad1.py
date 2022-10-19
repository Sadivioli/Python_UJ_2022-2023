def triangle(n):
    
    if (n%2 == 0):
        n -= 1;
    
    print("*"*n)

    for i in range(1, n//2, 1):
        print (" " * i + "*", end = "")
        print (" " * (n - i * 2 - 2), end = "")
        print ("*")

    print (" " * (n // 2) + "*\n")
    

print("Wprowadź długość podstawy: ")
n = int(input())
triangle(n)