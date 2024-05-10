import json, requests

headers = {
        "X-RapidAPI-Key": "f83e32ba4dmsh9e258aa66e87ac5p1cedb2jsn6d976f8f26bc",
        "X-RapidAPI-Host": "streaming-availability.p.rapidapi.com"
    }

def saveFile():
    f = open('streamingApi/users.json', "w")
    json.dump(userJsonData, f, indent=4)
    f.close()

def selectUser():
    for idx,i in enumerate(userJsonData["user"]):
        print(str(idx+1), ":", i["userName"])
    userSelection = int(input("Which user would you like to select?"))
    global currentUser
    currentUser = userJsonData["user"][userSelection-1]
    movieLoop(False)
    

def guest():
    pass

def addNewUser():
    print("Enter your username: ")
    newUser = str(input())
    newUserJsonString = {"userName" : newUser, "movieList" : []}
    userJsonData["user"].append(newUserJsonString)
    

def importUserJson():
    f = open('streamingApi/users.json')
    global userJsonData
    userJsonData = json.load(f)
    f.close()

def addToList():
    pass

def apiSearch(searchString):
    url = "https://streaming-availability.p.rapidapi.com/shows/search/title"

    querystring = {"country":"us","title": searchString,"output_language":"en","show_type":"movie","series_granularity":"show"}
    
    response = requests.get(url, headers=headers, params=querystring)

    searchReturn = (response.json()[0]["title"], response.json()[0]["rating"])

    return searchReturn

def movieLoop(asGuest):
    while True:
        while True:
            print("Would you like to look for a movie(1) or exit(2)?")
            cont = int(input())
            if cont == 2:
                return 0
            print("Enter the title of the movie you are looking for: ")
            searchString = input()
            searchResults = apiSearch(searchString)
            print(searchResults)
            if not asGuest:
                print("Would you like to save this movie to your list?")
                print("1. Yes")
                print("2. No")
                saveSelection = int(input())
                if saveSelection == 1:
                    addToList()


    



    
def main():
     
    importUserJson()

    print(userJsonData)

    while True:
        print("Welcome to our streaming availability platform! \n What would you like to do?")
        print("1: Select User")
        print("2: Continue as Guest")
        print("3: Add new User")
        print("4: About")
        print("5: Exit")
        userInput = int(input())
        
        if userInput == 1:
            selectUser()
        
        elif userInput == 2:
            print("By browsing as guest, you are not allowed to add films to a list.")
            movieLoop(True)
        
        elif userInput == 3:
            addNewUser()
        
        elif userInput == 4:
            print("Selecting an account will allow you to save movies and shows to your list")
        
        elif userInput == 5:
            return 0
        
        else:
            return 0
        saveFile()
    
if __name__ == "__main__" : 
    main()