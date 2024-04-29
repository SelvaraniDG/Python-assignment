def company_name(email):
    parts = email.split('@')
    if len(parts) != 2:
        raise ValueError("Invalid email format.")
    company_name = parts[1].split('.')[0].capitalize()
    return company_name

def get_email():
    try:
        email = input("Enter an email address: ")
        cname = company_name(email)
        return cname
    except ValueError as ve:
        print("Error:", ve)
        return get_email()

company_name = get_email()
print("Company Name:", company_name)