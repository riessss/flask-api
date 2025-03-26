from flask import jsonify

class InvalidAPIUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        super().__init__()
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


def register_error_hanlders(app):
    @app.errorhandler(400)
    def bad_request(e):
        return jsonify(error=str(e)), 400
    
    @app.errorhandler(404)
    def resource_not_found(e):
        return jsonify(error=str(e)), 404
    
    @app.errorhandler(InvalidAPIUsage)
    def invalid_api_usage(e):
        return jsonify(e.to_dict()), e.status_code
    
    @app.errorhandler(500)
    def server_error(e):
        return jsonify(error=str(e)), 500

    
