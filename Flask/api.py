from flask import Flask, render_template, request, jsonify
app = Flask(__name__)



# Items list
items = [
    {
        'id': 1,
        'title': 'Item 1',
        'description': 'This is item 1.'
    },
    {
        'id': 2,
        'title': 'Item 2',
        'description': 'This is item 2.'
    }
]

@app.route('/')
def welcome():
    return "Welcome to the Sample To Do Application made using Flask."


# GET: Retrieve all the items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

# GET: Retrieve a specific item by id
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id) :
    item = [item for item in items if item['id'] == item_id]
    if len(item) == 0:
        return "Item not found."
    return jsonify(item)

# POST: Add a new item -- API 
@app.route('/items', methods=['POST'])
def add_item():
    item = {
        'id': items[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json['description']
    }
    items.append(item)
    return jsonify(item)
    if not request.json or not 'title' in request.json:
        return "Bad Request", 400


# PUT: Update an existing item by id 
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = [item for item in items if item['id'] == item_id]
    if len(item) == 0:
        return "Item not found."
    item['title'] = request.json.get('title', item['title'])
    item['description'] = request.json.get('description', item['description'])
    return jsonify(item) 

# Here, the PUT method is used to update the item by id.
# The item is retrieved by the id from the items list.
# The item is updated with the new title and description. (with the help of request.json.get() method)
# The updated item is returned as a response.


# DELETE: Delete an existing item by id
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = [item for item in items if item['id'] == item_id]
    if len(item) == 0:
        return "Item not found."
    items.remove(item)
    return jsonify(items)




if __name__=="__main__":
    app.run(debug=True)