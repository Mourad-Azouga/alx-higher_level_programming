# Python Networking
## Made by AZOUGA Mourad

### Glossary
	.Uniform Resource Locator (URL) - is used to identify resources over the web.
	.HyperText Transfer Protocol (HTTP) - asymmetric request-response client-server protocol, it is a stateless protocol which means the current request doesn't know what has been done in the previous requests.
	.Transmission Control Protocol / Internet Protocol (TCP/IP) - is a set of transport and network-layer protocols for machines to communicate with each other over the network.
	.IP (Internet Protocol) - is a network-layer protocol, deals with network addressing and routing. In an IP network, each machine is assigned an unique IP address (e.g., 165.1.2.3), and the IP software is responsible for routing a message from the source IP to the destination IP.
	.TCP (Transmission Control Protocol) - is a transport-layer protocol, responsible for establish a connection between two machines. TCP consists of 2 protocols: TCP and UDP (User Datagram Package).  TCP is reliable, each packet has a sequence number, and an acknowledgement is expected.  A packet will be re-transmitted if it is not received by the receiver.  Packet delivery is guaranteed in TCP.
	.Query string - A query string is a part of a uniform resource locator (URL) that assigns values to specified parameters. A query string commonly includes fields added to a base URL by a Web browser or other client application, for example as part of an HTML document, choosing the appearance of a page, or jumping to positions in multimedia content.

### HTTP Request Message

-Request Line
The first line of the header is called the request line, followed by optional request headers.

The request line has the following syntax:

	.request-method-name request-URI HTTP-version
	.request-method-name: HTTP protocol defines a set of request methods, e.g., GET, POST, HEAD, and OPTIONS. The client can use one of these methods to send a request to the server.
	.request-URI: specifies the resource requested.
	.HTTP-version: Two versions are currently in use: HTTP/1.0 and HTTP/1.1.
Examples of request line are:

GET /test.html HTTP/1.1
HEAD /query.html HTTP/1.0
POST /index.html HTTP/1.1

-Request Headers
The request headers are in the form of name:value pairs. Multiple values, separated by commas, can be specified.

request-header-name: request-header-value1, request-header-value2, ...
Examples of request headers are:

Host: www.xyz.com
Connection: Keep-Alive
Accept: image/gif, image/jpeg, */*
Accept-Language: us-en, fr, cn

-Response Headers
The response headers are in the form name:value pairs:

response-header-name: response-header-value1, response-header-value2, ...
Examples of response headers are:

Content-Type: text/html
Content-Length: 35
Connection: Keep-Alive
Keep-Alive: timeout=15, max=100

### HTTP Request Methods
HTTP protocol defines a set of request methods. A client can use one of these request methods to send a request message to an HTTP server. The methods are:

GET: A client can use the GET request to get a web resource from the server.
HEAD: A client can use the HEAD request to get the header that a GET request would have obtained. Since the header contains the last-modified date of the data, this can be used to check against the local cache copy.
POST: Used to post data up to the web server.
PUT: Ask the server to store the data.
DELETE: Ask the server to delete the data.
TRACE: Ask the server to return a diagnostic trace of the actions it takes.
OPTIONS: Ask the server to return the list of request methods it supports.
CONNECT: Used to tell a proxy to make a connection to another host and simply reply the content, without attempting to parse or cache it. This is often used to make SSL connection through the proxy.
Other extension methods.

### HTTP Cookies
	.An HTTP cookie (web cookie, browser cookie) - is a small piece of data that a server sends to a user's web browser. The browser may store the cookie and send it back to the same server with later requests. Typically, an HTTP cookie is used to tell if two requests come from the same browser—keeping a user logged in, for example. It remembers stateful information for the stateless HTTP protocol

### General Informations
	.When an HTTP response indicates a redirection, which header defines the URL the client should be redirected to? 
	->Location
	.What is the name of the HTTP request header that defines the size (in bytes) of the message body?
	->Content-Length
	.What is the curl option to disable the progression display?
	->-s or --silent
	.Which HTTP request header indicates the browser used by the client sending the request?
	->User-Agent
	.What is the name of the HTTP response header used to define the formatting of the body? (This header gives details to the client on how to interpret the data received.)
	->Content-Type
	.What is the curl option to set a cookie with a key-value pair?
	->-b or --cookie
	.What is the curl option to save the body of the resulting response to a file?
	->-o or --output
	.curl -sI is a silent HEAD request to retrieve the headers of a resource without the actual content.
	.curl -sX is used for sending silent requests with a custom HTTP method.
	.curl -d is used to include data in the request BODY.
	.curl -H to add customer HEADERS to the request

