import requests

url = "http://localhost:8000/generate-essay"
data = {
    "topic": "best friend",
    "forward_url": "http://localhost:8000/essay"  # Replace with the actual URL you want to forward the response to
}

response = requests.post(url, json=data)
if response.status_code == 200:
    print("Essay successfully forwarded")
    try:
        forwarded_response = response.json()
        print(forwarded_response)
    except (KeyError, ValueError) as e:
        print(f"Error parsing forwarded response JSON: {e}")
else:
    print(f"Status Code: {response.status_code}")
    print(f"Raw Response: {response.text}")
