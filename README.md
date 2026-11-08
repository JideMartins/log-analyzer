# Log Analyzer
A Python command-line tool for triaging plain-text application logs. Get a quick count of errors, warnings, and informational entries, or print just the messages for the severity you’re investigating.

## Quick start
Use Python 3.10 or later. The project uses only the Python standard library, so there are no packages to install. Run the commands from the directory containing `log_analyzer.py`. On Windows, use `py` in place of `python3` if you use the Python launcher.

Save the following text as `sample.log` in that directory using UTF-8.

```text
INFO Application started
WARNING Disk space low
ERROR Database connection failed
ERROR
INFO Retry scheduled
ERROR Request timed out
```

### Summarize a log file
```bash
python3 log_analyzer.py sample.log # sample.log or dir/to/sample.log
```
```text
INFO: 2
WARNING: 1
ERROR: 2
malformed: 1
```
The summary always includes all three levels, even when a level has zero entries. The bare `ERROR` line counts as malformed because it has no message.

### Filter by severity
```bash
python3 log_analyzer.py sample.log --level ERROR
```

```text
ERROR Database connection failed
ERROR Request timed out
```

Use `-l` as a shorthand for `--level`. Filtering skips malformed lines and prints matches in file order, including duplicates. A filter with zero matches produces empty output and exits successfully.

## Input Format
Each UTF-8 log entry occupies one line and begins with `INFO`, `WARNING`, or `ERROR`, followed by whitespace and a message. Levels are case-sensitive. The parser trims surrounding whitespace and preserves spaces and tabs inside the message.

Blank lines, unknown or lowercase levels, and lines with a missing message count as malformed. Timestamp-prefixed entries also count as malformed because the first token must be a supported level.

## Command reference
```text
python3 log_analyzer.py [-l {INFO,WARNING,ERROR}] path
python3 log_analyzer.py --help
```

The `path` argument takes a relative or absolute path to a log file. Quote paths that contain spaces, for example `python3 log_analyzer.py "logs/sample copy.log"`.


| Exit code | Meaning                                                                                                       |
| --------- | ------------------------------------------------------------------------------------------------------------- |
| `0`       | The command completed successfully, including help, logs with malformed lines, and filters with zero matches. |
| `1`       | The path points to a directory, the file is missing, or a file access error occurred.                         |
| `2`       | The CLI arguments were invalid, such as an unsupported level or a missing path.                               |

Both summary and filter mode reject directory paths. If you pass `logs/` instead of `logs/sample.log`, the CLI reports that the path is a directory on standard error and exits with code `1`.

## Tests and project files

From the directory containing the Python files, run the automated suite with `unittest`.

```bash
python3 -m unittest -v
# or
python -m unittest -v test_log_analyzer.py 
```

| File                                           | Purpose                                                                                                                                                                                                                   |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`log_analyzer.py`](log_analyzer.py)           | Parses log entries, summarizes or filters files, and handles command-line arguments with `argparse`.                                                                                                                      |
| [`test_log_analyzer.py`](test_log_analyzer.py) | Tests parsing and file handling, and runs the CLI in subprocesses to check output, errors, and exit codes. It creates its own temporary log files.                                                                        |
| [`manual_checks.py`](manual_checks.py)         | Prints exploratory checks. To run it, first supply `sample.log`, `empty.log`, `blank.log`, `single.log`, and `unicode.log` inside `logs/`, then run `python3 manual_checks.py` from the directory containing the scripts. |
