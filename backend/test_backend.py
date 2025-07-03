import requests

url = 'http://127.0.0.1:5000/summarize'
file_path = 'audio.mp3'  # Update with your file name

with open(file_path, 'rb') as f:
    files = {'file': f}
    response = requests.post(url, files=files)

if response.status_code == 200:
    with open('summary.pdf', 'wb') as out:
        out.write(response.content)
    print("✅ PDF downloaded as summary.pdf")
else:
    print("❌ Error:", response.text)
