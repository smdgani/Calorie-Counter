from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# In-memory database for simplicity. In a real app, use a database.
users = {}

# API endpoint to add a new food item with its calorie count
@cross_origin()
@app.route('/add_food', methods=['POST'])
def add_food():
    data = request.json

    user_id = data['user_id']
    food_name = data['food_name']
    calories = data['calories']

    if user_id not in users:
        users[user_id] = {'total_calories': 0, 'foods': []}

    users[user_id]['total_calories'] += calories
    users[user_id]['foods'].append({'food_name': food_name, 'calories': calories})

    return jsonify({'message': 'Food added successfully'})

# API endpoint to get the total calorie count for a user
@app.route('/get_total_calories/<user_id>', methods=['GET'])
def get_total_calories(user_id):
    if user_id in users:
        total_calories = users[user_id]['total_calories']
        return jsonify({'total_calories': total_calories})
    else:
        return jsonify({'error': 'User not found'}), 404

# API endpoint to get the list of foods and their calorie counts for a user
@app.route('/get_foods/<user_id>', methods=['GET'])
def get_foods(user_id):
    if user_id in users:
        foods = users[user_id]['foods']
        return jsonify({'foods': foods})
    else:
        return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)