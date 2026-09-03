import json
import random

log_levels = ["INFO", "WARNING", "ERROR"]

messages = {
    "INFO": [
        "Server started successfully",
        "User logged in",
        "Database connection established",
        "Backup completed",
        "User logged out"
    ],
    "WARNING": [
        "High memory usage",
        "CPU usage above threshold",
        "Disk space running low",
        "Slow database response"
    ],
    "ERROR": [
        "Database connection failed",
        "File not found",
        "Authentication failed",
        "Request timed out",
        "Service unavailable"
    ]
}

file_path = "python_projects\Log-Analyzer\sample_logs\sample.log"


try:
    with open(file= file_path, mode="w") as file:
        for i in range(50):
            log_level_random = random.choice(log_levels)
            log_message = random.choice(messages[log_level_random])
            file.write(log_message+"\n")
        #json.dump(messages, file, indent=4)
        print(f"log file {file_path} was created!")
except FileNotFoundError:
    print("File was not found")