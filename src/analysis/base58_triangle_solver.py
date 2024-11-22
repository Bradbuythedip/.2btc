#!/usr/bin/env python3
"""
Analysis focusing on Base58 encoding and triangular pattern relationship
"""
import base58
import hashlib
from itertools import combinations

def get_base58_indices(text):
    """Get the Base58 alphabet indices for each character"""
    alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    return [alphabet.index(c) for c in text if c in alphabet]

def triangle_to_base58(triangle_values):
    """Convert triangle values to Base58 string"""
    alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    return ''.join(alphabet[i % 58] for i in triangle_values if i is not None)

def analyze_triangle_sequences():
    """Analyze various triangle reading sequences"""
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
    
    # Different reading patterns
    patterns = {
        'diagonal': [row[i] for i, row in enumerate(triangle) if i < len(row)],
        'reverse_diagonal': [row[-i-1] for i, row in enumerate(triangle) if i < len(row)],
        'left_edges': [row[0] for row in triangle],
        'right_edges': [row[-1] for row in triangle],
        'alternating': [val for i, row in enumerate(triangle) for val in (row if i%2==0 else reversed(row))]
    }
    
    return patterns

def analyze_base58_encoded(encoded_str):
    """Analyze patterns in Base58 encoded string"""
    indices = get_base58_indices(encoded_str)
    
    print(f"Base58 indices: {indices}")
    
    # Look for arithmetic sequences
    diffs = [indices[i] - indices[i-1] for i in range(1, len(indices))]
    print(f"Index differences: {diffs}")
    
    # Look for modular patterns
    mod_values = [i % 8 for i in indices]  # mod 8 for triangle rows
    print(f"Modulo 8 values: {mod_values}")
    
    return indices

def try_triangle_combinations(tx_id, encoded_str):
    """Try different combinations of triangle positions"""
    tx_bytes = bytes.fromhex(tx_id)
    indices = get_base58_indices(encoded_str)
    triangle_patterns = analyze_triangle_sequences()
    
    print("\nTrying triangle position combinations...")
    
    # Try combining different patterns
    for name1, pattern1 in triangle_patterns.items():
        for name2, pattern2 in triangle_patterns.items():
            if name1 < name2:  # Avoid duplicate combinations
                combined = []
                for i, j in zip(pattern1[:len(tx_bytes)], pattern2[:len(tx_bytes)]):
                    val = (tx_bytes[i] + tx_bytes[j]) % 58
                    combined.append(val)
                
                # Check if result contains known values
                if len(combined) >= 26:  # Need at least 26 bytes to check position 25
                    if combined[7] == 9 and combined[22] == 22 and combined[25] == 7:
                        print(f"\nFound matching combination: {name1} + {name2}")
                        print(f"Result: {combined}")
                        try:
                            result_str = triangle_to_base58(combined)
                            print(f"Base58: {result_str}")
                        except:
                            print("Could not convert to Base58")

def main():
    # Known values
    tx_id = "fcee21d44ee94c09869947c74b61669bf928358e9c2d1699fb075bb6ebf5d043"
    encoded_str = "J2LM1xeN3WPiPYgasXB6zZZzcCzM6gNUh77BaiWNmPAJ"
    
    print("=== Base58 Triangle Analysis ===")
    
    # Analyze Base58 encoded string
    print("\nAnalyzing Base58 encoded string...")
    indices = analyze_base58_encoded(encoded_str)
    
    # Try triangle combinations
    try_triangle_combinations(tx_id, encoded_str)

if __name__ == "__main__":
    main()