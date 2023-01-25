from hashlib import sha256

def to_sha256(s):
  return sha256(str.encode(s)).hexdigest()