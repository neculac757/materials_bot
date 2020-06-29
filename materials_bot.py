#!/usr/bin/env python
# coding: utf-8

# In[1]:

import urllib
import json
import os

import pandas as pd
import xlrd
import csv

from flask import Flask
from flask import request
from flask import make_response

app = Flask(__name__)

@app.route('/',methods=['GET'])
def hello_world():
    return 'Hello, World!'

@app.route('/webhook',methods=['POST'])
def webhook():
    req=request.get_json(silent=True,force=True)
    print("Request:")
    print(json.dumps(req,indent=4))
    res=makeWebhookResult(req)
    res=json.dumps(res,indent=4)
    
    r=make_response(res)
    r.headers['Content-Type']='application/json'
    print("yeeee haiiii responseeee: ",r)
    return r

def makeWebhookResult(req):
    m_type=req.queryResult.outputContexts[0].parameters.mat_type.original
    m_feature=req.queryResult.outputContexts[0].parameters.mat_feature.original
    m_feature1=req.queryResult.outputContexts[0].parameters.mat_feature1.original
    speech=str(m_type)+str(m_feature)+str(m_feature1)+"  yeh he response"
    return {
              "fulfillmentMessages": [
                {
                  "text": {
                    "text": [
                      speech
                    ]
                  }
                }
              ]
            }

if __name__=='__main__':
    port=int(os.getenv('PORT',80))
    app.run(debug=False,port=port,host='0.0.0.0')
    
    
    
#     port= int(os.getenv('PORT',5000))
#     print("starting server on port",port)
#     app.run(debug=True,port=port,host='0.0.0.0')
   
    
    
#     if req.get("result").get("action")=='material_feature':
#         result=req.get("result")
#         parameters=result.get("parameters")
#         mtype=parameters.get("material_type")
#         kfeature=parameters.get("key_features")
#         new_material="ni milega new material"
#         speech="New material is"+new_material
#         print("Response:")
#         print(speech)
#         return {
#             "speech":speech,
#             "displayText":speech,
#             "source":'material_feature'  
#         }



# import importlib.util
# spec = importlib.util.spec_from_file_location("flask", "/home/ashar/anaconda3/bin/flask")
# foo = importlib.util.module_from_spec(spec)
# spec.loader.exec_module(foo)
# foo.MyClass()

# import flask
# from flask import request
# from flask import make_response

# app=flask(__name__)

# @app.route('/webhook',methods=['POST'])
# def webhook():
#     req=request.get_json(silent=True,force=True)
#     print("Request:")
#     print(json.dumps(req,indent=4))
#     res=makeWebhookResult(req)
#     res=json.dumps(res,indent=4)
#     print(res)
#     r=make_response(res)
#     r.headers['Content-Type']='application/json'
#     return r

# def makeWebhookResult(req):
#     if req.get("result").get("action")=='material_feature':
#         result=req.get("result")
#         parameters=result.get("parameters")
#         mtype=parameters.get("material_type")
#         kfeature=parameters.get("key_features")
#         new_material="ni milega new material"
#         speech="New material is"+new_material
#         print("Response:")
#         print(speech)
#         return {
#             "speech":speech,
#             "displayText":speech,
#             "source":'material_feature'  
#         }
    
# if __name__=='__main__':
#     port=process.env.PORT
#     app.run(debug=True,port=port)
    


# In[2]:


# import pandas as pd
# import xlrd
# import csv

# file_path='new_material.xlsx'


# def csv_from_excel(file):
#     wb = xlrd.open_workbook(file)
#     sh = wb.sheet_by_name('Foglio1')
#     csv_new_material = open('new_material.csv', 'w')
#     wr = csv.writer(csv_new_material, quoting=csv.QUOTE_ALL)

#     for rownum in range(sh.nrows):
#         wr.writerow(sh.row_values(rownum))

#     csv_new_material.close()

# # runs the csv_from_excel function:
# csv_from_excel(file_path)
# new_material = pd.read_csv('new_material.csv')
# new_material=new_material[['New material name (output)','Type (input)','Ultimate tensile strength(Mpa)','Elongation(%)','Key features (input)','Application']]

# print(new_material)


# In[ ]:





# In[23]:


