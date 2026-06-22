import whois

print("=== WHOIS Lookup Tool ===")

domain = input("Enter domain name: ")

try:
    info = whois.whois(domain)

    print("\nDomain Information:")
    print("Domain Name:", info.domain_name)
    print("Registrar:", info.registrar)
    print("Creation Date:", info.creation_date)
    print("Expiration Date:", info.expiration_date)

except Exception as e:
    print("Error:", e)
