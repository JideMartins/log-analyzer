# create get_level function
def get_level(line):
    """Identifies the severity of log at the beginning of the line
    Args:
        line (str): _description_
    Returns:
        str: Returns "ERROR", "WARNING" or "INFO"
        None: Returns None if the log doesn't have any severity
    """

    levels = ["ERROR", "WARNING", "INFO"]
    line_list = line.split()

    # check for non-empty list
    if line_list:
        if line_list[0] in levels:
            return line_list[0]
    return None

# line parser
def parse_line(line):
    """Turn one log line into a structured record contyaining its level and message
    """
    pass

# tests

