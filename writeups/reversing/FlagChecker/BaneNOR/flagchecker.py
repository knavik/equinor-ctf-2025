def decode(encoded_text):
    decoded = []
    
    for position, char in enumerate(encoded_text):
        if not char.isupper():
            decoded.append(char)
            continue
        
        encoded_value = ord(char) - ord('A')  # Convert to 0-25 range
        
        for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            test_encoding = (position + ord(letter) - 48) % 26
            if test_encoding == encoded_value:
                decoded.append(letter)
                break
    return ''.join(decoded)

ENC_FLAG = "VHM{WQQQDCPPGXNSLQBQCQNHVEFV}"
flag = decode(ENC_FLAG)
print(f"Flag: {flag}")