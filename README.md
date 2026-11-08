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
