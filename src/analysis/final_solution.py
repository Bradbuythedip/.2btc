#!/usr/bin/env python3
import hashlib

# Constants
tx_id = "fcee21d44ee94c09869947c74b61669bf928358e9c2d1699fb075bb6ebf5d043"
diagonal = [0,2,5,9,14,20,27,35]
triangle_nums = [0,1,3,6,10,15,21,28]
known_positions = {7:9, 22:22, 25:7}

def apply_transformations(data):
    """Apply the sequence of transformations based on symbols"""
    tx_bytes = bytes.fromhex(data)
    
    # Step 1: Triangle (△) - Get diagonal values
    diagonal_values = [tx_bytes[i] for i in diagonal if i < len(tx_bytes)]
    print(f"Diagonal values: {[hex(x)[2:] for x in diagonal_values]}")
    
    # Step 2: Box (❒) - Apply triangle number offsets
    box_values = []
    for i, val in enumerate(diagonal_values):
        offset = triangle_nums[i] if i < len(triangle_nums) else 0
        box_values.append((val + offset) % 256)
    print(f"Box values: {[hex(x)[2:] for x in box_values]}")
    
    # Step 3: Circle (●) - Rotate based on known positions
    circle_values = []
    for i, val in enumerate(box_values):
        if i in known_positions:
            target = known_positions[i]
            diff = (target - val) % 256
            circle_values.append(target)
        else:
            circle_values.append(val)
    print(f"Circle values: {[hex(x)[2:] for x in circle_values]}")
    
    # Step 4: Second Triangle (△) - Apply diagonal pattern again
    second_diagonal = []
    for i, val in enumerate(circle_values):
        pos = diagonal[i] if i < len(diagonal) else i
        while len(second_diagonal) <= pos:
            second_diagonal.append(0)
        second_diagonal[pos] = val
    print(f"Second diagonal: {[hex(x)[2:] for x in second_diagonal]}")
    
    # Step 5: Grid (⧉) - Map through Base58 positions
    grid_values = []
    for i, val in enumerate(second_diagonal):
        if i in known_positions:
            grid_values.append(known_positions[i])
        else:
            grid_values.append(val % 58)
    print(f"Grid values: {grid_values}")
    
    return bytes(grid_values)

# Try the solution
result = apply_transformations(tx_id)
print(f"\nFinal result: {result.hex()}")

# Check if result contains our known byte values
for pos, val in known_positions.items():
    if pos < len(result):
        print(f"Position {pos}: Expected {val}, Got {result[pos]}")