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
    print("\n" + "Enter Artist Name, Or Type Exit" + "\n")
    line = input()
    if line=="exit" or line=="Exit":
        break
    response = requests.get(URL + line + URL2)
    data = response.json()
    print("\n" + "Looking for Artist: " + line + " \n")
    with open("downloadLinks.txt", "a") as linkFile:
        if 'data' in data:
            for obj in data['data']:
                print("Found an artist! Is the Artist:" + "\n")
                print(obj['name'] + "\n")
                print("What you were looking for?" + "\n")
                print("Type y/n")
                yn = ""
                
                while True:
                    yn = input()
                    if yn=="y":
                        break
                    if yn=="n":
                        print("\n" + "Oh, uh damn, Deezer probably doesn't have that artist then. Sorry b.")
                        time.sleep(1)
                        print("Restarting..." + "\n" + "\n" + "\n")
                        time.sleep(1)
                        break
                    else:
                        print("\n" + "You Bum! Type either y or n!" + "\n")

                if yn=="n":
                    continue
                print("\n" + "Processing Now.." + " \n")
                time.sleep(1)
                print("Link that's being written: \n" + obj['link'])
                linkFile.write(obj['link'] + "\n")
                counter += 1
                print("\n" + "Processed " + str(counter) + " artists! \n" +"\n" + "\n" + "\n" + "\n")
                time.sleep(1)
                    
        else:
            print("Error: The Artist " + line + " wasn't found on Deezer. Or anything even remotely similar to where it just returned an error. What a bunch of fucking bullshit. \n")
            time.sleep(0.5)
            time.sleep(1)

print("\n" + "\n" + "\n" + "\n" + "All done! There were a total of " + str(counter) + " Artists processed! \n")
input("\n" + "Press Enter to Close...")
