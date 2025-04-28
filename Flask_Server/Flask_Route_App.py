''' Vi importer med vilje ikke  all (*), da det er grimt imo'''
from flask import Flask, render_template, request, jsonify
import Questions as Q
import Map as M

app = Flask(__name__)


def initialize():
    return app


def run_program():
    return app.run(debug=True, port=3050)

""" ##################### Initilize ####################### """

initialize()


""" ##################### Setup Routes ####################### """

@app.route('/')
def generate_index():

    return render_template('index.html',
     ip="127.0.0.1")


@app.route("/ip", methods=["GET"])
def get_my_ip():
    return jsonify({'ip': request.remote_addr}), 200

@app.route("/map")
def map():
    result = M.execMap()
    desc = "This is a Interactive map showing the prices of 1kg bananas across the world in DKK currency"
    return render_template('page.html',data=result, desc=desc)

@app.route("/faq")
def faq():
    routes = Q.getQuestions()
    return render_template('questions.html',data=routes)

@app.route("/1")
def question1():
    result = Q.execQ1()
    desc = "This is a interactive chart over how many products were tested (currently test phase)"
    return render_template('page.html',data="aa", desc=result)


""" ##################### Start shit ####################### """

run_program()
