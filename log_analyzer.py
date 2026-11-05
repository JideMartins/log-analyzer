from argparse import ArgumentParser, Namespace
import sys

LEVELS = ["INFO", "WARNING", "ERROR"]


# create get_level function
def get_level(line: str) -> str | None:
    """Identifies the severity of log at the beginning of the line
    Args:
        line (str): _description_
    Returns:
        str: Returns "ERROR", "WARNING" or "INFO"
        None: Returns None if the log doesn't have any severity
    """
    line_list = line.split()

    # check for non-empty list
    if line_list:
        if line_list[0] in LEVELS:
            return line_list[0]
    return None


# line parser
def parse_line(line: str) -> dict | None:
    """Turn one log line into a structured record containing its level and message
    Args:
        line (str)
    Returns:
        dict: key=level, value=level message - if it has ERROR, INFO or WARNING along with its message
        None: if arg has none of the levels or the levels without message
    """

    # split line and strip it of trailing and ending spaces, newlines and tabs
    parsed_list = [item.strip() for item in line.split(maxsplit=1)]

    # check for non-empty lists and lists with message
    if parsed_list and len(parsed_list) > 1:
        if parsed_list[0] in LEVELS:
            return dict(
                level=parsed_list[0],
                message=parsed_list[1],
            )
    return None


def analyze_lines(lines: list) -> dict:
    """Analyzes a list of raw log lines and counts occurrences of each severity level.
    Iterates through raw log text entries, parses them, and accumulates the frequency
    of known severity levels. If a log line fails validation or cannot be parsed
    successfully, it is tracked as a malformed entry.

    Args:
        lines (list): A list of raw string log lines to be parsed and analyzed.

    Returns:
        dict: A mapping of severity levels (plus a 'malformed' counter) to their
        respective integer frequency counts. Example:
        {'INFO': 15, 'ERROR': 2, 'malformed': 1}
    """
    # create initial dictionary
    # severity_set = set(LEVELS) # set creates inconsistent format
    result = {item: 0 for item in LEVELS}
    result["malformed"] = 0

    for line in lines:
        line_dict = parse_line(line)

        # Check guard
        if line_dict is not None:
            level = line_dict["level"]  # get level of log line
            result[level] += 1
        else:
            result["malformed"] += 1

    return result


def analyze_file(path: str) -> dict:
    """Analyze logs saved locally.
    Args:
        path (str): The local file path to the log file.
    Returns:
        dict: A breakdown of the analyzed log data.
    Raises:
        FileNotFoundError: If the log file does not exist at the specified path.
    """
    try:
        # Read local file
        with open(path, "r", encoding="utf-8") as log:
            log_lines_list = log.readlines()
        # file closed
    except FileNotFoundError:
        raise

    # use lines
    return analyze_lines(log_lines_list)


# Create parser object
analyzer = ArgumentParser(description="Analyzes log files")

# Add path argument
analyzer.add_argument("path", type=str, help="File path")

# The main event
def main():
    """Parses command-line arguments and prints log analysis results.
    """
    # parse argument(s)
    args: Namespace = analyzer.parse_args()
    try:
        if args.path:
            for level, count in analyze_file(args.path).items():
                print(f"{level}: {count}")
    except FileNotFoundError:
        # handle missing files
        print(
            f"Error: cannot read '{args.path}': No such file or directory",
            file=sys.stderr,
        )
        sys.exit(1)

    except PermissionError:
        # handle file access without required permissions
        print(
            f"Error: Permission denied when accessing'{args.path}': Check permissions",
            file=sys.stderr,
        )
        sys.exit(1)

    except IsADirectoryError:
        # handles directories
        print(
            f"Error: file path: '{args.path}' is a directory and not a file",
            file=sys.stderr,
        )
        sys.exit(1)

    except OSError as e:
        # Catch other system and OS-level file issues
        print(
            f"Error: '{args.path}': An unexpected OS error occcured: {e}",
            file=sys.stderr,
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
