import requests


"""
    http_request_get(url)
    
    :param url
        endpoint with want to access
        
    Makes a http request to a endpoint and prints it's json response status_code, headers, encoding, text, json
"""
def http_request_get(url):
    request = requests.get(url)
    print request.status_code
    print request.headers['content-type']
    print request.encoding
    print request.text
    print request.json()

http_request_get('https://swapi.co/api/people/1/')
