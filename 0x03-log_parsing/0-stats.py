#!/usr/bin/python3
'''
Write a script that reads stdin line by line and computes metrics:

Input format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
(if the format is not this one, the line must be skipped)
After every 10 lines and/or a keyboard interruption (CTRL + C), print these
statistics from the beginning:
Total file size: File size: <total size>
where <total size> is the sum of all previous <file size>
(see input format above)
Number of lines by status code:
possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
if a status code doesn’t appear or is not an integer, don’t print anything
for this status code
format: <status code>: <number>
status codes should be printed in ascending order
Warning: In this sample, you will have random value - it’s normal to not have
the same output as this one.
'''
from sys import stdin
import re
import signal

# Regular expression to match the input format
log_regex = re.compile(
    r'(\S+) - \[(.*?)\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)')

# Dictionary to store the count of each status code
status_code_counts = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

total_file_size = 0
line_count = 0


def print_stats():
    '''Function to print the statistics.'''
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")


def handle_interrupt(signal, frame):
    '''Function to handle keyboard interruption (CTRL + C).'''
    print_stats()
    exit(0)


# Register the signal handler for keyboard interruption
signal.signal(signal.SIGINT, handle_interrupt)

try:
    for line in stdin:
        match = log_regex.match(line)
        if match:
            status_code = match.group(3)
            file_size = int(match.group(4))

            total_file_size += file_size
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1

            line_count += 1

            if line_count % 10 == 0:
                print_stats()
except EOFError:
    pass
finally:
    print_stats()
