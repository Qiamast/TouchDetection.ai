import requests
from requests.structures import CaseInsensitiveDict

import json

QUERY_URL = "https://api.openai.com/v1/images/generations"

def detect_ai_image(image_url):
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"
    headers["Authorization"] = f"Bearer {secrets['api_key']}"

    data = """
    {
        """
    data += f'"model": "image-alpha-001",'
    data += f'"data": [{{ "url": "{image_url}" }}],'
    data += """
        "num_images":1,
        "size":"256x256",
        "response_format":"url"
    }
    """

    resp = requests.post(QUERY_URL, headers=headers, data=data)

    if resp.status_code != 200:
        raise ValueError("Failed to generate image "+resp.text)

    response_text = json.loads(resp.text)
    return response_text["data"][0]["url"]

