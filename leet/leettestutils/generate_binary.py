import random, argparse

parser = argparse.ArgumentParser(description="Will generate random binary string of given size")
parser.add_argument("size", type=int, help="Size of string to be generated")

args = parser.parse_args()


def generate_binary(sLength):
    return "".join([str(random.randint(0, 1)) for i in range(sLength)])


print(generate_binary(args.size))
