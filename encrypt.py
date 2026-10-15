from cryptography.fernet import Fernet
# Step 1: Generate a key (store this securely for reuse)
key = Fernet.generate_key()
print(key)
cipher = Fernet(key)
# Step 2: Take user input
message = input("Enter a sentence to encrypt: ")
# Step 3: Encrypt the message
encrypted_message = cipher.encrypt(message.encode())
# Step 4: Display results
print("\nOriginal Message:", message)
print("Encrypted Message:", encrypted_message.decode())
# Step 5: Decrypt to verify (optional)
decrypted_message = cipher.decrypt(encrypted_message).decode()
print("Decrypted Message:", decrypted_message)
