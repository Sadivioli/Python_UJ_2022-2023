import sys

args = sys.argv[1:]

#zakładamy że przy wywolaniu podanie zostaną argumenty w postaci: szerokość, wysokość
def main(args):
    #zaczynamy obrazek od jednego "+"
    canvas = "\n+"
    for i in range(int(args[0])):
        canvas += "---+"
    
    for j in range(int(args[1])):
        evenRow = "\n|"
        oddRow = "\n+"
        for k in range(int(args[0])):
            evenRow += "   |"
            oddRow += "---+"
        canvas += evenRow + oddRow
    print(canvas)
main(args)