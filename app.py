#############################
# KMeans clustering web app
# Input: node file (.csv) 
#        number of clusters
#        initialization method
#        number of runs
# output: The best clustering result 
#         within the specified number of runs
# Yun Zhang 09/16/2017
#############################

from flask import Flask, render_template, request, redirect
import numpy as np
import io
import csv
import sys
app = Flask(__name__)
# store global variable
app.vars={}

@app.route('/')
def main():
	return redirect('/alphonso')

# first page for input
@app.route('/alphonso',methods=['GET'])
def index():
   # page for upload csv data and number of cluster
   return render_template('alphonso.html')
	
if __name__ == '__main__':
   try:
      if len(sys.argv)>1:
         app.run(debug = True,port=int(sys.argv[1]))
      else:
         app.run(debug = True,port=5000)
   except PermissionError:
      print('Permission Error! Try different port number, maybe >5000')