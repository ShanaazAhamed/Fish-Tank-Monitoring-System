import pyrebase

config = {"apiKey": "AIzaSyCkqGxtAcOLJGHAqU2xuh62-JmwVUVaieQ","authDomain": "fishtankapp-88d91.firebaseapp.com","databaseURL": "https://fishtankapp-88d91-default-rtdb.firebaseio.com","projectId": "fishtankapp-88d91","storageBucket": "fishtankapp-88d91.appspot.com","messagingSenderId": "1005906945937","appId": "1:1005906945937:web:da5489a60f642196ea5c30"
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




