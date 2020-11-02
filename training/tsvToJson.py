import json
import logging
import sys
def tsv_to_json_format(input_path,output_path):
    try:
        f=open(input_path,'r') # input file
        fp=open(output_path, 'w') # output file
        data_dict={}
        annotations =[]
        label_dict={}
        s=''
        start=0
        flag = 0
        flag2 = 0
        first = 1
        extra = 0
        newLine = 0
        extra2 = 0
        for line in f:

            if line[0:len(line)-1]!='.\t.':
                try:
                    word,entity=line.split('\t')
                except:
                    continue
                entity=entity[:len(entity)-1]
                if first == 1:
                    s += word
                    first = 0
                    extra2 = 0
                    extra3 = 0
                elif word == '\"':
                    s+="\n" 
                    word = "\n"
                    newLine = 1
                    extra2 = 0
                    extra3 = 0
                elif newLine == 1:
                    s+=word
                    newLine = 0
                    extra2 = 0
                    extra3 = 0
                else:
                    if entity[0] == 'B':
                        extra3 = 1
                    else:
                        extra3 = 0
                    s+=" "+word
                    extra2 = 1
                if entity =='':
                    continue
                if entity[0] == 'B' and flag == 1:
                    d = {}
                    d['text'] = y
                    d['start'] = real_start 
                    d['end'] = real_start + (len(y)-1) 
                    try:
                        label_dict[real_entity].append(d)
                    except:
                        label_dict[real_entity]=[]
                        label_dict[real_entity].append(d) 
                    flag2 = 0    
                    flag = 0                
                    y = word
                    real_start = start + extra3
                    real_entity = entity[2:]
                    flag = 1
                    flag2 = 1
                    
                elif entity[0] == 'B' and flag == 0:
                    y = word 
                    
                    real_start = start + extra3
                    real_entity = entity[2:]
                    flag = 1
                    flag2 = 1
                
                
                
                elif entity[0] == 'I' and word != '\n' and y[-1:] != '\n':
                    y +=  " " + word 
                    extra += 1
                
                elif entity[0] == 'I' and word != '\n' and y[-1:]=='\n':                        
                    y +=   word 

                    
                elif entity[0] == 'I' and word == '\n':                    
                    y +=   word 

                    
                else:
                    if flag2 == 1:
                        d = {}
                        d['text'] = y
                        d['start'] = real_start 
                        d['end'] = real_start + (len(y)-1) 
                        try:
                            label_dict[real_entity].append(d)
                        except:
                            label_dict[real_entity]=[]
                            label_dict[real_entity].append(d) 
                        flag2 = 0
                        flag=0
                start+=len(word) + extra2
                extra = 0
                
            else:
                newLine = 0
                extra2 = 0
                if flag2 == 1:
                        d = {}
                        d['text'] = y
                        d['start'] = real_start 
                        d['end'] = real_start + (len(y)-1) 
                        try:
                            label_dict[real_entity].append(d)
                        except:
                            label_dict[real_entity]=[]
                            label_dict[real_entity].append(d) 
                        flag2 = 0
                        flag=0
                data_dict['content']=s
                s=''
                label_list=[]
                for ents in list(label_dict.keys()):
                    for i in range(len(label_dict[ents])):
                        if(label_dict[ents][i]['text']!=''):
                            l=[ents,label_dict[ents][i]]
                            for j in range(i+1,len(label_dict[ents])): 
                                if(label_dict[ents][i]['text']==label_dict[ents][j]['text']):  
                                    di={}
                                    di['start']=label_dict[ents][j]['start']
                                    di['end']=label_dict[ents][j]['end']
                                    di['text']=label_dict[ents][i]['text']
                                    l.append(di)
                                    label_dict[ents][j]['text']=''
                            label_list.append(l)                          
                            
                for entities in label_list:
                    label={}
                    label['label']=[entities[0]]
                    label['points']=entities[1:]
                    annotations.append(label)
                data_dict['annotation']=annotations
                annotations=[]
                json.dump(data_dict, fp)
                fp.write('\n')
                data_dict={}
                label_dict={}
                s=''
                start=0
                flag = 0
                flag2 = 0
                first = 1
                extra = 0
                newLine = 0
                extra2 = 0

    except Exception as e:
        logging.exception("Unable to process file" + "\n" + "error = " + str(e))
        return None


def convertTSVtoJSON(inptutTSV, outputJSON):
    tsv_to_json_format(inptutTSV, outputJSON)

    with open(outputJSON, 'r') as f:
        lines = f.readlines()
    fp = open(outputJSON, 'w')
    for line in lines:
        data = json.loads(line)
        if len(data['content'])<7:
            continue

        json.dump(data,fp )
        fp.write('\n')
    
    
if __name__ == "__main__":
    convertTSVtoJSON('/home/accubits/Documents/Projects/AI/resume/training/training_dataset/Education.tsv', \
                     '/home/accubits/Documents/Projects/AI/resume/training/training_dataset/Education.json')