import hashlib

def generate_hash(text):
    sha256_hash = hashlib.sha256(text.encode())
    return sha256_hash.hexdigest()

print("=== SHA-256 Hash Generator ===")

text = input("Enter text to hash: ")

hash_value = generate_hash(text)

print("\nSHA-256 Hash:")
print(hash_value)
