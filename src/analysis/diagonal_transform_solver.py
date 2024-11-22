#!/usr/bin/env python3
"""
Solver focusing on diagonal patterns and transformations
"""
import hashlib
import base58
from itertools import combinations

# Constants
TX_ID = "fcee21d44ee94c09869947c74b61669bf928358e9c2d1699fb075bb6ebf5d043"
DIAGONAL_VALUES = ['fc', '21', 'e9', '99', '66', '9c', 'b6']
KNOWN_POS = {7: 9, 22: 22, 25: 7}
BASE58_CHARS = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"

def hex_to_base58_indices(hex_values):
    """Convert hex values to potential Base58 indices"""
    indices = []
    for hex_val in hex_values:
        val = int(hex_val, 16)
        # Try different transformations
        indices.append([
            val % 58,  # Direct modulo
            (val + len(BASE58_CHARS)) % 58,  # Offset modulo
            (val ^ 0x58) % 58,  # XOR with Base58 length
            (val + val % 8) % 58  # Row-based offset
        ])
    return indices

def check_sequence_valid(sequence):
    """Check if a sequence of bytes could be a valid private key"""
    if len(sequence) != 32:
        return False
    # Check known positions
    for pos, val in KNOWN_POS.items():
        if pos < len(sequence) and sequence[pos] != val:
            return False
    return True

def try_diagonal_transformations():
    """Try different transformations on diagonal values"""
    print("=== Testing Diagonal Transformations ===")
    
    # Convert diagonal values to bytes
    diag_bytes = [int(x, 16) for x in DIAGONAL_VALUES]
    print(f"Diagonal bytes: {diag_bytes}")
    
    # Try different transformations
    transformations = []
    
    # 1. Direct mapping
    transformations.append(diag_bytes)
    
    # 2. XOR chain
    xor_chain = []
    current = diag_bytes[0]
    for val in diag_bytes[1:]:
        current ^= val
        xor_chain.append(current)
    transformations.append(xor_chain)
    
    # 3. Rotation based on position
    rot_chain = []
    for i, val in enumerate(diag_bytes):
        rot_chain.append(((val << i) | (val >> (8-i))) & 0xFF)
    transformations.append(rot_chain)
    
    # 4. Row number based
    row_chain = []
    for i, val in enumerate(diag_bytes):
        row_chain.append((val + i + 1) % 256)
    transformations.append(row_chain)
    
    print("\nTransformation results:")
    for i, trans in enumerate(transformations):
        print(f"\nTransformation {i+1}:")
        print(f"Values: {[hex(x)[2:] for x in trans]}")
        print(f"Mod 58: {[x % 58 for x in trans]}")
        
        # Check for Base58 alphabet positions
        b58_positions = [x % 58 for x in trans]
        b58_chars = [BASE58_CHARS[i] for i in b58_positions]
        print(f"Base58 chars: {''.join(b58_chars)}")

def analyze_symbol_sequence_transformation():
    """Analyze transformations based on the symbol sequence △❒●△⧉▣"""
    print("\n=== Symbol Sequence Analysis ===")
    
    tx_bytes = bytes.fromhex(TX_ID)
    diag_bytes = [int(x, 16) for x in DIAGONAL_VALUES]
    
    # △ First triangle - use diagonal values
    print("\n1. Triangle (△) transformation:")
    triangle_values = diag_bytes
    print(f"Values: {[hex(x)[2:] for x in triangle_values]}")
    
    # ❒ Box - apply grid transformation
    print("\n2. Box (❒) transformation:")
    box_values = []
    for i, val in enumerate(triangle_values):
        row = i // 4  # Assuming 4 columns
        col = i % 4
        box_values.append((val + row + col) % 256)
    print(f"Values: {[hex(x)[2:] for x in box_values]}")
    
    # ● Circle - rotate values
    print("\n3. Circle (●) transformation:")
    circle_values = []
    for i, val in enumerate(box_values):
        rotated = ((val << 1) | (val >> 7)) & 0xFF
        circle_values.append(rotated)
    print(f"Values: {[hex(x)[2:] for x in circle_values]}")
    
    # △ Second triangle - apply diagonal pattern
    print("\n4. Second Triangle (△) transformation:")
    second_triangle = []
    for i, val in enumerate(circle_values):
        second_triangle.append((val + diag_bytes[i % len(diag_bytes)]) % 256)
    print(f"Values: {[hex(x)[2:] for x in second_triangle]}")
    
    # ⧉ Grid - map to Base58
    print("\n5. Grid (⧉) transformation:")
    grid_values = [x % 58 for x in second_triangle]
    print(f"Base58 indices: {grid_values}")
    print(f"Base58 chars: {''.join(BASE58_CHARS[i] for i in grid_values)}")

def try_combined_approach():
    """Try combining different transformation approaches"""
    print("\n=== Combined Transformation Approach ===")
    
    tx_bytes = bytes.fromhex(TX_ID)
    diag_bytes = [int(x, 16) for x in DIAGONAL_VALUES]
    
    # Step 1: Use diagonal pattern as key
    key_pattern = diag_bytes
    
    # Step 2: Apply position-based transformation
    transformed = []
    for i, key_byte in enumerate(key_pattern):
        # Try different position-based transformations
        pos_transforms = [
            key_byte,  # Original
            (key_byte + i) % 256,  # Position offset
            key_byte ^ i,  # Position XOR
            (key_byte + (i * i)) % 256  # Square position offset
        ]
        transformed.append(pos_transforms)
    
    print("\nPosition-based transformations:")
    for i, trans in enumerate(transformed):
        print(f"Position {i}: {[hex(x)[2:] for x in trans]}")
        
        # Check Base58 mappings
        b58_indices = [x % 58 for x in trans]
        b58_chars = [BASE58_CHARS[i] for i in b58_indices]
        print(f"Base58 chars: {''.join(b58_chars)}")

def main():
    try_diagonal_transformations()
    analyze_symbol_sequence_transformation()
    try_combined_approach()
    
    print("\n=== Key Observations ===")
    print("1. The diagonal pattern produces identical values in both directions")
    print("2. Known positions (7->9, 22->22, 25->7) may indicate transformation checkpoints")
    print("3. Symbol sequence (△❒●△⧉▣) suggests specific transformation order")
    print("4. Base58 indices might be derived through position-based transformations")

if __name__ == "__main__":
    main()