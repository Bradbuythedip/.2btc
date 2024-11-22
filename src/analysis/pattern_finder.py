#!/usr/bin/env python3
"""
Pattern finder focusing on specific relationships in the puzzle
"""

# Constants
TX_ID = "fcee21d44ee94c09869947c74b61669bf928358e9c2d1699fb075bb6ebf5d043"
B58_STR = "J2LM1xeN3WPiPYgasXB6zZZzcCzM6gNUh77BaiWNmPAJ"
KNOWN_POS = {7:9, 22:22, 25:7}

def analyze_tx_chunks():
    """Analyze transaction ID in chunks"""
    chunks = [TX_ID[i:i+8] for i in range(0, len(TX_ID), 8)]
    print("Transaction ID chunks:")
    for i, chunk in enumerate(chunks):
        print(f"Chunk {i}: {chunk}")
        # Convert to binary
        bin_val = bin(int(chunk, 16))[2:].zfill(32)
        print(f"Binary: {bin_val}")
        # Count 1s and 0s
        ones = bin_val.count('1')
        zeros = bin_val.count('0')
        print(f"1s: {ones}, 0s: {zeros}")

def find_position_patterns():
    """Look for patterns in known positions"""
    tx_bytes = bytes.fromhex(TX_ID)
    
    print("\nPosition analysis:")
    for pos, val in KNOWN_POS.items():
        # Get surrounding bytes
        prev_byte = tx_bytes[pos-1] if pos > 0 else None
        next_byte = tx_bytes[pos+1] if pos+1 < len(tx_bytes) else None
        
        print(f"\nPosition {pos} (expected {val}):")
        print(f"Previous byte: {hex(prev_byte)[2:] if prev_byte is not None else None}")
        print(f"Current byte: {hex(tx_bytes[pos])[2:]}")
        print(f"Next byte: {hex(next_byte)[2:] if next_byte is not None else None}")
        
        # Look for mathematical relationships
        if prev_byte is not None:
            print(f"Diff with prev: {tx_bytes[pos] - prev_byte}")
        if next_byte is not None:
            print(f"Diff with next: {next_byte - tx_bytes[pos]}")

def analyze_base58_patterns():
    """Analyze patterns in Base58 string"""
    print("\nBase58 string analysis:")
    # Look for repeating characters
    char_count = {}
    for c in B58_STR:
        char_count[c] = char_count.get(c, 0) + 1
    
    print("Character frequencies:")
    for c, count in sorted(char_count.items()):
        if count > 1:
            print(f"'{c}' appears {count} times")
    
    # Look for recurring sequences
    for length in range(2, 4):
        sequences = {}
        for i in range(len(B58_STR)-length+1):
            seq = B58_STR[i:i+length]
            if seq in B58_STR[i+1:]:
                sequences[seq] = sequences.get(seq, 0) + 1
        
        if sequences:
            print(f"\nRepeating sequences of length {length}:")
            for seq, count in sequences.items():
                print(f"'{seq}' appears {count+1} times")

def main():
    print("=== Pattern Analysis ===")
    analyze_tx_chunks()
    find_position_patterns()
    analyze_base58_patterns()

if __name__ == "__main__":
    main()