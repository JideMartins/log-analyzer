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
    """Turn one log line into a structured record contyaining its level and message"""
    
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


# tests
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


# get_level regression tests
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
