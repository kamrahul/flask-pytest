from flask import Blueprint, request, jsonify,current_app
#from run import mqtt_client
import os


# setting up blueprint
test_blueprint= Blueprint('dummy_module',__name__,url_prefix='/dummy_module')





@test_blueprint.route('/print', methods=['GET'])
def print_message():
    print("MESSAGE RECEIVED",flush=True)
    return jsonify({})



@test_blueprint.route('/notCovered', methods=['GET'])
def print_message_test():
    print("MESSAGE RECEIVED",flush=True)
    return jsonify({})

