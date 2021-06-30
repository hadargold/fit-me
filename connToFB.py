import pyrebase
from Segmentation.cropImage import crop
from Segmentation.seg import segmentation
# https://github.com/Dirk-Sandberg/Pyrebase

config = {
    "apiKey": "AIzaSyAsczeUwUsZXin9LVHYP5kJpleg4K_ESPE",
    "authDomain": "final-project-95ac9.firebaseapp.com",
    "databaseURL" : "http://final-project-95ac9.firebaseapp.com",
    "projectId": "final-project-95ac9",
    "storageBucket": "final-project-95ac9.appspot.com",
    "messagingSenderId": "243981816200",
    "appId": "1:243981816200:web:728e448e45dfe56c15ea3d"
}

def download():
    firebase = pyrebase.initialize_app(config)
    storage = firebase.storage()

    path_on_cloud = "images/img.jpeg"
    path_local = "tryNew.jpg"
    # storage.child(path_on_cloud).put(path_local)

    storage.child(path_on_cloud).download("testImg.png")

    crop(path_local)

    return "'finalPic.png'"

