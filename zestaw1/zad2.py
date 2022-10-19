import sys

args = sys.argv[1:]

def main(args):
    for i in range(len(args)):
        num = args[i]
        print(num, " = ", end="")

        p = 2
        numInt = int(num)
        while numInt > p*p :
            primeOccurences = 0
            while numInt % p == 0:
                primeOccurences += 1
                numInt /= p

            if(primeOccurences > 0):
                print(p, "^", primeOccurences, " * ", end="")
            p += 1

        print(numInt)

main(args)
