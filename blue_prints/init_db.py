from flask import Blueprint, jsonify
from repository.csv_repo import init_accidents_db
from database.config import locations, accidents, injuries

init_db_bp = Blueprint('init_db', __name__)

@init_db_bp.route('/initdb', methods=["GET"])
def initdb():
    init_accidents_db()
    return jsonify({'Success': 'Successfully initialized database!'})


















