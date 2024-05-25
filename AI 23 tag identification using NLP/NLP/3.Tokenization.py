import pandas as pd
import nltk

rawdata=open("SMSSpamCollection.tsv").read()
rawdata[0:250]
data=pd.read_csv('SMSSpamCollection.tsv', sep='\t', names=['label','body_text'], header=None)
print("Read_Data",data.head)


##Remove Punctuations
import string
string.punctuation        
def remove_punct(text):
    text_nopunct="".join([char for char in text if char not in string.punctuation])
    return text_nopunct
data['body_text_clean']=data['body_text'].apply(lambda x:remove_punct(x))
print("Remove_Punct",data.head)

##Tokenization
import re
def tokenize(text):
    tokens=re.split('\W+',text)
    return tokens
data['body_text_tokenized']=data['body_text_clean'].apply(lambda x: tokenize(x.lower()))
print("Tokenization",data.head)
