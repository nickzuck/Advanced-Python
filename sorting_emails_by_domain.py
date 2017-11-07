import random
import string

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

def domain_wise_sort(first_email, second_email):
    first_domain = first_email.split("@")[-1]
    second_domain = second_email.split('@')[-1]
    if first_domain < second_domain :
        return -1
    if first_domain == second_domain:
        return 0 
    if first_domain > second_domain:
        return 1


print sorted(random_emails, cmp = domain_wise_sort)