import password_generator
import password_strength_checker
import hash_generator
import port_scanner
import dns_lookup
import whois_lookup
import file_integrity_checker

print("=== Cyber Security Toolkit ===")

print("1. Password Generator")
print("2. Password Strength Checker")
print("3. Hash Generator")
print("4. Port Scanner")
print("5. DNS Lookup")
print("6. WHOIS Lookup")
print("7. File Integrity Checker")

choice = input("\nSelect an option: ")

if choice == "1":
    password_generator
elif choice == "2":
    password_strength_checker
elif choice == "3":
    hash_generator
elif choice == "4":
    port_scanner
elif choice == "5":
    dns_lookup
elif choice == "6":
    whois_lookup
elif choice == "7":
    file_integrity_checker
else:
    print("Invalid option")
