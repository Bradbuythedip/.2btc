#!/usr/bin/env python3
"""
Analysis of binary patterns in the red dot triangle
"""
import itertools

def generate_binary_patterns(dots_per_row):
    """Generate all possible binary patterns for the triangle"""
    total_dots = sum(dots_per_row)
    patterns = []
    
    for bits in itertools.product([0, 1], repeat=total_dots):
        pattern = []
        start = 0
        for row_dots in dots_per_row:
            pattern.append(list(bits[start:start+row_dots]))
            start += row_dots
        patterns.append(pattern)
    return patterns[:100]  # Limit to first 100 patterns for analysis

def analyze_binary_pattern(pattern):
    """Analyze a binary pattern for potential significance"""
    # Convert pattern to bytes
    bits = []
    for row in pattern:
        bits.extend(row)
    
    # Convert bits to bytes
    bytes_data = []
    for i in range(0, len(bits), 8):
        if i + 8 <= len(bits):
            byte = 0
            for bit_pos in range(8):
                byte = (byte << 1) | bits[i + bit_pos]
            bytes_data.append(byte)
    
    return bytes(bytes_data)

def check_known_positions(bytes_data):
    """Check if bytes data matches known positions"""
    known_pos = {7: 9, 22: 22, 25: 7}
    for pos, val in known_pos.items():
        if pos < len(bytes_data) and bytes_data[pos] != val:
            return False
    return True

def main():
    # Triangle structure (dots per row)
    dots_per_row = [1, 2, 3, 4, 5, 6, 7, 8]
    
    print("Generating binary patterns...")
    patterns = generate_binary_patterns(dots_per_row)
    
    print(f"Analyzing {len(patterns)} patterns...")
    for i, pattern in enumerate(patterns):
        bytes_data = analyze_binary_pattern(pattern)
        if check_known_positions(bytes_data):
            print(f"\nFound potentially matching pattern {i}:")
            print("Binary pattern:")
            for row in pattern:
                print(''.join(str(b) for b in row))
            print("Bytes:", bytes_data.hex())

if __name__ == "__main__":
    main()