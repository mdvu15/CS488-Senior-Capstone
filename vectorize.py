#Initialization module
import numpy as np
import pickle

# Load the fastText model stored in model.pkl
file = open('model.pkl', 'rb')
model = pickle.load(file)
file.close()

# Load unpacked IBC data stored in ibcData.pkl
ibcData = open('ibcData.pkl', 'rb')
[lib, con, neutral] = pickle.load(ibcData)
ibcData.close()

def getSentencesIbc():
    """Gets sentences and their labels from the IBC"""
    
    sentences = []
    label = []

    for ideology in [lib, con, neutral]:
        for tree in ideology:
            for node in tree: #each node is a subset of words in the sentence
                if hasattr(node, 'label'):
                    sentence = node.get_words().split() #store sentence as a list of words
                    sentences.append(sentence) 
                    label.append(node.label)

    return (sentences, label)


def sentenceVectorizer(sent, model):
    """Vectorize ONE sentence given the word embedding model"""
    
    sent_vec =[]
    numw = 0

    for word in sent:
        try:
            if numw == 0:
                sent_vec = model[word]
            else:
                sent_vec = np.add(sent_vec, model[word])
            numw+=1
        except:
            pass
    #Return the sentence matrix as an average of the word matrices
    return np.asarray(sent_vec) / numw 

 
def vectorizeSentences():
    """Return an array of vectorized sentences from the IBC"""
    
    vectorizedSentences=[]
    sentences = getSentencesIbc()[0]

    for sentence in sentences:
        vectorizedSentences.append(sentenceVectorizer(sentence, model))  

    return vectorizedSentences 


