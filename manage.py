from flask_cors import CORS

from app import blueprint
from app.main import create_app


app = create_app()
CORS(app, resources={r"/": {"origins": "*"}})

app.register_blueprint(blueprint)
app.app_context().push()

if __name__ == "__main__":
    app.run(host="0.0.0.0")
