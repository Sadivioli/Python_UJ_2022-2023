import sys

args = sys.argv[1:]

def main(args):
    div = " |"
    val = "0"
    lenght = int(args[0])
    for i in range(1, lenght + 1):
        div += "....|"
        val += str(i).rjust(5)

    print(div, "\n", val)

main(args)