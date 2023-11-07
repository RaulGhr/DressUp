import requests
import base64
from PIL import Image

base = 'http://127.0.0.1:5000/'

while True:
    print("1.Delete Clothing by ID")
    print("2.Delete Clothing by Tip")
    print("3.Delete Outfit by ID")
    print("4.Delete Outfit by Tip")
    caz = int(input("Selecteaza:"))

    if caz == 1:
        idClothing = int(input("id: "))
        response = requests.delete(base + "clothing", json={'id': idClothing})
        print(response)

    elif caz == 2:
        tipClothing = input("tip: ")
        response = requests.delete(base + "clothing", json={'tip': tipClothing})
        print(response)

    elif caz == 3:
        idOutfit = int(input("id: "))
        response = requests.delete(base + "outfit", json={'id': idOutfit})
        print(response)

    elif caz == 4:
        idOutfit = input("tip: ")
        response = requests.delete(base + "outfit", json={'tip': idOutfit})
        print(response)

