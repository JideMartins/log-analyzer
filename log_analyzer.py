# create get_level function
def get_level(line):

    levels = ["ERROR", "WARNING", "INFO"]
    line_list = line.split()
    
    # check for non-empty list
    if line_list:
        if line_list[0] in levels:
            return line_list[0]
    return None

# tests
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