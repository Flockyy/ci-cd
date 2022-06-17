from flask import Flask, jsonify, render_template

app = Flask(__name__, template_folder='templates')

usersList = ['Aaron', 'Bianca', 'Cat', 'Danny', 'Elena']

# @app.route('/')
# def index():
#     return render('Hello World')

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('base.html')

@app.route('/users', methods=['GET'])
def users():
    return jsonify({ 'users': [user for user in usersList] })

@app.route('/user/<int:id>', methods=['GET'])
def userById(id):
    return jsonify({ 'username': usersList[id]  })

@app.route('/user/<string:name>', methods=['GET'])
def getUserByName(name):
    # Show some user information
    return "Some info"

@app.route('/user/<string:name>', methods=['POST'])
def addUserByName(name):
    usersList.append(name)
    return jsonify({ 'message': 'New user added'  })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
    
#deploy push