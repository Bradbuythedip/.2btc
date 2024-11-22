#!/usr/bin/env python3
"""
Analysis focusing on row-based patterns and mathematical relationships
"""

TX_ID = "fcee21d44ee94c09869947c74b61669bf928358e9c2d1699fb075bb6ebf5d043"
ROWS = [
    [0],               # Row 1
    [1, 2],           # Row 2
    [3, 4, 5],        # Row 3
    [6, 7, 8, 9],     # Row 4 (contains known position 7)
    [10, 11, 12, 13, 14],         # Row 5
    [15, 16, 17, 18, 19, 20],     # Row 6
    [21, 22, 23, 24, 25, 26, 27], # Row 7 (contains positions 22, 25)
    [28, 29, 30, 31, 32, 33, 34, 35]  # Row 8
]

def analyze_row_relationships():
    """Analyze mathematical relationships between rows"""
    tx_bytes = bytes.fromhex(TX_ID)
    
    print("=== Row Relationship Analysis ===")
    
    # Focus on rows 4 and 7 (containing known positions)
    row4 = [tx_bytes[i] if i < len(tx_bytes) else None for i in ROWS[3]]
    row7 = [tx_bytes[i] if i < len(tx_bytes) else None for i in ROWS[6]]
    
    print("\nRow 4 (contains position 7):")
    print(f"Values: {[hex(x)[2:] if x is not None else 'None' for x in row4]}")
    print(f"Known value at position 7: 0x09")
    
    print("\nRow 7 (contains positions 22, 25):")
    print(f"Values: {[hex(x)[2:] if x is not None else 'None' for x in row7]}")
    print(f"Known values: pos 22 -> 0x16, pos 25 -> 0x07")
    
    # Calculate relationships between known positions
    print("\nRelationships between known positions:")
    pos7_val = tx_bytes[7] if 7 < len(tx_bytes) else None
    pos22_val = tx_bytes[22] if 22 < len(tx_bytes) else None
    pos25_val = tx_bytes[25] if 25 < len(tx_bytes) else None
    
    if all(x is not None for x in [pos7_val, pos22_val, pos25_val]):
        print(f"XOR: {pos7_val} ^ {pos22_val} = {pos7_val ^ pos22_val}")
        print(f"XOR: {pos22_val} ^ {pos25_val} = {pos22_val ^ pos25_val}")
        print(f"XOR: {pos7_val} ^ {pos25_val} = {pos7_val ^ pos25_val}")
        
        print(f"ADD: {pos7_val} + {pos22_val} = {(pos7_val + pos22_val) % 256}")
        print(f"ADD: {pos22_val} + {pos25_val} = {(pos22_val + pos25_val) % 256}")
        print(f"ADD: {pos7_val} + {pos25_val} = {(pos7_val + pos25_val) % 256}")

def analyze_row_patterns():
    """Analyze patterns within each row"""
    tx_bytes = bytes.fromhex(TX_ID)
    
    print("\n=== Row Pattern Analysis ===")
    
    for row_idx, row in enumerate(ROWS, 1):
        row_vals = [tx_bytes[i] if i < len(tx_bytes) else None for i in row]
        print(f"\nRow {row_idx}:")
        print(f"Values: {[hex(x)[2:] if x is not None else 'None' for x in row_vals]}")
        
        # Calculate row statistics
        valid_vals = [x for x in row_vals if x is not None]
        if valid_vals:
            print(f"Sum: {sum(valid_vals)} (mod 256 = {sum(valid_vals) % 256})")
            print(f"XOR: {eval(' ^ '.join(str(x) for x in valid_vals))}")
            
            # Check for arithmetic progressions
            if len(valid_vals) > 2:
                diffs = [valid_vals[i] - valid_vals[i-1] for i in range(1, len(valid_vals))]
                print(f"Differences: {diffs}")

def analyze_diagonal_patterns():
    """Analyze patterns along diagonals"""
    tx_bytes = bytes.fromhex(TX_ID)
    
    print("\n=== Diagonal Pattern Analysis ===")
    
    # Main diagonal
    diagonal = []
    for i, row in enumerate(ROWS):
        if i < len(row):
            pos = row[i]
            if pos < len(tx_bytes):
                diagonal.append(tx_bytes[pos])
    
    print("\nMain diagonal:")
    print(f"Values: {[hex(x)[2:] for x in diagonal]}")
    
    # Anti-diagonal
    anti_diagonal = []
    for i, row in enumerate(ROWS):
        if row:
            pos = row[-1]
            if pos < len(tx_bytes):
                anti_diagonal.append(tx_bytes[pos])
    
    print("\nAnti-diagonal:")
    print(f"Values: {[hex(x)[2:] for x in anti_diagonal]}")

def main():
    print("Starting row-based pattern analysis...")
    analyze_row_relationships()
    analyze_row_patterns()
    analyze_diagonal_patterns()
    
    print("\n=== Additional Observations ===")
    print("1. Known positions follow the pattern:")
    print("   - Position 7 (row 4): Value 9")
    print("   - Position 22 (row 7): Value 22")
    print("   - Position 25 (row 7): Value 7")
    print("\n2. Row relationships:")
    print("   - Row 4 contains one known position")
    print("   - Row 7 contains two known positions")
    print("   - These rows may be key to the transformation sequence")

if __name__ == "__main__":
    main()