import hashlib
import sys

with open(sys.argv[1], "rb") as f:
    print(hashlib.sha256(f.read()).hexdigest())
