# Script sederhana untuk mencari Hash MD5 dan SHA256 dari file
# Dibuat untuk tugas Static Analysis Lab

import hashlib
import sys

def get_hashes(filepath):
    # Membaca file secara binary
    with open(filepath, "rb") as f:
        bytes = f.read()
        readable_hash_md5 = hashlib.md5(bytes).hexdigest()
        readable_hash_sha256 = hashlib.sha256(bytes).hexdigest()
        
        print(f"File: {filepath}")
        print(f"MD5: {readable_hash_md5}")
        print(f"SHA256: {readable_hash_sha256}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Cara pakai: python get_hash.py <nama_file>")
    else:
        get_hashes(sys.argv[1])
