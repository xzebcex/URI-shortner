# URI_shortner
import requests


def shorten_uri(uri):
    # Make a request to the TinyURL API to shorten the URL
    response = requests.get(f'http://tinyurl.com/api-create.php?url={uri}')

    return response.text  # Return the shortened URL


# Test the uri_shortner
print(shorten_uri(input('Enter uri: ')))
