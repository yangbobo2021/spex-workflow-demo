"""A tiny integer-addition CLI for SPEX workflow practice."""

import argparse


def main():
    parser = argparse.ArgumentParser(description="Add two integers.")
    parser.add_argument("a", type=int, help="first integer")
    parser.add_argument("b", type=int, help="second integer")
    args = parser.parse_args()
    print(args.a + args.b)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
