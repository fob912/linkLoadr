#!/usr/bin/env python3

# Library Imports
import requests
import json
import time

# API URLS
URL = "https://api.deezer.com/search/artist/?q="
URL2 = "&index=0&limit=1&output=json"

#COUNTER
counter = 0

while True:
    print("\nEnter Artist Name, Or Type Exit\n")
    line = input()
    
    if line == "exit" or line == "Exit":
        break
    response = requests.get(URL + line + URL2)
    data = response.json()
    print("\nLooking for Artist: " + line + " \n")
    
    with open("downloadLinks.txt", "a") as linkFile:
        if 'data' in data:
            for obj in data['data']:
                print("Found an artist! Is the Artist:" + "\n")
                print(obj['name'] + "\n")
                print("What you were looking for?\n")
                print("Type y/n")
                yn = ""
                
                while True:
                    yn = input()
                    if yn == "y":
                        break
                        
                    if yn == "n":
                        print("\n" + "Oh, uh damn, Deezer probably doesn't have that artist then. Sorry b.")
                        time.sleep(1)
                        print("Restarting...\n\n\n")
                        time.sleep(1)
                        break
                        
                    else:
                        print("\nYou Bum! Type either y or n!\n")

                if yn=="n":
                    continue
                    
                print("\nProcessing Now...\n")
                time.sleep(1)
                print("Link that's being written: \n" + obj['link'])
                linkFile.write(obj['link'] + "\n")
                counter += 1
                print("\nProcessed " + str(counter) + " artists! \n\n\n\n\n")
                time.sleep(1)
                    
        else:
            print("Error: The Artist " + line + " wasn't found on Deezer. Or anything even remotely similar to where it just returned an error. What a bunch of fucking bullshit. \n")
            time.sleep(0.5)
            time.sleep(1)

print("\n\n\n\nAll done! There were a total of " + str(counter) + " Artists processed! \n")
input("\nPress <Enter> to Close...")
