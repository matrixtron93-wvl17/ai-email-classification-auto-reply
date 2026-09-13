import csv

INPUT_FILE = 'data/sample_emails.csv'

with open(INPUT_FILE, 'r', encoding='utf-8') as file:
    emails = list(csv.DictReader(file))

print('Email Data Processing Complete')
print('Total Emails:', len(emails))
