from flask import Blueprint, jsonify


bp = Blueprint('default', __name__)


@bp.route('/api')
def default():
    return jsonify({
        'msg': 'Hello from the Flask backend!',
        'status': 200
    })
