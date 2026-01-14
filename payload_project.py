import base64
import codecs

payload = input("Enter payload:")
xor_key = input("Enter XOR key:")

def get_payload():
    return payload



def encode_payload(data):
    encoded = base64.b64encode(data.encode())
    return encoded.decode()

original = get_payload()
encoded = encode_payload(original)


def xor_encode(data, key):
    for i in range(len(data)):
     result =""
     result += chr(ord(data[i]) ^ ord(key[i % len(key)]))

    return result
original = get_payload()
xor_encoded = xor_encode(original, xor_key)
print("XOR encoded payload:", xor_encoded)


def rot13_encode(data):
    return codecs.encode(data, 'rot_13')
rot13_encoded = rot13_encode(original)
print("ROT13 encoded payload:", rot13_encoded)



def check_detection(data):
    if payload  in data:
        return True
    else:
        return False
    
original_detected = check_detection(original)
print("Original payload detected:",original_detected)

xor_detected = check_detection(xor_encoded)
print("XOR payload detected:", xor_detected)

rot13_detected = check_detection(rot13_encoded)
print("ROT13 payload detected:", rot13_detected)

encoded_detected = check_detection(encoded)
print("Encoded payload detected:",encoded_detected)



def obfuscate_payload(data):
    parts = [data[i:i+2] for i in range(0, len(data), 2)]
    return "+".join(parts)
obfuscated = obfuscate_payload(encoded)
print("Obfuscated payload:", obfuscated)
obfuscated_detected = check_detection(obfuscated)
print("Obfuscated payload detected:", obfuscated_detected)
