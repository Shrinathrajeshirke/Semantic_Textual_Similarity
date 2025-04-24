import requests

url = "http://127.0.0.1:5000/similarity"
payload = {
    "text1": "Artificial intelligence is evolving rapidly.",
    "text2": "AI technology is growing fast."
}
response = requests.post(url, json=payload)
print(response.json())