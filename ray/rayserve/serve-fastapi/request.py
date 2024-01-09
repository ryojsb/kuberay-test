import requests

response_healthy = requests.get("http://127.0.0.1:8000/healthz").text
print(response_healthy)

english_text = (
    "It was the best of times, it was the worst of times, it was the age "
    "of wisdom, it was the age of foolishness, it was the epoch of belief"
)
response = requests.get("http://127.0.0.1:8000/summarize", params={"text": english_text})
french_text = response.text

print(french_text)
