#coding utf-8
import json
import getpass


def write_Json(dados):
    with open('db.json', 'w', encoding='utf8') as f:
        json.dump(dados, f, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ':'))

def read_Json(_jasonFile):
    with open(_jasonFile, 'r', encoding='utf8') as f:
        return json.load(f)

def auth_User(_user):
    data = read_Json('db.json')
    dataUsers = data['users']
    for key in dataUsers:
        if key['user'] == _user:
            return {'user': _user,'id': key['id'], 'pos': dataUsers.index(key), 'auth': True}    
    return {'user': _user, 'auth': False}

def auth_Pass(_user, _pass):
    data = read_Json('db.json')
    auth = auth_User(_user)
    if data['users'][auth['pos']]['pwd'] == _pass:
        return True
    return False

def register_New_User():
    user = str(input('\nNEW LOGIN\n>> '))
    password = getpass.getpass(('\nNEW PASSWORD\n>> '))
    
    data = read_Json('db.json')
    try:
        #lastDbId = data['users'][int(len(data['users']) - 1)]['id'] + 1 #take the ID of last element and reduce one
        lastDbId = data['lastId'] + 1
    except:
        lastDbId = 0
    data['users'].append({'id': lastDbId, 'user': user, 'pwd': password})
    data['lastId'] = lastDbId
    
    write_Json(data)
    
def login ():
    _user = str(input('\nUSER\n>> '))
    _pass = getpass.getpass(('\nPASSWORD\n>> '))
    
    if auth_User(_user)['auth']:
        if auth_Pass(_user, _pass):
            print('\nEVERYTHING OK!')
        else:
            print('\nWRONG PASSWORD!')
    else:
        willCreateNewUser = str(input('USER NOT FOUND DO YOU LIKE TO CREATE A NEW USER ?\n[Y/N] >> '))
        register_New_User() if willCreateNewUser in ['Y', 'y', 'yes'] else print('\nTHANK YOU!')
    
def delete_User(_user):
    data = read_Json('db.json')
    _pass = getpass.getpass(('\nPASSWORD\n>> '))
    if auth_Pass(_user,_pass):
        del(data['users'][auth_User(_user)['pos']])
        write_Json(data)
        print('\n')
    else:
        print('\nWRONG PASSWORD!')
    
    
login()
# register_New_User()
# delete_User('user_here')