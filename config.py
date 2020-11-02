import os
import spacy


basepath = os.path.dirname(os.path.realpath(__file__))
filedir = "data/samples"
skill_csv  = 'commons/skills.csv'
nations = 'commons/nationality.csv'
state = 'commons/state.csv'
country ='commons/country.csv'
city = "commons/cities_samples.txt"

skills_rb = 'commons/skills'
skill_model_dir = os.getcwd() + '/commons/Models/SKILLS_MODEL'
resume_model = os.getcwd() + '/commons/Models/RESUME-REAL_MODEL'
education_model = 'commons/Models/NEW_EDUCATION'
experience_model = 'commons/Models/NEW_EXPERIENCE'


en_sm = spacy.load('en_core_web_sm')
