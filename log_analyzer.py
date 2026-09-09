from pathlib import Path
cwd = str(Path.cwd())

def log_reader(log_path):
    try:
        with open(file=log_path, mode="r") as file:
            content = file.read()
            return content

    except FileNotFoundError:
        print("No log was found")


log_content = log_reader(cwd + "\sample_logs\sample1.log")
info_message = log_content.count("INFO")
warning_message = log_content.count("WARNING")
error_message = log_content.count("ERROR")
total_entries = info_message + warning_message + error_message
log_entries = set(log_content.split("\n"))

print(f"{"=" * 5} Log Entries {"=" * 5}\n")
print(f"Total entries: {total_entries}")
print(f"INFO: {info_message}")
print(f"WARNING: {warning_message}")
print(f"ERRORS: {error_message}")
print(f"Error average {int(error_message/total_entries*100)}%")
print(f"\n{"=" * 25}\n")

print(f"{"="*6} ERRORS {"="*6}")
for entry in log_entries:
    if "ERROR" in entry:
        print(entry)