
import pandas as pd
import math
import string
import training.utils as utils
import training.config as config



def convertODStoTSV(fromODS, toTSV):    

    data = utils.read_ods(fromODS)
    df = pd.DataFrame(data)

    print(len(df))
    words_list = []
    tags_list = []


    for ind in df.index:

        if df['Word'][ind] == '.' and df['Tag'][ind] == '.':
            words_list.append('.')
            tags_list.append('.')
            continue
        if df['Word'][ind] == 'XXX':
            words_list.append('\n')
        else:
            words_list.append(df['Word'][ind])

        if df['Tag'][ind][:2] in ('B-', 'I-'):
            tags_list.append(df['Tag'][ind])
        
        else:
            tags_list.append('O')
            
        
    dict = {'Word': words_list, 'Tag': tags_list}  
    df = pd.DataFrame(dict)

    print(len(df))  
    df.to_csv(toTSV,sep='\t', index=False)


# convertODStoTSV('/home/accubits/Documents/Projects/AI/resume/training/training_dataset/Education.ods' \
#     , '/home/accubits/Documents/Projects/AI/resume/training/training_dataset/Education.tsv')