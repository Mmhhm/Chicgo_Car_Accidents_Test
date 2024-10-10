from flask import Blueprint

init_db_bp = Blueprint('init_db', __name__)

@init_db_bp.route('initdb', methods=["GET"])
def initdb():


















