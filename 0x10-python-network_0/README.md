
URL (Uniform Resource Locator): A URL is a reference or address to a web resource that specifies its location on the internet. It typically consists of several components including the protocol (such as HTTP or HTTPS), domain name, path, query parameters, and fragment identifier.

HTTP (Hypertext Transfer Protocol): HTTP is an application protocol that governs the communication between web clients (such as browsers) and servers. It facilitates the transfer of hypertext, typically in the form of HTML documents, but it can be used for other purposes such as transferring images, videos, or data.

Reading a URL: A URL is typically divided into several parts:

Scheme: Indicates the protocol being used, such as HTTP or HTTPS.
Domain Name: The human-readable name that identifies a website, often preceded by www.
Subdomain: An optional part of the domain preceding the main domain.
Port Number: If specified, it follows the domain and is preceded by a colon (e.g., :8080).
Path: Specifies the specific resource or location within the website.
Query String: Contains parameters for a query, usually following a question mark (?).
Fragment Identifier: Specifies a specific section within the resource, preceded by a hash symbol (#).
Scheme for a HTTP URL: The scheme for an HTTP URL is typically "http://" for unencrypted connections or "https://" for encrypted connections (secured with SSL/TLS).

Domain Name: A domain name is the human-readable name that corresponds to a unique IP address on the internet. It serves as a mnemonic to easily locate resources on the web.

Subdomain: A subdomain is a subdivision of a domain. It allows for further organization and delegation of control within a domain. For example, in "subdomain.example.com," "subdomain" is the subdomain.

Port Number in a URL: A port number in a URL is specified after the domain name preceded by a colon. It indicates the specific network endpoint within the server to which the client should connect. If not specified, the default port for HTTP is 80 and for HTTPS is 443.

Query String: A query string is a part of a URL that follows the path and is preceded by a question mark (?). It contains key-value pairs used to pass data to the server for processing.

HTTP Request: An HTTP request is a message sent by a client (such as a web browser) to a server, requesting a specific action, usually to retrieve a resource identified by a URL.

HTTP Response: An HTTP response is a message sent by a server to a client in response to an HTTP request. It contains the requested resource or indicates the outcome of the requested action.

HTTP Headers: HTTP headers are additional pieces of information sent along with an HTTP request or response. They provide metadata about the message, such as the content type, encoding, caching directives, and cookies.

HTTP Message Body: The HTTP message body contains the payload of an HTTP request or response. It can include data such as HTML content, JSON data, or file attachments.

HTTP Request Method: An HTTP request method indicates the desired action to be performed on a resource. Common methods include GET (retrieve a resource), POST (submit data to be processed), PUT (update a resource), DELETE (remove a resource), etc.

HTTP Response Status Code: An HTTP response status code is a three-digit number sent by a server to indicate the outcome of an HTTP request. It categorizes responses into different classes (e.g., 2xx for successful responses, 4xx for client errors, 5xx for server errors).

HTTP Cookie: An HTTP cookie is a small piece of data sent from a website and stored on the user's computer by the web browser. Cookies are commonly used for session management, user authentication, and tracking user behavior.

Making a Request with cURL: cURL is a command-line tool for transferring data using various protocols, including HTTP. To make a request with cURL, you typically use the curl command followed by the URL and any additional options such as headers or request methods.

Typical Browser Behavior when Typing google.com: When you type "google.com" into your browser and press Enter, the browser initiates an HTTP request to the server hosting the Google website. The server then responds with the appropriate HTML content, which the browser renders, displaying the Google homepage to the user. Additionally, the server might set cookies or other HTTP headers as part of the response, and the browser may also cache certain resources for faster loading in subsequent visits.
