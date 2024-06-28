from flask import Flask
from flask_cors import CORS
from app.views import *
from app.database import init_app

#inicializacion del proyecto Flask
app = Flask(__name__)

init_app(app)
CORS(app)

app.route('/', methods=['GET'])(index)
app.route('/api/cities/', methods=['GET'])(get_all_cities)
app.route('/api/cities/<int:city_id>', methods=['GET'])(get_city)
app.route('/api/cities/', methods=['POST'])(create_city)
app.route('/api/cities/<int:city_id>', methods=['PUT'])(update_city)
app.route('/api/cities/<int:city_id>', methods=['DELETE'])(delete_city)

if __name__=='__main__':
    app.run(debug=True)