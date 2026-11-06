from log_analyzer import (
    get_level,
    parse_line,
    analyze_lines,
    analyze_file,
    filter_lines,
)

# tests-1
# print("=====================Test 1=====================")
# print(get_level("INFO Application started"))
# print(get_level("WARNING Disk space low"))
# print(get_level("ERROR Database connection failed"))
# print(get_level("  ERROR Connection refused  "))
# print(get_level("\tINFO\tService ready\n"))
# print(get_level("ERROR"))
# print(get_level(""))
# print(get_level("   \t\n"))
# print(get_level("error Connection refused"))
# print(get_level("DEBUG Connection details"))
# print(get_level("INFO Previous ERROR resolved"))
# print(get_level("ERRORS occurred"))
# print()

# # tests-2
# print("=====================Test 2=====================")
# print(parse_line("INFO Application started"))
# print(parse_line("  ERROR Connection refused  "))
# print(parse_line("WARNING Disk  space low"))
# print(parse_line("\tINFO\tService ready\n"))
# print(parse_line("ERROR"))
# print(parse_line("ERROR   \t"))
# print(parse_line(""))
# print(parse_line("   \t\n"))
# print(parse_line("error Connection refused"))
# print(parse_line("ERRORS occurred"))
# print(parse_line("INFO Previous ERROR resolved"))
# print(parse_line("INFO Service\tready"))
# print()

# # tests 3
# print("=====================Test 3=====================")
# log1 = [
#     "INFO Application started",
#     "ERROR Database connection failed",
#     "WARNING Disk space low",
#     "INFO Application stopped",
#     "ERROR",
#     "",
#     "DEBUG Connection details",
# ]


# print(analyze_lines(log1))
# print(analyze_lines(log1))  # Calling it twice to test for consistent results
# print(analyze_lines([]))
# print(analyze_lines(["ERROR Failed", "ERROR Failed"]))
# print(analyze_lines(["ERROR", "error Failed", "   \t", "DEBUG Details"]))
# print(analyze_lines(["INFO Previous ERROR resolved", "\tWARNING\tDisk  space low\n"]))

# # tests 4
# print("=====================Test 4=====================")
# print(analyze_file("logs/sample.log"))
# print(analyze_file("logs/sample.log"))
# print(analyze_file("logs/empty.log"))
# print(analyze_file("logs/blank.log"))
# print(analyze_file("logs/single.log"))
# print(analyze_file("logs/unicode.log"))
# print(analyze_file("logs/non-existent.log"))


# test-7
print("=====================Test 7=====================")
print(
    filter_lines(
        [
            "ERROR First failure",
            "INFO Ready",
            "ERROR",
            "  ERROR Second  failure  ",
            "ERROR First failure",
            "error Lowercase entry",
        ],
        "ERROR",
    )
)
