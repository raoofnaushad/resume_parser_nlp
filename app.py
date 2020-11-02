from flask import Flask, request, jsonify
import json
import PyPDF2
import docx
import mainML
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
resources = {r"/api/*": {"origins": "*"}}
app.config["CORS_HEADERS"] = "Content-Type"
app.config['JSON_SORT_KEYS'] = False


@app.route('/')
def check():
    return {"Message":"Check"}


@app.route('/mlparse', methods=['POST'])
def mlparse():
    response = request.files['file']
    file_name = response.filename
    resume_parsed = ''
    path = 'data/samples/' + file_name
    response.save(path)
    
    resume_parsed = mainML.get_parsed(file_name)
    # mainML.delete()   
    return jsonify(resume_parsed)


if __name__ == "__main__":
    app.run(debug = True, host='0.0.0.0', port=5007)
