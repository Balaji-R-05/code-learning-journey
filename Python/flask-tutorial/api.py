from flask import Flask, request, jsonify

app = Flask(__name__)

items = [
    {"id": 1, "name": "Item1", "desc": "This is item 1"},
    {"id": 2, "name": "Item2", "desc": "This is item 2"}
]

@app.route("/")
def index():
    return "Sample TODO list"

@app.route('/items', methods=['GET'])
def getItems():
    return jsonify(items)

@app.route('/items/<int:id>', methods=["GET"])
def get_item(id):
    item = [item for item in items if item['id'] == id]
    if not item:
        return jsonify({"Error": "No item found"})
    return jsonify(item[0])

@app.route("/items", methods=["POST"])
def create_items():
    if not request.json or 'name' not in request.json:
        return jsonify({"Error": "Missing item name"})
    new_item = {
        "id": items[-1]["id"] + 1 if items else 1,
        "name": request.json['name'],
        "desc": request.json.get('desc', '')
    }
    items.append(new_item)
    return jsonify(new_item)

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_items(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        return jsonify({"Error": "Item not found"})
    item['name'] = request.json.get("name", item["name"])
    item['desc'] = request.json.get("desc", item["desc"])
    return jsonify(item)

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_items(item_id):
    global items
    items = [item for item in items if item["id"] != item_id]
    return jsonify({"Result": "Item Deleted"})

if __name__ == "__main__":
    app.run(debug=True)
