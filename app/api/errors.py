from pynamodb.exceptions import DoesNotExist

def register_error_handlers(app):
    @app.errorhandler(DoesNotExist)
    def handle_does_not_exist_error(error):
        return {
            "error": str(error),
        }, 404