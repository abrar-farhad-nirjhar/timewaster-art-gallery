from apiflask.app import APIFlask
from app.api.blueprint import blueprint as api_blueprint


app = APIFlask(__name__)
app.register_blueprint(api_blueprint)



if __name__ == "__main__":
    app.run(debug=True)