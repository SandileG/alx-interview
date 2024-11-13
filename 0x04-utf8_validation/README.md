# 0x04. UTF-8 Validation

## Project Overview
This project is about validating if a given dataset represents a valid UTF-8 encoding. It combines bitwise operations, data representation, and boolean logic to achieve character validation at the byte level in Python. 

The function `valid_utf8(data)` will check whether each byte in the dataset adheres to the UTF-8 encoding standard.

## Key Concepts

### 1. UTF-8 Encoding Scheme
UTF-8 is a variable-width character encoding system that can represent each Unicode character using 1 to 4 bytes. The first byte determines the total length of the character:
- **1-byte character**: `0xxxxxxx` - Standard ASCII.
- **2-byte character**: `110xxxxx 10xxxxxx`.
- **3-byte character**: `1110xxxx 10xxxxxx 10xxxxxx`.
- **4-byte character**: `11110xxx 10xxxxxx 10xxxxxx 10xxxxxx`.

Each UTF-8 character sequence starts with a "leading byte" that indicates the character length and continues with "continuation bytes" for multi-byte characters.

### 2. Bitwise Operations
The validation function uses bitwise operators to:
- Mask the leading bits of each byte to determine its type.
- Identify if bytes follow the correct UTF-8 patterns.

#### Bitwise Operators
- **AND (`&`)**: Used to extract bits.
- **Shift Right (`>>`)**: Used to check leading bits by shifting positions.
  
For example, checking if a byte starts with `110` can be done with:
```python
(byte >> 5) == 0b110
```

### 3. Data Representation at the Byte Level
We treat each integer in the dataset as an 8-bit byte. UTF-8 validation involves iterating through each byte and checking if it aligns with UTF-8 encoding rules.

### 4. List Manipulation
The function iterates over a list of bytes, managing state as it moves through UTF-8 character sequences.

### 5. Boolean Logic
Logical checks ensure that each byte conforms to the expected pattern. If any byte violates the UTF-8 rules, the function returns `False`.

## Approach to the Validation Function

The algorithm steps through the following process for each byte:

1. **Initialize a Counter**:  
   `num_bytes` keeps track of the expected number of continuation bytes based on the initial byte in each sequence.

2. **Determine Byte Type**:
   - If `num_bytes` is 0, determine the length of the character based on the leading bits.
   - If `num_bytes` is greater than 0, check that each continuation byte matches the `10xxxxxx` pattern.

3. **Pattern Matching with Bitwise Operations**:
   - Use bitwise shifts and masks to match the UTF-8 patterns for leading and continuation bytes.

4. **Return the Result**:
   - The function returns `True` if all bytes conform to UTF-8, and `False` otherwise.

## Conclusion
By combining Python programming, bitwise operations, and UTF-8 encoding rules, this project demonstrates how to validate character encoding at a low level.
