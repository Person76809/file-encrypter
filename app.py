import os
from Crypto.Cipher import AES

# Define the key and block size
key = b'MySuperSecretKey!'
block_size = 16

# Function to pad the data
def pad(data):
    padding_size = block_size - len(data) % block_size
    padding = chr(padding_size) * padding_size
    return data + padding.encode()

# Function to encrypt the file
def encrypt_file(input_file_path, output_file_path):
    # Open the input and output files
    with open(input_file_path, 'rb') as input_file, open(output_file_path, 'wb') as output_file:
        # Initialize the cipher with the key and mode
        cipher = AES.new(key, AES.MODE_ECB)
        # Read and pad the data from the input file
        data = pad(input_file.read())
        # Encrypt the data and write it to the output file
        output_file.write(cipher.encrypt(data))
        # Delete the original file
        os.remove(input_file_path)

# Usage example
encrypt_file('my_file.txt', 'my_file_encrypted.txt')
