# there are two codes in this file 1st one is default code 2nd one is modified by dheeraj, use any- "one" of them.

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import numpy as np
import nltk
nltk.download('punkt')
nltk.download('stopwords')

def process(file):
    raw=open(file).read()
    tokens=word_tokenize(raw)
    words=[w.lower() for w in tokens]
    porter=nltk.PorterStemmer()
    Stemmed_tokens=[porter.stem(t) for t in words]
    #removing stop words
    stop_words=set(stopwords.words('english'))
    filtered_tokens=[w for w in Stemmed_tokens if not w in
    stop_words]
    #count words
    count=nltk.defaultdict(int)
    for word in filtered_tokens:
        count[word]+=1
    return count

def cos_sim(a,b):
    dot_product=np.dot(a,b)
    norm_a=np.linalg.norm(a)
    norm_b=np.linalg.norm(b)
    return dot_product/(norm_a * norm_b)


def getSimilarity(dict1,dict2):
    all_words_list=[]
    for key in dict1:
        all_words_list.append(key)
    for key in dict2:
        all_words_list.append(key)
    all_words_list_size=len(all_words_list)
    v1=np.zeros(all_words_list_size,dtype=int)
    v2=np.zeros(all_words_list_size,dtype=int)
    i=0
    for (key) in all_words_list:
        v1[i]=dict1.get(key,0)
        v2[i]=dict2.get(key,0)
        i=i+1
    return cos_sim(v1,v2)


if __name__=='__main__':
    dict1=process("C:/Users/BSC_IT1/Desktop/text_2.txt")
    dict2=process("C:/Users/BSC_IT1/Desktop/text_2.txt")
    print("Similarity between two text documents",getSimilarity(dict1,dict2))

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

    
    
# 2nd version-
nltk.download('punkt')
nltk.download('stopwords')
def process(file):
    raw = open(file).read()
    tokens = word_tokenize(raw)
    words = [w.lower() for w in tokens]
    Stemmed_tokens = [nltk.PorterStemmer().stem(t) for t in words]
    return {w: Stemmed_tokens.count(w) for w in set(Stemmed_tokens) if not w in stopwords.words()}
def cos_sim(a,b):
    return np.dot(a,b) / (np.linalg.norm(a) * np.linalg.norm(b))
def getSimilarity(dict1, dict2):
    words = set(dict1.keys()).union(set(dict2.keys()))
    v1, v2 = np.array([dict1.get(w, 0) for w in words]), np.array([dict2.get(w, 0) for w in words])
    return cos_sim(v1, v2)
if __name__ == '__main__':
    dict1 = process('text1.txt')
    dict2 = process('text2.txt')
    print('Similarity between two text documents:',getSimilarity(dict1,dict2))
