# this is vommand line tool inspired by certutil windows
# here is how program's flow look like
# baze63
# coded by me, optimize by AI

import base64
import sys
import os

# function to encode and decode
def encode_base64(input_file):
    with open(input_file, 'rb') as f:
        data = f.read()
    encoded = base64.b64encode(data).decode('utf-8')
    return encoded

def decode_base64(input_file):
    with open(input_file, 'rb') as f:
        data = f.read()
    decoded = base64.b64decode(data).decode('utf-8')
    return decoded

def encode_base32(input_file):
    with open(input_file, 'rb') as f:
        data = f.read()
    encoded = base64.b32encode(data).decode('utf-8')
    return encoded

def decode_base32(input_file):
    with open(input_file, 'rb') as f:
        data = f.read()
    decoded = base64.b32decode(data).decode('utf-8')
    return decoded
# end of function

# main function
def main():
    # argumen must have  4 min
    # python tool.py [mode] [process] filename
    if len(sys.argv) < 4:
        print("Usage: python tool.py <base64|base32> <-e|-d> <filename> [-o <output_filename>]")
        sys.exit(1)

    mode = sys.argv[1]
    operation = sys.argv[2]
    filename = sys.argv[3]
    output_filename = None

    if len(sys.argv) == 6 and sys.argv[4] == '-o':
        output_filename = sys.argv[5]

    if mode == "base64":
        if operation == "-e":
            result = encode_base64(filename)
            #check if file output set by user in cli
            if output_filename:
                with open(output_filename, 'w') as out_file:
                    out_file.write(result)
                print(f"Encoded Base64 saved to: {output_filename}")
            else:
		# tool will return an output if output file not set
                print("Encoded Base64:")
                print(result)
        elif operation == "-d":
            result = decode_base64(filename)
            if output_filename:
                with open(output_filename, 'w') as out_file:
                    out_file.write(result)
                print(f"Decoded Base64 saved to: {output_filename}")
            else:
		#same
                print("Decoded Base64:")
                print(result)
        else:
            print("Invalid operation. Use -e for encode and -d for decode.")
    elif mode == "base32":
        if operation == "-e":
            result = encode_base32(filename)
            if output_filename:
                with open(output_filename, 'w') as out_file:
                    out_file.write(result)
                print(f"Encoded Base32 saved to: {output_filename}")
            else:
		#same
                print("Encoded Base32:")
                print(result)
        elif operation == "-d":
            result = decode_base32(filename)
            if output_filename:
                with open(output_filename, 'w') as out_file:
                    out_file.write(result)
                print(f"Decoded Base32 saved to: {output_filename}")
            else:
		#same
                print("Decoded Base32:")
                print(result)
        else:
            print("Invalid operation. Use -e for encode and -d for decode.")
    else:
        print("Invalid mode. Use base64 or base32.")

if __name__ == "__main__":
    main()
