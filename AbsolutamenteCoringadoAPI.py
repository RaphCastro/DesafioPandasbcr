import pandas as pd
from flask import Flask, request, jsonify 
# from flask_cors import CORS
from generateDB import delete_country, update_country, get_countries, get_country_by_id, delete_country, insert_country

# INICIO DA IMPLEMENTAÇÃO DA API
app = Flask(__name__)
# CORS(app, resources={r"/*": {"origins":"*"}})

@app.route('/api/countries', methods=['GET'])
def api_get_countries():
    try:
        return jsonify(get_countries()), 200
    except:
        return jsonify({'reason': 'falha ao recuperar os dados'}), 500

@app.route('/api/countries/<country_id>', methods=['GET'])
def api_get_country(country_id):
    return jsonify(get_country_by_id(country_id))

@app.route('/api/countries/add',  methods = ['POST'])
def api_add_country():
    country = request.get_json()
    return jsonify(insert_country(country))

@app.route('/api/countries/update',  methods = ['PUT'])
def api_update_country():
    country = request.get_json()
    return jsonify(update_country(country))

@app.route('/api/countries/delete/<country_id>',  methods = ['DELETE'])
def api_delete_country(country_id):
    return jsonify(delete_country(country_id))

if __name__ == "__main__":
    #app.debug = True
    #app.run(debug=True)
    app.run(port=5000,debug=True) #run app







