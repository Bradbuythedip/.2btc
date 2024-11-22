# Bitcoin 0.2 BTC Puzzle Analysis

This repository contains analysis and solution attempts for the 0.2 BTC puzzle from privatekeys.pw.

## Puzzle Details

- Prize: 0.2 BTC
- Target Bitcoin Address: 1KfZGvwZxsv5memoCmEV75uqcNzYBHjkHZ
- Transaction ID: fcee21d44ee94c09869947c74b61669bf928358e9c2d1699fb075bb6ebf5d043
- Base58 Encoded String: J2LM1xeN3WPiPYgasXB6zZZzcCzM6gNUh77BaiWNmPAJ

## Key Components

1. Red Dots Triangle Pattern
   - 36 dots in 8 rows
   - Diagonal pattern: [0,2,5,9,14,20,27,35]

2. Symbol Sequence
   - △❒●△⧉▣
   - Represents transformation sequence

3. Known Byte Positions
   - Position 7: 9
   - Position 22: 22
   - Position 25: 7

## Repository Structure

- `src/`: Source code for analysis and solution attempts
- `notes/`: Additional analysis and observations
- `tools/`: Helper scripts and utilities

## Analysis Approaches

1. Pattern Analysis
   - Triangle number relationships
   - Base58 character mapping
   - Byte position analysis

2. Transformation Chain
   - Triangle (△) transformation
   - Box (❒) mapping
   - Circle (●) rotation
   - Grid (⧉) overlay
   - Final box (▣) completion

## Running the Analysis

All scripts are written in Python 3 and require the following packages:
- base58
- hashlib (standard library)