#
# Example file for parsing and processing JSON
#

import urllib.request
import json

def printResults(data):
    #Use the json module to load the string data into a directory
    theJSON = json.loads(data.decode('utf-8'))

    if "title" in theJSON["metadata"]:
        print("Title : " + theJSON["metadata"]["title"] + "\r\n")

    count = theJSON["metadata"]["count"]
    print(str(count) + " Events recoreded")



def main():
    #Define a variable to hold the source url
    # In this case we'll use the free data feed from the UGGS
    # This feed lists all the earthquakes for the last day Significant Earthquakes
    urlData = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_day.geojson"

    #Open the url and read the data
    webUrl = urllib.request.urlopen(urlData)
    print("Result code : " + str(webUrl.getcode()))
    if (webUrl.getcode() == 200 ) : 
        data = webUrl.read()
        printResults(data)
    else :
        print("Recevied error, cannot parse result")



if __name__ == "__main__":
    main()