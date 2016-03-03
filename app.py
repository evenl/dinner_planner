#!flask/bin/python
from flask import Flask, jsonify
import planner

app   = Flask(__name__)
dplan = planner.dinner_planner()

@app.route('/api/v1.0/dinners', methods=['GET'])
def get_dinners():
    return jsonify({'dinners': dplan.get_dinners()})

@app.route('/api/v1.0/plan', methods=['GET'])
def get_plan():
    return jsonify({'dinner_plan': dplan.get_plan()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

