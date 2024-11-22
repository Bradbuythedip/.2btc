#!/usr/bin/env python3
import base58
import hashlib
from itertools import permutations

def hash160(data):
    """Perform RIPEMD160(SHA256(data))"""
    h = hashlib.new('ripemd160')
    h.update(hashlib.sha256(data).digest())
    return h.digest()

def pubkey_to_address(pubkey):
    """Convert public key to Bitcoin address"""
    h160 = hash160(pubkey)
    version_h160 = b'\x00' + h160
    checksum = hashlib.sha256(hashlib.sha256(version_h160).digest()).digest()[:4]
    return base58.b58encode(version_h160 + checksum).decode()

# Known information
target_address = "1KfZGvwZxsv5memoCmEV75uqcNzYBHjkHZ"
tx_id = "fcee21d44ee94c09869947c74b61669bf928358e9c2d1699fb075bb6ebf5d043"

# Triangle pattern (36 positions)
triangle = [
    [0],
    [1,2],
    [3,4,5],
    [6,7,8,9],
    [10,11,12,13,14],
    [15,16,17,18,19,20],
    [21,22,23,24,25,26,27],
    [28,29,30,31,32,33,34,35]
]

# Extract potential patterns
diagonal = []
for i, row in enumerate(triangle):
    if i < len(row):
        diagonal.append(row[i])
print(f"Diagonal pattern: {diagonal}")

# Create zigzag pattern
zigzag = []
for i, row in enumerate(triangle):
    if i % 2 == 0:
        zigzag.extend(row)
    else:
        zigzag.extend(reversed(row))
print(f"Zigzag pattern: {zigzag}")

# Try different pattern combinations
def try_pattern(byte_pattern):
    """Try a specific byte pattern as private key"""
    try:
        # Convert to bytes
        key_bytes = bytes(byte_pattern)
        if len(key_bytes) != 32:
            return False
            
        # For testing, just hash the private key directly
        # In reality, we'd need proper Bitcoin key derivation
        address = pubkey_to_address(key_bytes)
        
        if address == target_address:
            print(f"Found matching key: {key_bytes.hex()}")
            return True
    except:
        pass
    return False

# Generate patterns based on transaction ID
tx_bytes = bytes.fromhex(tx_id)

# Test 1: Direct diagonal mapping
pattern1 = [tx_bytes[i] for i in diagonal if i < len(tx_bytes)]
print("\nTesting diagonal pattern...")
try_pattern(pattern1)

# Test 2: Zigzag pattern
pattern2 = [tx_bytes[i] for i in zigzag if i < len(tx_bytes)]
print("\nTesting zigzag pattern...")
try_pattern(pattern2)

# Test 3: Special positions
special_positions = {7:9, 22:22, 25:7}  # Known byte values
print("\nKnown byte positions:", special_positions)

# Look for Base58 alphabet patterns
base58_chars = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
word = "have"
positions = [base58_chars.index(c) for c in word]
print(f"\nPositions of '{word}' in Base58 alphabet: {positions}")

# Symbol sequence analysis
symbols = "△❒●△⧉▣"
print(f"\nSymbol sequence interpretation:")
print("△ (triangle) -> Use diagonal pattern")
print("❒ (box) -> Use grid pattern")
print("● (circle) -> Rotate/transform")
print("△ (triangle) -> Second diagonal pattern")
print("⧉ (grid) -> Final grid overlay")
print("▣ (filled box) -> Complete pattern")