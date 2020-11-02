# End to End Resume Parser using Natural Language Processing Techniques

* Make sure that you have python and pip installed.
* Now create a virtualenvironment 
`virtualenv -p python3 venv`
* Go inside venv
`source venv/bin/activate`
* Install packages with `pip install -r requirements.txt`
* Now download and link spacy's english language model 
`python -m spacy download en_core_web_sm`

* Now for training run =>
`python trainin_pipeline.py`
Now the model is saved and ready to go.

Now for starting API =>
`python app.py`


Parser is ready and running on port __5007__

Send resume to port __5007__ at this end point __/mlparse__

