import json
import pickle
import re

def trim_entity_spans(data: list) -> list:
    invalid_span_tokens = re.compile(r'\s')

    cleaned_data = []
    for text, annotations in data:
        entities = annotations['entities']
        valid_entities = []
        for start, end, label in entities:
            valid_start = start
            valid_end = end
            while valid_start < len(text) and invalid_span_tokens.match(
                    text[valid_start]):
                valid_start += 1
            while valid_end > 1 and invalid_span_tokens.match(
                    text[valid_end - 1]):
                valid_end -= 1
            valid_entities.append([valid_start, valid_end, label])
        cleaned_data.append([text, {'entities': valid_entities}])
    print("Cleaned trailing spaces")

    return cleaned_data



def for_spacy(input_file, output_file):
    count = 0
    class_labels = list()
    training_data = []
    lines = []
    with open(input_file, 'r')  as f:
        lines = f.readlines()
    
    for line in lines:
        data = json.loads(line)
        entities = []
        if  data['annotation'] == None:
            continue
        text = data['content']
        count += 1
        for annotation in data['annotation']:
            point = annotation['points'][0]
            labels = annotation['label']
            
            for lb in labels:
                if lb not in class_labels:
                    class_labels.append(lb)
            if not isinstance(labels, list):
                labels = [labels]

            for label in labels:
                entities.append((point['start'], point['end'] + 1 ,label))


        training_data.append((text, {"entities" : entities}))
    training_data = trim_entity_spans(training_data)
    print(training_data)
    print(count)
    

    with open(output_file, 'wb') as fp:
            pickle.dump(training_data, fp)
    
            
        
        
        


# if __name__ == "__main__":
#     for_spacy('/home/accubits/Documents/Projects/AI/resume/training/training_dataset/Education.json' ,\
#          '/home/accubits/Documents/Projects/AI/resume/training/Models/EducationForTraining')
