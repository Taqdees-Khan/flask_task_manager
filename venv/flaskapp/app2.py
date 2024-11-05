from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# List to store tasks
task_list = []
task_id_counter = 0

# Route to serve the index.html file
@app.route('/')
def home():
    return render_template('index.html')

# Route for viewing tasks (GET)
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(task_list)

# Route for adding tasks (POST)
# Route for adding tasks (POST)
@app.route('/tasks', methods=['POST'])
def add_task():
    global task_id_counter
    new_task = request.json
    if 'task' not in new_task:
        return jsonify({'error': 'Task description is required'}), 400
    new_task['id'] = task_id_counter
    task_list.append(new_task)
    task_id_counter += 1
    return jsonify(new_task), 201


# Route for deleting tasks (DELETE)
# Route for deleting tasks (DELETE)
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global task_list  # Ensure we're modifying the global task list
    for i, task in enumerate(task_list):
        if task['id'] == task_id:
            removed_task = task_list.pop(i)
            return jsonify(removed_task), 200
    return jsonify({'error': 'Task not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
