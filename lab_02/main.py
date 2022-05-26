from endianify import Endianify

test_values_fn = 'test_values.txt'
test_values = []

# Load test values from file
with open(test_values_fn, 'r', encoding = 'utf-8') as file:
    test_values = file.read().splitlines()

for hex_value in test_values:

    # Get size of value in bytes
    number_of_bytes = Endianify.BytesCount(hex_value)
    
    # Convert hex value to Little and Big Endian
    little_endian = Endianify.HexToLittleEndian(hex_value)
    big_endian = Endianify.HexToBigEndian(hex_value)

    # Make sure we can convert values back correctly
    little_to_hex = Endianify.LittleEndianToHex(little_endian, number_of_bytes)
    big_to_hex = Endianify.BigEndianToHex(big_endian, number_of_bytes)
    
    # Show the results
    print(f'Value           : {hex_value}')    
    print(f'Number of Bytes : {number_of_bytes}')
    print(f'Little Endian   : {little_endian}')
    print(f'Big Endian      : {big_endian}')
    
    print('-' * 17)

    print(f'Little to Hex   : {little_to_hex}')
    print(f'Big to Hex      : {big_to_hex}')
    print('-' * 128)
