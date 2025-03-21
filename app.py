from flask import Flask , jsonify , request
from models import User

app = Flask(__name__)

users = []

user_id_counter = 1

@app.route("/users", methods=["GET"])
def get_user():
    return jsonify([user.todict() for user in users])

@app.route("/users", methods=["POST"])
def add_user():
     global user_id_counter
     data = request.get_json()
     new_user = User(user_id_counter, data["name"], data["password"], data["email"])
     users.append(new_user)
     user_id_counter += 1
     return jsonify(new_user.todict()), 201 

if __name__ == "__main__":
    app.run(debug=True)