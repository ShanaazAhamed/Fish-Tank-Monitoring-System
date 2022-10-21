import pyrebase

config = {"apiKey": "","authDomain": "","databaseURL": "","projectId": "","storageBucket": "","messagingSenderId": "","appId": ""
}

firebase = pyrebase.initialize_app(config)
database = firebase.database()

def fetch_to_firebase(db,data):
    database.child(db)
    database.set(data)
    
def get_tokens(db):
    tokens = database.child(db).get()
    all_tokens = []
    for token in tokens.each():
        all_tokens.append(token.val())
    return all_tokens

def feed_now(db):
    datas = database.child(db).get()
    for data in datas.each():
        if data.key() == "Feed Now":
            return data.val()
        
        
        
if __name__ == '__main__':
    fetch_to_firebase("Test DB",{"Key1":1})




