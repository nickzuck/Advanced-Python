import random
import string
from itertools import groupby

domains = [ "hotmail.com", "gmail.com", "aol.com", "mail.com" , "mail.kz", "yahoo.com"]
letters = string.ascii_lowercase[:12]

MAX_EMAILS = 100

def get_one_random_domain(domains):
    return random.choice(domains)

def get_one_random_name(letters):
    return ''.join(random.choice(letters) for i in range(7))

def generate_random_emails():
    return [get_one_random_name(letters) + '@' + get_one_random_domain(domains) for i in range(MAX_EMAILS)]

random_emails = generate_random_emails()
print random_emails


custom_key = lambda x: x.split('@')[-1]

# Grouping the emails
grouped_emails = groupby(sorted(random_emails, key = custom_key), custom_key)

# Printing the grouped emails
for domain, emails  in grouped_emails:
    print domain
    for email_id in emails:
        print email_id,
    print "\n\n"
