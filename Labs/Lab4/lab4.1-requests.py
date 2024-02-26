

from xml.dom.minidom import Identified
import requests
import json 

#url = "http://google.com"
#response = requests.get(url)
#print (response.text)

URL = "http://andrewbeatty1.pythonanywhere.com/books"
response = requests.get(URL)
# print (response.json())

def readbooks():
    response = requests.get(URL)
    # we could do checking for correct response code here
    return response.json()

#if __name__ == "__main__":
 # print(readbooks())


def readbook(id):
    geturl = URL + "/" + str(id)
    response = requests.get(geturl)
    # we could do checking for correct response code here
    return response.json()
# print(readbook(524))

def createbook(book):
    book = {
        'Autor': 'Hemingway',
        'Title': 'The old Man and the Sea',
        'Price': 4000
    }
    response = requests.post(URL, json=book)
    # should check we have the correct status code
    return response.json()

print(createbook({}))