from bf import BloomFilter

# Create Bloom Filter
bloom = BloomFilter(size=200, hash_count=4)

# List of blocked URLs
blocked_urls = [
    "http://malicious-site.com",
    "http://phishing-login.com",
    "http://fake-bank-login.com",
    "http://free-prize-scam.com",
    "http://account-verify-now.com",
    "http://win-lottery-now.com",
    "http://fake-shopping-site.com",
    "http://suspicious-download.com",
    "http://password-reset-fake.com",
    "http://free-money-offer.com",
    "http://fake-payment-page.com",
    "http://online-prize-winner.com",
    "http://urgent-account-alert.com",
    "http://unknown-download.com",
    "http://fake-job-offer.com"
]

# Add blocked URLs to Bloom Filter
for url in blocked_urls:
    bloom.add(url)

# Test predefined URLs
test_urls = [
    "http://malicious-site.com",
    "http://phishing-login.com",
    "http://fake-bank-login.com",
    "http://fake-job-offer.com",
    "https://google.com",
    "https://youtube.com",
    "https://github.com",
    "https://example.com"
]

print("========== BLOOM FILTER URL CHECKER ==========\n")
print("Predefined URL Results:\n")

for url in test_urls:
    if bloom.contains(url):
        print(url, "-> MAY BE BLOCKED")
    else:
        print(url, "-> DEFINITELY NOT BLOCKED")

# User input
print("\n==============================================")
user_url = input("Enter a URL to check: ")

if bloom.contains(user_url):
    print(user_url, "-> MAY BE BLOCKED")
else:
    print(user_url, "-> DEFINITELY NOT BLOCKED")