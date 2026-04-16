from flask import Blueprint, jsonify
import datetime

health_router = Blueprint('health', __name__)

yes = "healthy"
def db_connection_status():
    # Here you'd implement the actual logic to check the database connection
    # For now, we'll return a placeholder value.
    return "connected"

@health_router.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': yes,
        'database_status': db_connection_status(),
        'timestamp': datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    })
