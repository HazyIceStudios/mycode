#!/usr/bin/env python3
"""Star Wars API HTTP responce parsing"""

# import our requests - use to send HTTP requests

import requests

URL = "https://swapi.dev/api/people/1"

def main():
    """sending GET request, checking response"""

    #send a request to our SWAPI -- store a response in a "resp" object
    resp = requests.get(URL)
    print(resp)
    #what do we get back? what is the type of object => variable resp?
    print("This object class is: ", type(resp), "\n")

    #great! what can we do with the variable resp?
    print("Methods/Attributes include: ", dir(resp), "\n")
    
if __name__ == "__main__":
    main()



