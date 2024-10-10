from flask import Blueprint, jsonify
from service.blue_prints import accidents_by_location

accidents_bp = Blueprint('accidents_analyze', __name__)

@accidents_bp.route('/accidents/area/<location>', methods=['GET'])
def get_accidents(location):
    res = accidents_by_location(location)
    return jsonify({'accidents': res})

@accidents_bp.route('/accidents/area/int<location>/<period>', methods=['GET'])
def accidents_by_period(area,period):
    pass

@accidents_bp.route('/accidents/cause/int<location>', methods=['GET'])
def accidents_by_cause():
    pass

@accidents_bp.route('/accidents/stat/int<location>', methods=['GET'])
def accidents_stat():
    pass




