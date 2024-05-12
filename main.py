from PIL import Image
from io import BytesIO
import requests

# The API endpoint
# url = "https://pixabay.com/api/?key=43843784-ca8a7d4eb022dffa63faad957&q=yellow+flowers&image_type=photo"
# url = "https://pixabay.com/api/?key=43843784-ca8a7d4eb022dffa63faad957&id=195893"
url = "https://cdn.pixabay.com/photo/2024/02/25/10/11/forsythia-8595521_150.jpg"

# A GET request to the API
response = requests.get(url)

# Print the response
# response_json = response.json()
# print(response_json)
# print(response.content)

img = Image.open(BytesIO(response.content))
# img = Image.open(BytesIO(url))
img.show()
# img = Image.open(BytesIO("https://cdn.pixabay.com/photo/2024/02/25/10/11/forsythia-8595521_150.jpg"))
# img = Image.open("https://cdn.pixabay.com/photo/2024/02/25/10/11/forsythia-8595521_150.jpg")