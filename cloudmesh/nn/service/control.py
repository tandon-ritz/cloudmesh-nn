from flask import Flask, send_file, make_response
from cloudmesh.nn.service.data import generate_figure

def create_boxplot():
    bytes_obj = generate_figure()
    
    return send_file(bytes_obj,
                     attachment_filename='plot.png',
                     mimetype='image/png')
