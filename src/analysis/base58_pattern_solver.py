#!/usr/bin/env python3
"""
Analysis focusing on Base58 encoding patterns and relationships
"""
import base58
from itertools import combinations

# Constants
TX_ID = "fcee21d44ee94c09869947c74b61669bf928358e9c2d1699fb075bb6ebf5d043"
B58_STRING = "J2LM1xeN3WPiPYgasXB6zZZzcCzM6gNUh77BaiWNmPAJ"
KNOWN_POS = {7: 9, 22: 22, 25: 7}
BASE58_CHARS = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"

def analyze_b58_positions():
    """Analyze positions of characters in Base58 string"""
    print("=== Base58 Position Analysis ===")
    
    # Map each character to its positions
    char_positions = {}
    for i, c in enumerate(B58_STRING):
        if c not in char_positions:
            char_positions[c] = []
        char_positions[c].append(i)
    
    print("\nCharacter positions:")
    for char, positions in sorted(char_positions.items()):
        if len(positions) > 1:
            print(f"'{char}': {positions}")
            print(f"Differences: {[positions[i] - positions[i-1] for i in range(1, len(positions))]}")
            
            # Check Base58 alphabet position
            b58_pos = BASE58_CHARS.index(char)
            print(f"Base58 alphabet position: {b58_pos}")

def analyze_known_value_patterns():
    """Analyze patterns related to known position values"""
    print("\n=== Known Value Pattern Analysis ===")
    
    for pos, val in KNOWN_POS.items():
        print(f"\nPosition {pos} -> {val}:")
        
        # Base58 properties
        b58_char = BASE58_CHARS[val % 58]
        print(f"Base58 char at value: {b58_char}")
        print(f"Base58 position: {val % 58}")
        
        # Find occurrences in B58_STRING
        occurrences = [i for i, c in enumerate(B58_STRING) if c == b58_char]
        if occurrences:
            print(f"Character appears in Base58 string at: {occurrences}")
            if len(occurrences) > 1:
                print(f"Differences: {[occurrences[i] - occurrences[i-1] for i in range(1, len(occurrences))]}")

def find_base58_transformations():
    """Find potential Base58 transformations"""
    print("\n=== Base58 Transformation Analysis ===")
    
    tx_bytes = bytes.fromhex(TX_ID)
    
    # Try different Base58 encoding patterns
    patterns = [
        tx_bytes[:8],  # First 8 bytes
        tx_bytes[8:16],  # Second 8 bytes
        tx_bytes[16:24],  # Third 8 bytes
        tx_bytes[24:32],  # Fourth 8 bytes
        tx_bytes[::2],  # Every second byte
        tx_bytes[1::2],  # Every second byte starting from 1
        bytes([tx_bytes[i] for i in sorted(KNOWN_POS.keys())])  # Known positions
    ]
    
    print("\nTrying different byte patterns:")
    for i, pattern in enumerate(patterns):
        try:
            b58_encoded = base58.b58encode(pattern).decode()
            print(f"\nPattern {i+1}:")
            print(f"Bytes: {[hex(x)[2:] for x in pattern]}")
            print(f"Base58: {b58_encoded}")
            
            # Look for matches with known position values
            for pos, val in KNOWN_POS.items():
                if pos < len(pattern):
                    print(f"Position {pos}: {pattern[pos]} vs expected {val}")
        except:
            print(f"Pattern {i+1}: Invalid Base58 encoding")

def analyze_b58_structure():
    """Analyze the structure of the Base58 encoded string"""
    print("\n=== Base58 Structure Analysis ===")
    
    # Split string into chunks
    chunk_size = 8
    chunks = [B58_STRING[i:i+chunk_size] for i in range(0, len(B58_STRING), chunk_size)]
    
    print("\nChunk analysis:")
    for i, chunk in enumerate(chunks):
        print(f"\nChunk {i+1}: {chunk}")
        # Analyze character types
        upper = sum(1 for c in chunk if c.isupper())
        lower = sum(1 for c in chunk if c.islower())
        digits = sum(1 for c in chunk if c.isdigit())
        print(f"Upper: {upper}, Lower: {lower}, Digits: {digits}")
        
        # Get Base58 positions for each character
        positions = [BASE58_CHARS.index(c) for c in chunk]
        print(f"Base58 positions: {positions}")
        print(f"Differences: {[positions[i] - positions[i-1] for i in range(1, len(positions))]}")

def main():
    print("Starting Base58 pattern analysis...")
    analyze_b58_positions()
    analyze_known_value_patterns()
    find_base58_transformations()
    analyze_b58_structure()
    
    print("\n=== Key Findings ===")
    print("1. Base58 string structure:")
    print(f"  - Length: {len(B58_STRING)}")
    print("  - Character distribution variations")
    print("  - Pattern of uppercase/lowercase/digits")
    
    print("\n2. Known value relationships:")
    for pos, val in KNOWN_POS.items():
        b58_char = BASE58_CHARS[val % 58]
        print(f"  Position {pos} -> Value {val} -> Base58 char '{b58_char}'")

if __name__ == "__main__":
    main()