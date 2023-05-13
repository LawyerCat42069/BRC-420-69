import gzip
import lzma
import bz2

def compress_file(file_path):
    compression_methods = [
        (gzip.compress, 'gzip'),
        (lzma.compress, 'lzma'),
        (bz2.compress, 'bz2')
    ]

    best_compression_ratio = float('inf')
    best_compressed_data = None
    best_compression_method = None

    with open(file_path, 'rb') as file:
        original_data = file.read()

    for compress_method, method_name in compression_methods:
        compressed_data = compress_method(original_data)
        compression_ratio = len(compressed_data) / len(original_data)

        if compression_ratio < best_compression_ratio:
            best_compression_ratio = compression_ratio
            best_compressed_data = compressed_data
            best_compression_method = method_name

    if best_compressed_data:
        compressed_file_path = f'{file_path}.{best_compression_method}'
        with open(compressed_file_path, 'wb') as compressed_file:
            compressed_file.write(best_compressed_data)
        print(f"Compression complete. Best method: {best_compression_method}. Saved as {compressed_file_path}")
    else:
        print("Compression failed.")

# Example usage
input_file = 'file.txt'

compress_file(input_file)
