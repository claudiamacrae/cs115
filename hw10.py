DICTFILE = 'musicrecplus.txt'

def loadUsers(fileName):
    try:
        file = open(fileName , 'r')
        userDict = {}
        for line in file:
            [userName, artists] = line.strip().split(':')
            artistList = artists.split(',')
            userDict[userName] = artistList
        file.close()
        return userDict
    except:
        return {}

def enterPrefs(userName, userDict):
    prefs = []
    newPref = input('Enter an artist that you like ( Enter to finish ): ')
    while newPref != '':
        prefs += [newPref.title()]
        newPref = input('Enter an artist that you like ( Enter to finish ): ')
    prefs.sort()
    userDict[userName] = prefs
    return userDict

def getRecs(userName, userDict):
    userPicks = userDict[userName]
    bestUser = findBestFriend(userName, userDict)
    if bestUser == None:
        print('No recommendations available at this time .')
        return
    for artist in userDict[bestUser]:
        if artist not in userPicks:
            print(artist)
            
def findBestFriend(userName, userDict):
    bestFriend = None
    topScore = 0
    for friend in userDict:
        userDict[friend]
        if friend[:-1] != '$' and userDict[friend] != userDict[userName]:   #skip private and identical users
            score = numMatches(userDict[friend], userDict[userName])
            if score > topScore:
                bestFriend, topScore = friend, score
    return bestFriend
    
def numMatches(L,M):
    '''Assuming L and M are sorted lists without duplicates, return number of common elements'''
    count = 0
    i = 0
    j = 0
    # Invariant: count == number of matches between L[:i] and M[:j]
    while i < len(L) and j < len(M):
        if L[i]==M[j]:
            count += 1
            i += 1
            j += 1
        elif L[i] < M[j]:
            i += 1
        else:
            j += 1
    return count

def artistCount(userDict):
    '''returns dictionary of artists and the count of times they appear in any any users
        preferences'''
    result = {}
    for user in userDict:
        for artist in userDict[user]:
            if artist in result:
                result[artist] += 1
            else:
                result[artist] = 1
    return result

def greatestKeyOfDict(d):
    '''assumes d has at least 1 element'''
    best = -1
    bestKey = None
    for key in d:
        if d[key] > best:
            bestKey = key
            best = d[key]
    return bestKey

def greatestElementOfDict(d):
    '''assumes d has at least 1 element'''
    best = -1
    for key in d:
        if d[key] > best: best = d[key]
    return best

def save(fileName, userDict):
    '''saves dictionary userDict to musicrecplus.txt'''
    try:
        file = open(fileName , 'w')
    except:
        file = open(fileName , 'w+')
    for user in userDict:
        toSave = str(user) + ':' + ','.join(userDict[user]) + '\n'
        file.write(toSave)
    file.close()
    
def longestElement(d):
    length = -1
    longKey = None
    for key in d:
        if len(d[key]) > length:
            longKey = key
            length = len(d[key])
    return longKey
    
def main():
    userDict = loadUsers(DICTFILE)  #load dictionary
    userName = input('"Enter your name ( put a $ symbol after your \
name if you wish your preferences to remain private ): ')
    if userName not in userDict:
        userDict = enterPrefs(userName, userDict)
    status = True
    while status == True:
        action = input('Enter a letter to choose an option :\
                        \n e - Enter preferences\
                        \n r - Get recommendations\
                        \n p - Show most popular artists\
                        \n h - How popular is the most popular\
                        \n m - Which user has the most likes\
                        \n q - Save and quit \n')
        if action == 'e':
            userDict = enterPrefs(userName, userDict)
        elif action == 'r':
            getRecs(userName, userDict)
        elif action == 'p':
            print(greatestKeyOfDict(artistCount(userDict))) 
        elif action == 'h':
            print(greatestElementOfDict(artistCount(userDict)))
        elif action == 'm':
            print(longestElement(userDict))
        elif action == 'q':
            save(DICTFILE, userDict)
            status = False
