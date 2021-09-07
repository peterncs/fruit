#!/usr/bin/env python3

import os
import sys
import shutil
import socket
import psutil
import emails

def check_cpu_usage():
    #Check if CPU usage is over 80%
    usage = psutil.cpu_percent(1)
    if usage > 80:
        return True
    return False

def check_disk_full():
    #Check if available disk space is lower than 20%
    du = shutil.disk_usage("/")
    percent_free = du.free/du.total*100
    if percent_free < 20:
        return True
    return False

def check_memory_lack():
    #Check if available memory is less than 500MB
    free_memory = psutil.virtual_memory().available
    free_MB = free_memory/2**20
    if free_memory < 500:
        return True
    return False

def check_hostname():
    #Check if hostname "localhost" cannot be resolved to "127.0.0.1"
    ip = socket.gethostbyname("localhost")
    if ip != "127.0.0.1":
        return True
    return False

def main():
    checks=[
    (check_cpu_usage, "Error - CPU usage is over 80%"),
    (check_disk_full, "Error - Available disk space is less than 20%"),
    (check_memory_lack, "Error - Available memory is less than 500MB"),
    (check_hostname, "Error - localhost cannot be resolved to 127.0.0.1")
    ]
    for check, error_msg in checks:
        if check():
            sender = "automation@example.com"
            receiver = "{}@example.com".format(os.environ.get('USER'))"
            subject = error_msg
            body = "Please check your system and resolve the issue as soon as possible."
            message = emails.generate_error_report(sender, receiver, subject, body)
            emails.send(message)
            sys.exit(1)

    sys.exit(0)

main()
