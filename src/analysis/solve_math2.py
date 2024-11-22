#!/usr/bin/env python3

# Constants
tx_id = "fcee21d44ee94c09869947c74b61669bf928358e9c2d1699fb075bb6ebf5d043"
base58_alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"

def analyze_patterns():
    """Analyze patterns in the transaction ID and triangle structure"""
    tx_bytes = bytes.fromhex(tx_id)
    
    print("=== Transaction ID Analysis ===")
    # Split into 4-byte chunks
    chunks = [tx_id[i:i+8] for i in range(0, len(tx_id), 8)]
    for i, chunk in enumerate(chunks):
        print(f"Chunk {i}: {chunk}")
    
    print("\n=== Triangle Pattern Analysis ===")
    # Triangle structure
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
    
    # Get values for diagonal pattern
    diagonal = [0,2,5,9,14,20,27,35]
    print(f"Diagonal positions: {diagonal}")
    diagonal_values = [tx_bytes[i] if i < len(tx_bytes) else None for i in diagonal]
    print(f"Diagonal values: {[hex(v)[2:] if v is not None else None for v in diagonal_values]}")
    
    # Known byte positions
    known_bytes = {7:9, 22:22, 25:7}
    print("\n=== Known Byte Analysis ===")
    for pos, val in known_bytes.items():
        if pos < len(tx_bytes):
            print(f"Position {pos}:")
            print(f"  Expected: {val}")
            print(f"  Actual: {tx_bytes[pos]}")
            print(f"  Hex: {hex(tx_bytes[pos])[2:]}")
            print(f"  Base58 index: {tx_bytes[pos] % 58}")
    
    # Look for mathematical patterns
    print("\n=== Mathematical Patterns ===")
    # XOR between consecutive bytes
    xor_pattern = [tx_bytes[i] ^ tx_bytes[i+1] for i in range(len(tx_bytes)-1)]
    print(f"XOR pattern (first 8): {[hex(x)[2:] for x in xor_pattern[:8]]}")
    
    # Modulo 58 values (Base58 alphabet indices)
    mod58_pattern = [b % 58 for b in tx_bytes]
    print(f"Mod 58 pattern (first 8): {mod58_pattern[:8]}")
    
    # Look for triangle number relationships
    triangle_nums = [n * (n + 1) // 2 for n in range(8)]
    print(f"Triangle numbers: {triangle_nums}")
    
    # Check if any bytes in transaction ID correspond to Base58 indices of 'have'
    have_indices = []
    for c in 'have':
        if c in base58_alphabet:
            idx = base58_alphabet.index(c)
            matches = [i for i, b in enumerate(tx_bytes) if b % 58 == idx]
            if matches:
                have_indices.append((c, idx, matches))
    
    if have_indices:
        print("\n=== 'have' Pattern Analysis ===")
        for char, idx, positions in have_indices:
            print(f"Character '{char}' (Base58 index {idx}) found at positions: {positions}")

# Run analysis
analyze_patterns()