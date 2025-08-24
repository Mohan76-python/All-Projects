from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory "database" of users
users = []

# Route to get all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# Route to add a new user
@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    user = {
        'id': len(users) + 1,
        'name': data.get('name'),
        'email': data.get('email')
    }
    users.append(user)
    return jsonify(user), 201

# Route to get a user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
