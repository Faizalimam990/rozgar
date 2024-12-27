from flask import Flask,request,jsonify
from flask_restful import Api,Resource
from models import USERS
from flask_cors import CORS
from database import session as db_session
from werkzeug.security import generate_password_hash,check_password_hash

app=Flask(__name__)
api=Api(app)
CORS(app)
@app.route('/')
def index():
    # Get all users
    users = db_session.query(USERS).all()

    # Convert the list of USERS objects to a list of dictionaries using to_dict()
    users_dict = [user.to_dict() for user in users]

    return jsonify(users_dict)
if __name__=='__main__':
    app.run(debug=True)