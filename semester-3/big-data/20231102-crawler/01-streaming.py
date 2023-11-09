import requests
from tqdm import tqdm

url = "https://bit.ly/5GB-TESTFILE-ORG"
response = requests.get(url)
response.raise_for_status()

with open("out3_14.txt", 'wb') as file_object:
    for chunk in tqdm(response.iter_content(256), desc="Downloading"):
        size = file_object.write(chunk)

print("Done.")
