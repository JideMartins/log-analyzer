from argparse import ArgumentParser, Namespace
from manual_checks import analyze_file

# Create parser object
analyzer = ArgumentParser(description="Analyzes log files")

# Add path argument
analyzer.add_argument("path", type=str, help="File path", default="")

# parse argument(s)
args: Namespace = analyzer.parse_args()


def main():
    if args.path:
        for level, count in analyze_file(args.path).items():
            print(f"{level}: {count}")


if __name__ == "__main__":
    main()
