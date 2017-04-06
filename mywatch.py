from ImagifyBlueprint import imagify_blueprint
from flask import Flask
from flask import request
from flask import redirect
from flask import url_for
from flask import render_template
from flask import send_from_directory

app = Flask(__name__)
app.register_blueprint(imagify_blueprint)



@app.route('/')
def root():
    return app.send_static_file('index.html')


    