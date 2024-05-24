import hashlib
import base64
import validators

def generate_short_url(long_url):
    # Create a SHA-256 hash of the long URL
    sha256_hash = hashlib.sha256(long_url.encode()).digest()
    
    # Encode the hash using Base64 and take the first 6 characters
    short_url = base64.urlsafe_b64encode(sha256_hash).decode()[:6] + "-0"
    return short_url

def incr_suff_on_collision(short_url):
    print("handling collision for:", short_url)
    return short_url[:-1] + str(int(short_url[-1]) + 1)

def validate_long_url(long_url):
    try:
        return validators.url(long_url)
    except Exception as e:
        print(e)
        return False