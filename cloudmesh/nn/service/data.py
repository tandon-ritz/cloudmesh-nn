import requests
import io
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.externals.joblib import Memory
from sklearn.datasets import load_svmlight_file
from sklearn.svm import SVC
from os import listdir
from flask import Flask, request, send_file, make_response
from cloudmesh.nn.service import code_dir

#url = 'https://drive.google.com/file/d/1ge5hCVEcSh57XKCh3CVY3GcnHc6WETpA/view?usp=sharing'
#url = 'https://drive.google.com/uc?export=download&id=12u9eviakwqiqsz7x8Sp1ybG9uBaF9bJV'
#url = 'https://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/multiclass/glass.scale'

#Obviously we should use a text file and a post to get this value and read it in here.

url = 'https://drive.google.com/uc?export=download&id=1ge5hCVEcSh57XKCh3CVY3GcnHc6WETpA'

def get_url():
    input_path = code_dir+'/input/input.txt'
    input_file = open(input_path, "rt")
    contents = input_file.read()
    url = contents.rstrip()
    input_file.close()
    return str(url)

def new_download(filename):
    get_url()
    r = requests.get(url, allow_redirects=True)
    open(filename, 'wb').write(r.content)

def download_data(url, filename):
    r = requests.get(url, allow_redirects=True)
    open(filename, 'wb').write(r.content)
    return 
    
def download(output):
    data_dir = code_dir+'/data/'
    output_file = data_dir+output
    new_download(filename=output_file)
    return  str(output) + " Downloaded" +"to" + str(code_dir)


def generate_figure(filename):
    data_dir = code_dir+'/data/'
    file = data_dir + filename
    with open(file,'r') as csvfile:
        my_file = pd.read_csv(csvfile)
        nfl = my_file
        nfl_numeric = nfl.select_dtypes(include=[np.number])
        nfl_numeric.boxplot()
        bytes_image = io.BytesIO()
        bytes_image
        plt.savefig(bytes_image, format='png')
        bytes_image.seek(0)
    return bytes_image

def generate_figureNorm(filename):
    data_dir = code_dir+'/data/'
    file = data_dir + filename
    with open(file,'r') as csvfile:
        my_file = pd.read_csv(csvfile)
        nfl = my_file
        nfl_numeric = nfl.select_dtypes(include=[np.number])
        nfl_normalized = (nfl_numeric - nfl_numeric.mean()) / nfl_numeric.std()
        nfl_normalized.boxplot()
        bytes_image = io.BytesIO()
        bytes_image
        plt.savefig(bytes_image, format='png')
        bytes_image.seek(0)
    return bytes_image

def create_boxplot(filename):
    bytes_obj = generate_figure(filename)
    
    return send_file(bytes_obj,
                     attachment_filename='plot.png',
                     mimetype='image/png')

def create_boxplotNorm(filename):
    bytes_obj = generate_figureNorm(filename)
    
    return send_file(bytes_obj,
                     attachment_filename='plot.png',
                     mimetype='image/png')
def data_location():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))
