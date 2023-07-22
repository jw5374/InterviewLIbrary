import random, argparse

parser = argparse.ArgumentParser(description="Will generate list of random ints of given size and upper/lower bounds")
parser.add_argument("lower", type=int, help="Lower bound for generated integers")
parser.add_argument("upper", type=int, help="Upper bound for generated integers")
parser.add_argument("size", type=int, help="Size of list to be generated")
parser.add_argument("-dis", "--distinct", action="store_true")

args = parser.parse_args()


def generateArray(lower: int, upper: int, size: int) -> list[int]:
    res = []
    for i in range(size):
        res.append(random.randint(lower, upper))
    return res


def generateDistinct(lower: int, upper: int, size: int) -> list[int]:
    res = set()
    while len(res) < size:
        res.add(random.randint(lower, upper))
    return list(res)


if args.distinct:
    print(generateDistinct(args.lower, args.upper, args.size))
else:
    print(generateArray(args.lower, args.upper, args.size))

