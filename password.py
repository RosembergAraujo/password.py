#coding utf-8
import json
import getpass


def write_Json(dados):
    with open('db.json', 'w', encoding='utf8') as f:
        json.dump(dados, f, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ':'))

def read_Json(arq_json):
    with open(arq_json, 'r', encoding='utf8') as f:
        return json.load(f)

def auth_Pass (iUser, iPass):
    data = read_Json('db.json')
    dataUsers = data['users']
    foundUser = False
    for key in dataUsers:
        if key["user"] == iUser:
            foundUser = True
            if key["pwd"] == iPass:
                print("\nACCESS GUARANTEED")
            else:
                print("\nWRONG PASSWORD => ACCESS DENIED")
            break
    if foundUser == False:
        willCreateNewUser = str(input("USER NOT FOUND DO YOU LIKE TO CREATE A NEW USER ?\n[Y/N] >> "))
        register_New_User() if willCreateNewUser in ['Y', 'y', 'yes'] else print("\nTHANK YOU!")


def register_New_User ():
    user = str(input("NEW LOGIN\n>> "))
    password = getpass.getpass(("NEW PASSWORD\n>> "))
    
    db = read_Json('db.json')
    try:
        lastDbId = db['users'][int(len(db['users']) - 1)]['id'] + 1 #take the ID of last element and reduce one
    except:
        lastDbId = 0
    db['users'].append({'id': lastDbId, 'user': user, 'pwd': password})
    
    write_Json(db)
    
def logIn ():
    inputUser = str(input("USER\n>> "))
    inputPass = getpass.getpass(("PASSWORD\n>> "))

    auth_Pass(inputUser, inputPass)
    

logIn()
