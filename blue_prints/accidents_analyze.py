from flask import Blueprint

accidents_bp = Blueprint('accidents_analyze', __name__)

@accidents_bp.route('/accidents/area/int<location>', methods=['GET'])
def get_accidents(area):
    pass

@accidents_bp.route('/accidents/area/int<location>/<period>', methods=['GET'])
def accidents_by_period(area,period):
    pass

@accidents_bp.route('/accidents/cause/int<location>', methods=['GET'])
def accidents_by_cause():
    pass

@accidents_bp.route('/accidents/stat/int<location>', methods=['GET'])
def accidents_stat():
    pass




