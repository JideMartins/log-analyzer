LEVELS = ["ERROR", "WARNING", "INFO"]


# create get_level function
def get_level(line: str):
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
def parse_line(line: str):
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


def analyze_lines(lines: list):
    """Return a dictionary showing an integer occurence frequency of each level"""
    pass


# tests
