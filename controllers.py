from flask import Flask, request, jsonify
from models import User  # Assuming User is a SQLAlchemy model for user data

app = Flask(__name__)

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])  # Assuming to_dict() serializes the user object

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify(user.to_dict())

if __name__ == '__main__':
    app.run(debug=True)
