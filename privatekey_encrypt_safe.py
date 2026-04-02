from cryptography.fernet import Fernet

# 生成密钥
KEY = Fernet.generate_key()
cipher = Fernet(KEY)

def encrypt_privatekey(key):
    encrypted = cipher.encrypt(key.encode())
    print(f"加密后: {encrypted.decode()}")
    return encrypted

def decrypt_privatekey(encrypted_data):
    decrypted = cipher.decrypt(encrypted_data).decode()
    print(f"解密后: {decrypted}")
    return decrypted

if __name__ == "__main__":
    pk = "0x1234567890abcdef"
    enc = encrypt_privatekey(pk)
    decrypt_privatekey(enc)
