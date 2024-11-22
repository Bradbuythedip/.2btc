#!/usr/bin/env python3
import base58

# Constants
tx_id = "fcee21d44ee94c09869947c74b61669bf928358e9c2d1699fb075bb6ebf5d043"
base58_alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
diagonal = [0,2,5,9,14,20,27,35]
symbols = "△❒●△⧉▣"

def base58_encode_with_pattern(data, pattern):
    """Encode data using Base58 with a specific pattern"""
    result = []
    tx_bytes = bytes.fromhex(data)
    
    # First apply diagonal pattern
    diagonal_values = [tx_bytes[i] if i < len(tx_bytes) else 0 for i in diagonal]
    print(f"Diagonal values: {[hex(x)[2:] for x in diagonal_values]}")
    
    # Map to Base58 indices
    b58_indices = [x % 58 for x in diagonal_values]
    print(f"Base58 indices: {b58_indices}")
    
    # Get corresponding Base58 characters
    b58_chars = [base58_alphabet[i] for i in b58_indices]
    print(f"Base58 characters: {''.join(b58_chars)}")
    
    # Apply symbol transformations
    transformed = []
    for i, (val, sym) in enumerate(zip(b58_indices, symbols)):
        if sym == '△':  # Triangle - use diagonal value
            transformed.append(val)
        elif sym == '❒':  # Box - use position value
            transformed.append(i % 58)
        elif sym == '●':  # Circle - rotate
            transformed.append((val + i) % 58)
        elif sym == '⧉':  # Grid - use XOR with previous
            prev = transformed[-1] if transformed else 0
            transformed.append(prev ^ val)
        elif sym == '▣':  # Final - use original
            transformed.append(val)
    
    print(f"Transformed indices: {transformed}")
    return transformed

# Try the solution
base58_indices = base58_encode_with_pattern(tx_id, diagonal)

# Convert to potential private key bytes
def indices_to_bytes(indices):
    result = bytearray()
    for i in range(0, len(indices), 2):
        if i + 1 < len(indices):
            msb = indices[i]
            lsb = indices[i+1]
            result.append((msb << 4) | lsb)
    return bytes(result)

private_key = indices_to_bytes(base58_indices)
print(f"\nPotential private key: {private_key.hex()}")

# Check known positions
known_positions = {7:9, 22:22, 25:7}
for pos, val in known_positions.items():
    if pos < len(private_key):
        print(f"Position {pos}: Expected {val}, Got {private_key[pos]}")