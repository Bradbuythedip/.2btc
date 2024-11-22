#!/usr/bin/env python3
import base58
import hashlib
import binascii

# Known puzzle components
target_address = "1KfZGvwZxsv5memoCmEV75uqcNzYBHjkHZ"
tx_id = "fcee21d44ee94c09869947c74b61669bf928358e9c2d1699fb075bb6ebf5d043"
base58_encoded = "J2LM1xeN3WPiPYgasXB6zZZzcCzM6gNUh77BaiWNmPAJ"

# Analyze Base58 string
def analyze_base58():
    try:
        decoded = base58.b58decode(base58_encoded)
        print(f"Base58 decoded (hex): {decoded.hex()}")
        print(f"Base58 decoded (raw): {decoded}")
        print(f"Length: {len(decoded)} bytes")
    except:
        print("Failed to decode Base58 string")

# Analyze transaction ID
def analyze_txid():
    print(f"Transaction ID length: {len(tx_id)} chars")
    print(f"Transaction ID bytes: {len(tx_id)//2} bytes")
    print("Possible byte values under 24:")
    tx_bytes = binascii.unhexlify(tx_id)
    for i, b in enumerate(tx_bytes):
        if b < 24:
            print(f"Position {i}: {b}")

# Look for patterns in Base58 string
def find_patterns():
    chars = list(base58_encoded)
    print("\nCharacter frequencies:")
    freq = {}
    for c in chars:
        freq[c] = freq.get(c, 0) + 1
    for c, count in sorted(freq.items()):
        print(f"{c}: {count}")
    
    # Look for repeated sequences
    print("\nRepeated sequences (3+ chars):")
    for i in range(len(base58_encoded)-2):
        for j in range(i+3, len(base58_encoded)+1):
            seq = base58_encoded[i:j]
            if base58_encoded.count(seq) > 1:
                print(f"'{seq}' appears {base58_encoded.count(seq)} times")

print("=== Analyzing Base58 String ===")
analyze_base58()
print("\n=== Analyzing Transaction ID ===")
analyze_txid()
print("\n=== Pattern Analysis ===")
find_patterns()