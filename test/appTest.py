from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS, cross_origin
import logging

app = Flask(__name__, static_folder='.')

logging.basicConfig(level=logging.DEBUG)
app.logger.setLevel(logging.DEBUG)
#CORS(app, resources={r"/*": {"origins": "*"}})

# Sample data: list of pets
pets = [
    {"id": 1, "name": "Fluffy", "species": "Cat"},
    {"id": 2, "name": "Rex", "species": "Dog"}
]


@app.route("/pets", methods=["GET"])
def get_pets():
    return jsonify(pets)


@app.route("/pets/<int:pet_id>", methods=["GET"])
def get_pet(pet_id):
    pet = next((pet for pet in pets if pet["id"] == pet_id), None)
    if pet:
        return jsonify(pet)
    else:
        return jsonify({"error": "Pet not found"}), 404


@app.route("/pets/", methods=["POST"])
def create_pet():
    data = request.get_json()
    if not data or "name" not in data or "species" not in data:
        return jsonify({"error": "Invalid data"}), 400
    pet = {
        "id": len(pets) + 1,
        "name": data["name"],
        "species": data["species"]
    }
    pets.append(pet)
    return jsonify(pet), 201


@app.route("/pets/<int:pet_id>/", methods=["DELETE"])
def delete_pet(pet_id):
    global pets
    pets = [pet for pet in pets if pet["id"] != pet_id]
    return jsonify({"message": f"Pet with ID {pet_id} deleted successfully"})


@app.route("/")
def serve_frontend():
    return send_from_directory('.', 'indexTest.html')


@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('.', filename)


if __name__ == "__main__":
    app.run(debug=True, port=8000)
