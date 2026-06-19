from apiflask.app import APIFlask
from app.api.blueprint import blueprint as api_blueprint
from app.api.errors import register_error_handlers

app = APIFlask(__name__)
app.register_blueprint(api_blueprint)
register_error_handlers(app)



if __name__ == "__main__":
    app.run(debug=True)