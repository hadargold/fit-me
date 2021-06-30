
#performing flask imports
from flask import Flask,jsonify
import shape


app = Flask(__name__) #intance of our flask application

#Route '/' to facilitate get request from our flutter app
@app.route('/', methods = ['GET'])
def index():
    f = open("pred.txt", "r")
    prediction = f.read()
    return jsonify({'BODY TYPE': prediction}) #returning key-value pair in json format


@app.route('/process/<url>', methods = ['GET'])
def process(url):
    # img = cv2.imread(url)
    print(url)
    prediction = shape.process("predict", url, 20, False)
    print prediction
    return jsonify({'BODY TYPE': prediction})  # returning key-value pair in json format


if __name__ == "__main__":
    app.run(debug = True, port=5005) #debug will allow changes without shutting down the server

