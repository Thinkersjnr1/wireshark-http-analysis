import pyshark

# Load the capture file
cap = pyshark.FileCapture('http_traffic.pcap', display_filter='http')

# Store extracted URLs
urls = []

# Iterate through packets and extract URLs
for packet in cap:
    try:
        host = packet.http.host
        uri = packet.http.request_uri
        full_url = f"http://{host}{uri}"
        urls.append(full_url)
    except AttributeError:
        # Skip packets without HTTP host/URI fields
        continue

# Remove duplicates and print results
unique_urls = sorted(set(urls))
print("Extracted URLs:")
for i, url in enumerate(unique_urls, 1):
    print(f"{i}. {url}")

# Save to a file
with open('urls.txt', 'w') as f:
    f.write("Extracted URLs:\n")
    for i, url in enumerate(unique_urls, 1):
        f.write(f"{i}. {url}\n")

cap.close()
