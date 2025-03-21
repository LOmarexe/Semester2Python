from flask import Flask , jsonify , request
from models import User

app = Flask(__name__)

users = []

user_id_counter = 1

@app.route("/users", methods=["GET"])
def get_user():
<<<<<<< HEAD
    return jsonify([user.to_dict() for user in users])
=======
    return jsonify([user.todict() for user in users])
>>>>>>> f24dfc903eef70c01891381e2390b0cb250793e1

@app.route("/users", methods=["POST"])
def add_user():
     global user_id_counter
     data = request.get_json()
     new_user = User(user_id_counter, data["name"], data["password"], data["email"])
     users.append(new_user)
     user_id_counter += 1
<<<<<<< HEAD
     return jsonify(new_user.to_dict()), 201 
=======
     return jsonify(new_user.todict()), 201 
>>>>>>> f24dfc903eef70c01891381e2390b0cb250793e1

if __name__ == "__main__":
    app.run(debug=True)