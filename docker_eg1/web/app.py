from flask import Flask, jsonify,request
from flask_restful import Api,Resource

app = Flask(__name__)


#Create a Restful API

api = Api(app)


def checkPostedData(postDict,function_name):
    if (function_name == "add" or function_name == "sub" or function_name == "mul"):
        if "x" not in postDict or "y" not in postDict:
            return 300
        else:
            return 200
    elif function_name == "div":
        if "x" not in postDict or "y" not in postDict:
            return 300
        elif int(postDict["y"]) == 0:
            return 301
        else:
            return 200

#Add the resource 
class Add(Resource):
    #POST Method
    def post(self):
        postDict = request.get_json()
        status_code = checkPostedData(postDict, "add")
        if status_code != 200:
            retJson = {"Message": "Error Occured",
                       "Status Code":status_code}
            return jsonify(retJson)
        
        x = postDict['x']
        y = postDict['y']
        z = x + y
        retJson = {"Message": z,
                   "Status Code":status_code}
        return jsonify(retJson)


class Subtract(Resource):
        #POST Method
    def post(self):
        postDict = request.get_json()
        status_code = checkPostedData(postDict, "sub")
        if status_code != 200:
            retJson = {"Message": "Error Occured",
                       "Status Code":status_code}
            return jsonify(retJson)
        
        x = postDict['x']
        y = postDict['y']
        z = x - y
        retJson = {"Message": z,
                   "Status Code":status_code}
        return jsonify(retJson)

class multiply(Resource):
        #POST Method
    def post(self):
        postDict = request.get_json()
        status_code = checkPostedData(postDict, "mul")
        if status_code != 200:
            retJson = {"Message": "Error Occured",
                       "Status Code":status_code}
            return jsonify(retJson)
        
        x = postDict['x']
        y = postDict['y']
        z = x * y
        retJson = {"Message": z,
                   "Status Code":status_code}
        return jsonify(retJson)

class Divide(Resource):
        #POST Method
    def post(self):
        postDict = request.get_json()
        status_code = checkPostedData(postDict, "div")
        if status_code != 200:
            retJson = {"Message": "Error Occured",
                       "Status Code":status_code}
            return jsonify(retJson)
        
        x = postDict['x']
        y = postDict['y']
        z = x / y
        retJson = {"Message": z,
                   "Status Code":status_code}
        return jsonify(retJson)

#Add the class resource and endpoint
api.add_resource(Add, '/add')
api.add_resource(Subtract, '/sub')
api.add_resource(multiply, '/mul')
api.add_resource(Divide, '/div')


#Example of defining a endpoints
@app.route('/')
def hello_world():
    return "Hello World"

@app.route('/bye')
def bye():
    return "Bye"


#Example of sending a JSON program
@app.route('/json1')
def json_file():
    retJson = {"field1":"abc",
               "field2":"ddd"}
    return jsonify(retJson)



#Example for using post method
@app.route('/add_two_nums',methods=['POST'])
def add_two_nums():
    dataDict = request.get_json()

    x = dataDict["x"]
    y = dataDict["y"]
    z = x + y

    retJson = { "z" : z,
               "status": 200}
    return jsonify(retJson)




if __name__ =="__main__":
    app.run(host='0.0.0.0')