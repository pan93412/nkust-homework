import requests

payload = {
    "organization": ["NKUST", "Intelligent Commerce"],
    "member": "Student",
}

post_response = requests.post(
    url="https://httpbin.org/post",
    data=payload,
)
post_response.raise_for_status()
print("Post response:\n\t", post_response.json())

get_response = requests.get(
    url="https://httpbin.org/",
    params=payload,
)
get_response.raise_for_status()
print("Get URL:\n\t", get_response.request.url)
