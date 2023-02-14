#!/usr/bin/python3
"""tracking the iss using api.open-notify.org/astros.json | Alta3 Research"""

# notice we no longer need to import urllib.request or json
import requests

## Define URL
MAJORTOM = 'http://api.open-notify.org/astros.json'

def main():
    """runtime code"""

    ## Call the webservice
    groundctrl = requests.get(MAJORTOM)

    # send a post with requests.post()
    # send a put with requests.put()
    # send a delete with requests.delete()
    # send a head with requests.head()


    ## strip the json off the 200 that was returned by our APO
    ## translate the json into python lists and dictionaries
    helmetson = groundctrl.json()

    ## display our pythonic data
    print("\n\nConverted Python Data")
    print(helmetson)
    
    print('\n\nPeople in Space: ', helmetson['number'])
    people = helmetson['people']
    # print(people)

    for astros in people:
        print(astros["name"], " on the ", astros["craft"])


#    for astros in helmetson['peope']:
#        print(astros)


if __name__ == "__main__":
    main()
