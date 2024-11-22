#!/usr/bin/env python3
"""
Focused analysis on red dot positions and their relationship to the transaction ID
"""

TX_ID = "fcee21d44ee94c09869947c74b61669bf928358e9c2d1699fb075bb6ebf5d043"
DOTS_PER_ROW = [1, 2, 3, 4, 5, 6, 7, 8]  # Number of dots in each row
KNOWN_POSITIONS = {7: 9, 22: 22, 25: 7}

def analyze_dot_positions():
    """Analyze the positions of dots and their corresponding tx_id bytes"""
    tx_bytes = bytes.fromhex(TX_ID)
    
    # Calculate position indices for each row
    positions = []
    current_pos = 0
    for dots in DOTS_PER_ROW:
        row = list(range(current_pos, current_pos + dots))
        positions.append(row)
        current_pos += dots
    
    print("=== Dot Position Analysis ===")
    print("\nPosition to byte mapping:")
    for row_idx, row in enumerate(positions):
        row_bytes = [tx_bytes[pos] if pos < len(tx_bytes) else None for pos in row]
        print(f"Row {row_idx + 1}: {[hex(b)[2:] if b is not None else 'None' for b in row_bytes]}")
        
        # Check for patterns in byte values
        if len(row_bytes) > 1:
            diffs = []
            for i in range(1, len(row_bytes)):
                if row_bytes[i-1] is not None and row_bytes[i] is not None:
                    diffs.append(row_bytes[i] - row_bytes[i-1])
            if diffs:
                print(f"  Differences: {diffs}")
    
    return positions

def check_known_positions(positions):
    """Check how known positions relate to the triangle structure"""
    tx_bytes = bytes.fromhex(TX_ID)
    
    print("\n=== Known Position Analysis ===")
    for pos, expected in KNOWN_POSITIONS.items():
        # Find position in triangle
        found = False
        for row_idx, row in enumerate(positions):
            if pos in row:
                pos_idx = row.index(pos)
                actual = tx_bytes[pos] if pos < len(tx_bytes) else None
                print(f"\nPosition {pos}:")
                print(f"  Row: {row_idx + 1}, Index in row: {pos_idx}")
                print(f"  Expected value: {expected}")
                print(f"  Actual value: {hex(actual)[2:] if actual is not None else None}")
                
                # Check surrounding values
                if pos_idx > 0:
                    left_pos = row[pos_idx - 1]
                    left_val = tx_bytes[left_pos] if left_pos < len(tx_bytes) else None
                    print(f"  Left neighbor: {hex(left_val)[2:] if left_val is not None else None}")
                if pos_idx < len(row) - 1:
                    right_pos = row[pos_idx + 1]
                    right_val = tx_bytes[right_pos] if right_pos < len(tx_bytes) else None
                    print(f"  Right neighbor: {hex(right_val)[2:] if right_val is not None else None}")
                
                found = True
                break
        
        if not found:
            print(f"Position {pos} not found in triangle structure")

def analyze_byte_patterns():
    """Analyze patterns in transaction ID bytes"""
    tx_bytes = bytes.fromhex(TX_ID)
    
    print("\n=== Byte Pattern Analysis ===")
    
    # Look for repeating byte values
    byte_counts = {}
    for b in tx_bytes:
        byte_counts[b] = byte_counts.get(b, 0) + 1
    
    print("\nRepeating bytes:")
    for byte, count in sorted(byte_counts.items()):
        if count > 1:
            print(f"0x{byte:02x} appears {count} times")
    
    # Look for arithmetic progressions
    print("\nByte differences (first 16 bytes):")
    for i in range(1, min(16, len(tx_bytes))):
        diff = tx_bytes[i] - tx_bytes[i-1]
        print(f"Bytes {i-1}-{i}: {diff}")

def find_potential_patterns():
    """Look for potential patterns that could lead to the solution"""
    positions = analyze_dot_positions()
    check_known_positions(positions)
    analyze_byte_patterns()
    
    # Summary of findings
    print("\n=== Summary of Findings ===")
    print("1. Known positions form a pattern:")
    print("   Position 7  -> 9  (in row 4)")
    print("   Position 22 -> 22 (in row 7)")
    print("   Position 25 -> 7  (in row 7)")
    
    # Check if known positions align with row boundaries
    total_dots = 0
    for row_idx, dots in enumerate(DOTS_PER_ROW, 1):
        row_start = total_dots
        row_end = total_dots + dots - 1
        print(f"\nRow {row_idx}: positions {row_start}-{row_end}")
        for pos in KNOWN_POSITIONS:
            if row_start <= pos <= row_end:
                print(f"  Contains known position {pos}")
        total_dots += dots

def main():
    find_potential_patterns()

if __name__ == "__main__":
    main()