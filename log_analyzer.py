LEVELS = ["ERROR", "WARNING", "INFO"]


# define helper function for cleaning up lines
def clean_up(line):
    lines_list = [item.strip() for item in line.split(maxsplit=1)]
    return lines_list


# define helper function that creates a list of list for lines of logs
def severity(lst):
    new_list = []
    for line in lst:
        sev_list = clean_up(line)
        new_list.append(sev_list)
    return new_list


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
    # create initial dictionary
    logs_list = severity(lines)

    severity_set = set(LEVELS)

    # set values to 0
    result = {item: 0 for item in severity_set}
    result["malformed"] = 0

    for sublist in logs_list:
        if sublist and len(sublist) > 1 and sublist[0] in result:
            result[sublist[0]] += 1
        else:
            result["malformed"] += 1

    return result


# tests
log1 = [
    "INFO Application started",
    "ERROR Database connection failed",
    "WARNING Disk space low",
    "INFO Application stopped",
    "ERROR",
    "",
    "DEBUG Connection details",
]


print(analyze_lines(log1))
print(analyze_lines(log1)) # Calling it twice to test for consistent results
print(analyze_lines([]))
print(analyze_lines(["ERROR Failed", "ERROR Failed"]))
print(analyze_lines(["ERROR", "error Failed", "   \t", "DEBUG Details"]))
print(analyze_lines(["INFO Previous ERROR resolved", "\tWARNING\tDisk  space low\n"]))
