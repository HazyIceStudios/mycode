#!/usr/bin/python3
import urllib.request
import json

## uncomment this import if you run in a GUI
## and want to open the URL in a browser
## import webbrowser

NASAAPI = "https://api.nasa.gov/planetary/apod?"

def main():
    ## Define credentials
    with open("/home/student/nasa.creds") as mycreds:
        nasacreds = mycreds.read()

    ## remove any extra lines from cred file
    nasacreds = "api_key=" + nasacreds.strip("\n")

    ## make a request using our key
    apodurlobj = urllib.request.urlopen(NASAAPI + nasacreds)

    ## read the file-like object
    apodread = apodurlobj.read()

    #decode (convert) the json to pythonic dictionary
    apod=json.loads(apodread.decode("utf-8"))

    ## display our pythonic data
    print("\n\nConverted Python data")
    print(apod)

    print()

    print(apod["title"] + "\n")

    print(apod["date"] + "\n")

    print(apod["explanation"] + "\n")

    print(apod["url"])

    ## Uncomment the code below if running in a GUI
    ## and you want to open the URL in a browser
    ## use Firefox to open the HTTPS URL
    ## input("\nPress Enter to open NASA Picture of the Day in Firefox")
    ## webbrowser.open(decodeapod["url"])



if __name__ == "__main__":
    main()