# material_type='steel'
# material_tensile_str=''
# material_elongation=''
# material_key_feature='corrosion resistant perform well at high temperatures'
# material_application=''

# material_score=pd.DataFrame(columns=['material','score','type','tensile','elongation','feature','application'])

# def find_type_similarity(current_type,material_type):
#     if (str(current_type)!='nan') & (str(material_type)!='nan'):
#         similarity_score=find_sent_sim(current_type.lower(),['sample text',material_type.lower()])
#     else:
#         similarity_score=[0,0]
#     return similarity_score[1]

# def find_tensile_similarity(current_tensile,material_tensile_str):
#     if (str(current_tensile)!='nan') & (str(material_tensile_str)!='nan'):
#         difference = abs(int(current_tensile)-int(material_tensile_str))
#         score = 1/difference
#     else:
#         score = 0
#     return score

# def find_elongation_similarity(current_elongation,material_elongation):
#     if (str(current_elongation)!='nan') & (str(material_elongation)!='nan'):
#         difference = abs(int(current_elongation)-int(material_elongation))
#         score = 1/difference
#     else:
#         score = 0
#     return score

# def find_feature_similarity(current_feature,material_key_feature):
#     if (str(current_feature)!='nan') & (str(material_key_feature)!='nan'):
#         similarity_score=find_sent_sim(current_feature.lower(),['sample text',material_key_feature.lower()])
#     else:
#         similarity_score=[0,0]
#     return similarity_score[1]
    
# def find_application_similarity(current_application,material_application):
#     if (str(current_application)!='nan') & (str(material_application)!='nan'):
#         similarity_score=find_sent_sim(current_application.lower(),['sample text',material_application.lower()])
#     else:
#         similarity_score=[0,0]
#     return similarity_score[1]

# for index,row in new_material.iterrows():
#     material_name = row['New material name (output)']
#     if material_type != '':
#         type_similarity = find_type_similarity(row['Type (input)'],material_type)
#     else:
#         type_similarity = 0.0
    
#     if material_tensile_str != '':
#         tensile_similarity = find_tensile_similarity(row['Ultimate tensile strength(Mpa)'],material_tensile_str)
#     else:
#         tensile_similarity = 0.0
        
#     if material_elongation != '':
#         elongation_similarity = find_elongation_similarity(row['Elongation(%)'],material_elongation)
#     else:
#         elongation_similarity = 0.0
        
#     if material_key_feature != '':
#         feature_similarity = find_feature_similarity(row['Key features (input)'],material_key_feature)
#     else:
#         feature_similarity = 0.0
        
#     if material_application != '':
#         application_similarity = find_application_similarity(row['Application'],material_application)
#     else:
#         application_similarity = 0.0
        
#     total_score = type_similarity+tensile_similarity+elongation_similarity+feature_similarity+application_similarity
#     material_score.loc[len(material_score)]=[material_name,total_score,
#                                              str(row['Type (input)']) + ' '+str(type_similarity),
#                                              str(row['Ultimate tensile strength(Mpa)']) + ' '+str(tensile_similarity),
#                                              str(row['Elongation(%)']) + ' '+str(elongation_similarity),
#                                              str(feature_similarity) +' '+ str(row['Key features (input)']),
#                                              str(application_similarity) + ' '+ str(row['Application'])]
#     material_score = material_score.sort_values(by='score', ascending=False)

# print(material_score[:1])
# print(str(material_score.loc[0]['feature']))
# print(str(material_score.loc[0]['application']))


# # In[4]:


# from gensim import corpora, models, similarities
# import jieba

# def find_sent_sim(sentence,sentList):
#     maxVal=0
#     texts = sentList
#     keyword = sentence
#     texts = [jieba.lcut(text) for text in texts]
#     dictionary = corpora.Dictionary(texts)
#     feature_cnt = len(dictionary.token2id)
#     corpus = [dictionary.doc2bow(text) for text in texts]
#     tfidf = models.TfidfModel(corpus) 
#     kw_vector = dictionary.doc2bow(jieba.lcut(keyword))
#     index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features = feature_cnt)
#     sim = index[tfidf[kw_vector]]
#     return sim

# print(find_sent_sim("I am astonishing",['asds dae',"ashar is my bro astonishing",])[1])

