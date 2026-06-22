import hashlib

print("=== File Integrity Checker ===")

file_path = input("Enter file path: ")

try:
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        while chunk := file.read(4096):
            sha256.update(chunk)

    current_hash = sha256.hexdigest()

    print("\nCurrent SHA-256 Hash:")
    print(current_hash)

    expected_hash = input("\nEnter expected hash: ")

    if current_hash.lower() == expected_hash.lower():
        print("✓ File integrity verified")
    else:
        print("✗ File may have been modified")

except FileNotFoundError:
    print("File not found")
