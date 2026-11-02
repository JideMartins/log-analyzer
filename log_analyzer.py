# create get_level function
def get_level(line):

    levels = ["ERROR", "WARNING", "INFO"]
    line_list = line.split()
    if line_list[0] in levels:
        return line_list[0]
    return None
