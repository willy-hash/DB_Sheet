from flask import Blueprint, jsonify, request
from Queries.QueriesSheet import QueriesMain
from Utilities.Generate_uid import get_uid
import logging

main = Blueprint('main', __name__)

logger = logging.getLogger(__name__)

queryMain = QueriesMain()

@main.route('/', methods=["GET"])
def index():
    return jsonify({
        "Get Data" : "/data",
        "Add" : "/add",
        "Update" : "/update/<id>",
        "remove" : "/update/<id>"
    }), 200

#get all information of worksheet
@main.route('/data', methods=["GET"])
def get_data():

    try:
        values = queryMain.get_all()
        return jsonify(values), 200

    except Exception as e:
        logger.error("Error to get data " +str(e))
        return jsonify({"Error" : "To get data"}), 500

#Add new product to worksheet
@main.route('/add', methods=["POST"])
def add_new_product():

    try:
        image = request.form.get('image')
        name = request.form.get('name')
        uid = get_uid()

        if not image or not name or not uid:
            return jsonify ({"Error": "Missing data"}), 400

        newProduct = [name, image]
        success = queryMain.add(newProduct, uid)

        if success is not True:
            return jsonify ({"Added Product": False}), 500
        else:
            return jsonify({"Added Product": True}), 200

    except Exception as e:
        logger.error("Error to add product" + str(e))
        return jsonify ({"Error": "In add product"}), 500

#update product
@main.route('/update/<idProduct>', methods=["PUT"])
def update_product(idProduct):

    try:
        image = request.form.get('image')
        name = request.form.get('name')

        if not image or not name:
            return jsonify ({"Error": "Missing data"}), 400

        newValues = [name, image]
        success = queryMain.update(idProduct, newValues)

        if success is not True:
            return jsonify({"Updated Product": False}), 500
        else:
            return jsonify({"Updated Product": True}), 200

    except Exception as e:
        logger.error("Error to update product" + str(e))
        return jsonify({"Error": "In update product"}), 500

#remove product
@main.route('/remove/<idProduct>', methods=["DELETE"])
def remove_product(idProduct):

    try:
        success = queryMain.remove(idProduct)

        if success is not True:
            return jsonify({"Remove Product": False}), 500
        else:
            return jsonify({"Remove Product": True}), 200

    except Exception as e:
        logger.error("Error to remove product" + str(e))
        return jsonify({"Error": "In remove product"}), 500

