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
    # create initial dictionary
    severity_set = set(LEVELS)
    result = {item: 0 for item in severity_set}
    result["malformed"] = 0

    for line in lines:
        line_dict = parse_line(line)

        # Using this condition as other conditions won't allow the .keys() usage
        if line_dict is not None:
            level = list(line_dict.values())[0]  # get first element of the list
            result[level] += 1
        else:
            result["malformed"] += 1

    return result


# tests-1
print("=====================Test stage 1=====================")
print(get_level("INFO Application started"))
print(get_level("WARNING Disk space low"))
print(get_level("ERROR Database connection failed"))
print(get_level("  ERROR Connection refused  "))
print(get_level("\tINFO\tService ready\n"))
print(get_level("ERROR"))
print(get_level(""))
print(get_level("   \t\n"))
print(get_level("error Connection refused"))
print(get_level("DEBUG Connection details"))
print(get_level("INFO Previous ERROR resolved"))
print(get_level("ERRORS occurred"))
print()

# tests-2
print("=====================Test stage 2=====================")
print(parse_line("INFO Application started"))
print(parse_line("  ERROR Connection refused  "))
print(parse_line("WARNING Disk  space low"))
print(parse_line("\tINFO\tService ready\n"))
print(parse_line("ERROR"))
print(parse_line("ERROR   \t"))
print(parse_line(""))
print(parse_line("   \t\n"))
print(parse_line("error Connection refused"))
print(parse_line("ERRORS occurred"))
print(parse_line("INFO Previous ERROR resolved"))
print(parse_line("INFO Service\tready"))
print()

# tests 3
print("=====================Test stage 3=====================")
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
print(analyze_lines(log1))  # Calling it twice to test for consistent results
print(analyze_lines([]))
print(analyze_lines(["ERROR Failed", "ERROR Failed"]))
print(analyze_lines(["ERROR", "error Failed", "   \t", "DEBUG Details"]))
print(analyze_lines(["INFO Previous ERROR resolved", "\tWARNING\tDisk  space low\n"]))
