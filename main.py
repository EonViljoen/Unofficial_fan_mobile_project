import flask
from flask import jsonify, request
import species_interface as si


# Config flask API
app = flask.Flask(__name__)
app.config["DEBUG"] = True

# API routes
@app.route('/', methods=['GET'])
def home():
    return "<h1>Defualt homepage</h1>"

@app.route('/api/species/all', methods=['GET'])
def species_all():
    species_list = si.return_full_list()

    return (jsonify(species_list))

@app.route('/api/species', methods=['GET'])
def species_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    result = si.return_item_with_id(id)

    name = result['name']
    image_path = result['image']

    return ('<h1>'+name+'</h1><br><br><img src=./'+image_path+'>')

# Run it
app.run()