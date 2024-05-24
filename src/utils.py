import hashlib
import base64

def generate_short_url(long_url):
    # Create a SHA-256 hash of the long URL
    sha256_hash = hashlib.sha256(long_url.encode()).digest()
    
    # Encode the hash using Base64 and take the first 6 characters
    short_url = base64.urlsafe_b64encode(sha256_hash).decode()[:6]
    return short_url