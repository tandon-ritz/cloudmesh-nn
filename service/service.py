from flask import jsonify
import connexion
import os
from pathlib import Path
from cloudmesh.nn.spec import specification_dir

print(specification_dir)

# Create the application instance

app = connexion.App(__name__, specification_dir=specification_dir)

# Read the yaml file to configure the endpoints
app.add_api("nn.yaml")


# create a URL route in our application for "/"
@app.route("/")
def home():
    msg = {"msg": "Cloudmesh Neural Network Service"}
    return jsonify(msg)


if __name__ == "__main__":
    app.run(host="127.0.0.1",
            port=8080,
            debug=True)


class Manager(object):

    def __init__(self):
        print("init {name}".format(name=self.__class__.__name__))

    def list(self, parameter):
        print("list", parameter)
