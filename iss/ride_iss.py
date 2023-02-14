#!/usr/bin/python3
"""Alta3 Research - astros on ISS"""

import urllib.request
import json

MAJORTOM = "http://api.open-notify.org/astros.json"

def main():
    """reading json from api"""

    # call the api
    groundctrl = urllib.request.urlopen(MAJORTOM)

    # strip off attachment (JSON) and read it
    # the problem here is that it will read out as a string
    helmet = groundctrl.read()

    print(helmet)

    # this shouyld say bytes
    helmetson = json.loads(helmet.decode("utf-8"))

    # this should say dict
    print(type(helmet))
    print(type(helmetson))

    # this returns a LIST of the people on this ISS
    print(helmetson["people"])

    # list the FIRSTY astro in the list
    print(helmetson["people"][0])

    # list the LAST astro in the list
    print(helmetson["people"][-1])


    # display every item in a list
    for astro in helmetson["people"]:
        # display what astro is
        print(astro)

    # ME testing calling specific attributes from within a for loop
    for astro in helmetson["people"]:
        # display what astro is
        print(astro["name"],",", astro["craft"])

    # display every item in a list
    for astro in helmetson["people"]:
        # display ONLY the name value associated with astro
        print(astro["name"])




if __name__ == "__main__":
    main()
    
