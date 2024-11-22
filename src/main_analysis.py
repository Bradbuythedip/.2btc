#!/usr/bin/env python3
"""
Main analysis script for the 0.2 BTC puzzle
Combines all analysis approaches and provides a unified interface
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'analysis'))

import base58
import hashlib
from puzzle_analyzer import analyze_base58, analyze_txid, find_patterns
from solve_triangle2 import analyze_patterns
from solve_math2 import analyze_mathematical_patterns
from final_solution import apply_transformations

def main():
    """Main analysis function that runs all approaches"""
    # Puzzle constants
    tx_id = "fcee21d44ee94c09869947c74b61669bf928358e9c2d1699fb075bb6ebf5d043"
    target_address = "1KfZGvwZxsv5memoCmEV75uqcNzYBHjkHZ"
    base58_str = "J2LM1xeN3WPiPYgasXB6zZZzcCzM6gNUh77BaiWNmPAJ"

    print("=== Bitcoin 0.2 BTC Puzzle Analysis ===\n")
    
    print("1. Basic Pattern Analysis")
    print("-" * 30)
    analyze_patterns()
    
    print("\n2. Mathematical Pattern Analysis")
    print("-" * 30)
    analyze_mathematical_patterns()
    
    print("\n3. Transformation Chain Analysis")
    print("-" * 30)
    result = apply_transformations(tx_id)
    
    print("\n4. Known Positions Verification")
    print("-" * 30)
    known_positions = {7:9, 22:22, 25:7}
    for pos, expected in known_positions.items():
        if pos < len(result):
            print(f"Position {pos}: Expected {expected}, Got {result[pos]}")

if __name__ == "__main__":
    main()