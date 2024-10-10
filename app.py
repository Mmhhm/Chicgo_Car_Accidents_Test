from flask import Flask
from blue_prints.init_db import init_db_bp
from blue_prints.accidents_analyze import accidents_bp

app = Flask(__name__)

app.register_blueprint(init_db_bp)
app.register_blueprint(accidents_bp)

if __name__ == '__main__':
    app.run()
