from flask import Blueprint, request, jsonify
from services.short_url_services import ShortURLService

short_url_bp = Blueprint('short_url', __name__)
service = ShortURLService()

@short_url_bp.route('/shorten/<short_code>', methods=['DELETE'])
def delete_short_url(short_code):
    result = service.delete_short_url(short_code)
    if result:
        return '', 204
    return jsonify({"error": "Short URL not found"}), 404

@short_url_bp.route('/shorten/<short_code>/stats', methods=['GET'])
def get_url_statistics(short_code):
    stats = service.get_statistics(short_code)
    if stats:
        return jsonify(stats), 200
    return jsonify({"error": "Short URL not found"}), 404
