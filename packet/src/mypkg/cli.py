import argparse
from .core import hello

def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("-n", "--name", default="world")
    args = p.parse_args()
    print(hello(args.name))
