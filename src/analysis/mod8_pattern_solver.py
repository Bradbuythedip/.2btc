#!/usr/bin/env python3
"""
Analysis focusing on mod 8 patterns and position XOR relationships
"""
import hashlib
import base58
from itertools import product

# Constants
TX_ID = "fcee21d44ee94c09869947c74b61669bf928358e9c2d1699fb075bb6ebf5d043"
DIAGONAL_VALUES = ['fc', '21', 'e9', '99', '66', '9c', 'b6']
KNOWN_POS = {7: 9, 22: 22, 25: 7}
SYMBOLS = "△❒●△⧉▣"  # Symbol sequence

def analyze_mod8_patterns():
    """Analyze patterns based on mod 8 relationships"""
    tx_bytes = bytes.fromhex(TX_ID)
    
    print("=== Mod 8 Pattern Analysis ===")
    
    # Analyze each row (8 bytes per row)
    for row in range(4):  # 32 bytes = 4 rows of 8
        start = row * 8
        row_bytes = tx_bytes[start:start+8]
        if row_bytes:
            print(f"\nRow {row}:")
            print(f"Values: {[hex(x)[2:] for x in row_bytes]}")
            print(f"Mod 8: {[x % 8 for x in row_bytes]}")
            
            # Check if any known positions in this row
            row_known = {pos: val for pos, val in KNOWN_POS.items() 
                        if start <= pos < start + 8}
            if row_known:
                print(f"Known positions in row: {row_known}")
                
                # Analyze relationship between position and value
                for pos, val in row_known.items():
                    rel_pos = pos % 8  # Position within row
                    print(f"\nPosition {pos} analysis:")
                    print(f"Row position: {rel_pos}")
                    print(f"Value: {val}")
                    print(f"Value mod 8: {val % 8}")
                    print(f"Position XOR Value: {rel_pos ^ val}")

def find_mod8_transformations():
    """Find transformations that preserve mod 8 relationships"""
    print("\n=== Mod 8 Transformation Analysis ===")
    
    # Try different transformations that preserve mod 8 relationships
    for pos, val in KNOWN_POS.items():
        print(f"\nAnalyzing position {pos} -> value {val}")
        row = pos // 8
        col = pos % 8
        
        # Test different operations that might preserve the relationship
        operations = [
            lambda x, r, c: (x + r) % 8,
            lambda x, r, c: (x + c) % 8,
            lambda x, r, c: (x + r + c) % 8,
            lambda x, r, c: (x ^ r ^ c) % 8,
            lambda x, r, c: (x * (r + 1)) % 8,
            lambda x, r, c: (x * (c + 1)) % 8
        ]
        
        print(f"Row {row}, Col {col}")
        for i, op in enumerate(operations, 1):
            result = op(val, row, col)
            print(f"Operation {i}: {result}")
            if result == val % 8:
                print("^ Matches original value mod 8")

def analyze_symbol_mod8():
    """Analyze how symbols might relate to mod 8 patterns"""
    print("\n=== Symbol-Mod8 Relationship Analysis ===")
    
    tx_bytes = bytes.fromhex(TX_ID)
    
    # Map symbols to positions
    for i, symbol in enumerate(SYMBOLS):
        print(f"\nSymbol {symbol} (position {i}):")
        
        # Get relevant bytes based on symbol position
        start = i * 4  # Assume each symbol affects 4 bytes
        bytes_chunk = tx_bytes[start:start+4]
        if bytes_chunk:
            print(f"Values: {[hex(x)[2:] for x in bytes_chunk]}")
            print(f"Mod 8: {[x % 8 for x in bytes_chunk]}")
            
            # Check for any known positions in this range
            relevant_known = {pos: val for pos, val in KNOWN_POS.items()
                            if start <= pos < start + 4}
            if relevant_known:
                print(f"Known positions in range: {relevant_known}")

def find_triangle_mod8_patterns():
    """Analyze mod 8 patterns in triangle structure"""
    print("\n=== Triangle Mod 8 Analysis ===")
    
    # Triangle structure
    triangle = [
        [0],
        [1, 2],
        [3, 4, 5],
        [6, 7, 8, 9],
        [10, 11, 12, 13, 14],
        [15, 16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25, 26, 27],
        [28, 29, 30, 31, 32, 33, 34, 35]
    ]
    
    tx_bytes = bytes.fromhex(TX_ID)
    
    # Analyze each row of triangle
    for row_idx, row in enumerate(triangle):
        print(f"\nTriangle Row {row_idx + 1}:")
        row_bytes = [tx_bytes[i] if i < len(tx_bytes) else None for i in row]
        valid_bytes = [b for b in row_bytes if b is not None]
        if valid_bytes:
            print(f"Values: {[hex(x)[2:] for x in valid_bytes]}")
            print(f"Mod 8: {[x % 8 for x in valid_bytes]}")
            
            # Check for known positions
            row_known = {pos: val for pos, val in KNOWN_POS.items() 
                        if pos in row}
            if row_known:
                print(f"Known positions: {row_known}")
                
                # Analyze relationships within row
                for pos, val in row_known.items():
                    idx_in_row = row.index(pos)
                    print(f"\nPosition {pos} in row:")
                    print(f"Row index: {idx_in_row}")
                    print(f"Row size: {len(row)}")
                    print(f"Value mod 8: {val % 8}")
                    print(f"Position in row XOR value: {idx_in_row ^ val}")

def main():
    print("Starting mod 8 pattern analysis...")
    analyze_mod8_patterns()
    find_mod8_transformations()
    analyze_symbol_mod8()
    find_triangle_mod8_patterns()
    
    print("\n=== Key Findings ===")
    print("1. Position-value relationships:")
    for pos, val in KNOWN_POS.items():
        print(f"  Position {pos}:")
        print(f"  - Row: {pos // 8}, Col: {pos % 8}")
        print(f"  - Value: {val} (mod 8: {val % 8})")
        print(f"  - Position XOR Value: {pos ^ val}")
    
    print("\n2. Symbol relationships:")
    print("  - Each symbol might correspond to a specific mod 8 transformation")
    print("  - Triangle pattern shows consistent mod 8 relationships")
    print("  - Known positions align with symbol boundaries")

if __name__ == "__main__":
    main()