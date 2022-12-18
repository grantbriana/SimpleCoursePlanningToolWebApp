import os
import random
import json
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename



app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = "Tracks"
dictionary = {
   "fileName": "",
   "track": ""
}

@app.route('/')
def home():
   return render_template('index.html')


@app.route('/browserSchedule')
def browserSchedule():
   return render_template('browserSchedule.html')


def runApp():
  import fileReader as fr
  import scheduleGenerator as gen
  import DAG as dag
 

@app.route('/success', methods = ['POST'])
def uploadFile():
  if request.method == 'POST':
    f = request.files['file']
    filename = secure_filename(f.filename)
    # create the folders when setting up your app
    os.makedirs(os.path.join(app.instance_path, 'htmlfi'), exist_ok=True)
    
    # when saving the file
    f.save(os.path.join(app.instance_path, 'htmlfi', secure_filename(f.filename)))

    #Load to JSON
    dictionary["fileName"] = filename
    dictionary["track"] = request.form.get("track")
    with open("upload.json", "w") as outfile:
      json.dump(dictionary, outfile)
      
  runApp()
  #return render_template('browserSchedule.html')
  from displaySchedule import display
  schedule = display()
  return render_template('browserSchedule.html', variable = schedule)


if __name__ == '__main__':
   app.run( # Starts the site
    debug=True,
		host='0.0.0.0',  # EStablishes the host, required for repl to detect the site
		port=random.randint(2000, 9000)  # Randomly select the port the machine hosts on.
	)




