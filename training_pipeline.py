from training.tsvToJson import convertTSVtoJSON
from training.JsonToTraining import for_spacy
from training.train import custom_nlp_train
from training.odsToTsv import convertODStoTSV
import training.config as config 



if __name__ == "__main__":
    
    ## Education
    # convertODStoTSV(config.EducationODS, config.Education_tsv)
    # convertTSVtoJSON(config.Education_tsv, config.Education_json)
    # for_spacy(config.Education_json, config.Education_training)
    # custom_nlp_train(config.Education_training, config.Education_model_dir)

    ## Skills
    # convertODStoTSV(config.SkillODS, config.Skills_tsv)
    # convertTSVtoJSON(config.Skills_tsv, config.Skills_json)
    # for_spacy(config.Skills_json, config.Skills_training)
    # custom_nlp_train(config.Skills_training, config.Skills_model_dir)


    # # # Experience
    # convertODStoTSV(config.ExperienceODS, config.Experience_tsv)
    # convertTSVtoJSON(config.Experience_tsv, config.Experience_json)
    # for_spacy(config.Experience_json, config.Experience_training)
    # custom_nlp_train(config.Experience_training, config.Experience_model_dir)

    # ## Resume
    # convertTSVtoJSON(config.Resume_tsv, config.Resume_json)
    for_spacy(config.Resume_json, config.Resume_training)
    custom_nlp_train(config.Resume_training, config.Resume_model_dir)




    
    
