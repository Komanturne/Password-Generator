import hashlib

def fourth(hex_block: str, plaintext: str) -> str:
    key_bytes = bytes.fromhex(hex_block)

    plain_bytes = plaintext.encode('utf-8')
    key_len = len(key_bytes)
    plain_len = len(plain_bytes)
    if key_len < plain_len:
        key_bytes = (key_bytes * (plain_len // key_len + 1))[:plain_len]
    else:
        key_bytes = key_bytes[:plain_len]
    xor_bytes = bytes([p ^ k for p, k in zip(plain_bytes, key_bytes)])
    transformed_bytes = bytes([(b + (i % 256)) % 256 for i, b in enumerate(xor_bytes)])
    passcode = transformed_bytes.hex()

    return passcode

hex_block = "d43af76aa357840e141a877bc2858a3c85131a2727f82a385609384d1a6091e1f5c5a8abe8a5b1af35ec3edf8e7e6660a68290c493902563944d9384dfb23428e48f30208ba558473d9cc0a3a7a5ccd8e097bbd3c590b231548efebc4fed1699be0f686de66e406e2c871dbd570119093d1c7f933967c3fb414d2f32f638ee89eaf81a145533bbc24e61bfed8336f352ac3f408fd9d2c8c8cfa5ce3957f5063cffe92a8c56c9037075d5ef6fddf9aa64a06dad3b2093a1dc2f627d43af76aa357840e141a877bc2858a3c85131a2727f82a385609384d1a6091e1f5c5a8abe8a5b1af35ec3edf8e7e6660a68290c493902563944d9384dfb23428e48f30208ba"
plaintext = ""
passcode = fourth(hex_block, plaintext)
print("Generated passcode:", passcode)
