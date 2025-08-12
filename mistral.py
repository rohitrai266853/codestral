import requests
import json

API_KEY = "your_api_key"
url = "https://codestral.mistral.ai/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

messages = []

while True:
    print("You (type 'exit' to quit, 'END' to finish paste):")
    lines = []
    while True:
        line = input()
        if line.strip().lower() == "exit":
            exit()
        if line.strip() == "END":
            break
        lines.append(line)
    user_input = "\n".join(lines).strip()
    if not user_input:
        continue

    messages.append({"role": "user", "content": user_input})

    payload = {
        "model": "codestral-2501",
        "messages": messages
    }

    resp = requests.post(url, headers=headers, data=json.dumps(payload))

    if resp.status_code != 200:
        print("Error:", resp.text)
        continue

    reply = resp.json()["choices"][0]["message"]["content"]
    print("Codestral:", reply)

    messages.append({"role": "assistant", "content": reply})

