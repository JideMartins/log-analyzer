LEVELS = ["ERROR", "WARNING", "INFO"]


# create get_level function
def get_level(line):
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
def parse_line(line):
    """Turn one log line into a structured record contyaining its level and message"""
    line_spl = line.split(maxsplit=1)
    parsed_list = [item.strip() for item in line_spl]
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
print(parse_line("DEBUG Connection details"))
