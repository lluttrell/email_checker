import csv
import sys
from validate_email import validate_email

with open(sys.argv[1], newline='') as myFile:
    reader = csv.reader(myFile)
    emails = []
    for row in reader:
        emails.append(row[2])

print(emails)

valid = []
invalid = []
for email in emails:
    is_valid = validate_email(email,check_mx=True)
    if is_valid:
        valid.append(email)
    else:
        invalid.append(email)
    print(is_valid)
