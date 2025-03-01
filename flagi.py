import hashlib

flag = picoCTF{FLAG}

hash_object = hashlib.sha256(flag.encode())
hex_dig = hash_object.hexdigest()
print(hex_dig)
