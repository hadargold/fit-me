
#performing flask imports
from flask import Flask,jsonify
import connToFB
import os
import requests


app = Flask(__name__) #intance of our flask application

#Route '/' to facilitate get request from our flutter app
@app.route('/', methods = ['GET'])
def index():
    url = connToFB.download()
    print(url)
    path = str(os.getcwd()) + "\\" + str(url)
    print(path)
    new_path = ("http://localhost:5005/process/" + path).replace("'", "")
    prediction = requests.get(new_path)
    # prediction = "Round"
    print(type(prediction))
    json_ans = prediction.json()
    print(json_ans)
    return json_ans
    #jsonify({'BODY TYPE': "prediction"}) #returning key-value pair in json format


if __name__ == "__main__":
    app.run(debug = True) #debug will allow changes without shutting down the server

