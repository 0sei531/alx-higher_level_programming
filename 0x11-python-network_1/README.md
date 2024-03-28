Fetching Internet Resources with urllib:
Fetching a Resource:

python
Copy code
import urllib.request

url = 'http://example.com/resource'
with urllib.request.urlopen(url) as response:
    data = response.read()
Decoding Response Body:

python
Copy code
decoded_data = data.decode('utf-8')  # Assuming UTF-8 encoding
Fetching Internet Resources with requests:
Installing requests:
You need to install it first using pip:

Copy code
pip install requests
Fetching a Resource:

python
Copy code
import requests

url = 'http://example.com/resource'
response = requests.get(url)
data = response.text  # or response.content for binary data
Fetching JSON Resources:

python
Copy code
json_data = response.json()
Making HTTP GET Requests:
Both urllib and requests use the same approach for GET requests:

urllib:

python
Copy code
import urllib.request

url = 'http://example.com/resource'
with urllib.request.urlopen(url) as response:
    data = response.read()
requests:

python
Copy code
import requests

url = 'http://example.com/resource'
response = requests.get(url)
data = response.text  # or response.content for binary data
Making HTTP POST/PUT/etc. Requests:
For non-GET requests, you'll need to specify the HTTP method and potentially include data or parameters.

requests Example for POST:

python
Copy code
import requests

url = 'http://example.com/post_endpoint'
payload = {'key': 'value'}
response = requests.post(url, data=payload)
requests Example for PUT:

python
Copy code
import requests

url = 'http://example.com/put_endpoint'
payload = {'key': 'updated_value'}
response = requests.put(url, data=payload)
Manipulating Data from an External Service:
Once you've fetched data from an external service (either with urllib or requests), you can manipulate it as needed in Python. This might involve parsing JSON, extracting relevant information, performing calculations, etc.

Example Manipulation of JSON Data:
python
Copy code
json_data = response.json()
# Manipulate JSON data as needed
Remember to handle errors gracefully, especially when making network requests, by utilizing exception handling constructs like try and except.
