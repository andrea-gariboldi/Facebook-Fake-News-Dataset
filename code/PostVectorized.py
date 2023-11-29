#import libraries
import spacy
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

nlp = spacy.load("en_core_web_sm")

#how each post will be structured
class postVectorized:
    def __init__(self, id, reactions, vaderSentiment, basicInfo, POS, NER, textLengths, label):
        self.id = id
        self.reactions = reactions
        self.vaderSentiment = vaderSentiment
        self.basicInfo = basicInfo
        self.POS = POS
        self.NER = NER
        self.textLengths = textLengths
        self.label = label
        
#function for trasforming post's text to array-like shape
def vectorizingVaderSentiment(post):
    text = post[1]['text']
    sid_obj = SentimentIntensityAnalyzer()
    sentiment = []
    try:
        sentiment_dict = sid_obj.polarity_scores(text)
    except Exception as e:
        print(e)
    for sent in sentiment_dict.values():
        sentiment.append(sent)
    return sentiment

#function for trasforming post's reactions to array-like shape
def vectorizingReactions(post):
    try:
        post_info = post[1]['reactions']
    except Exception as e:
        post_info = {'like' : 0}
        
    reactions = []
    try:
        reactions.append(post_info['like'])
    except Exception:
        reactions.append(0)
    try:
        reactions.append(post_info['haha'])
    except Exception:
        reactions.append(0)
    try:
        reactions.append(post_info['angry'])
    except Exception:
        reactions.append(0)   
    try:
        reactions.append(post_info['sad'])
    except Exception:
        reactions.append(0)   
    try:
        reactions.append(post_info['love'])
    except Exception:
        reactions.append(0)   
    try:
        reactions.append(post_info['wow'])
    except Exception:
        reactions.append(0)      
    return reactions

#describing each post's basic info in array-style
def vectorizingBasicInfo(post):
    basic_info = []
    
    shares = post[1]['shares']
    basic_info.append(shares)
    
    comments = post[1]['comments']
    basic_info.append(comments)
    
    try:
        reaction_count = post[1]['reaction_count']
        basic_info.append(reaction_count)
    except Exception as e:
        basic_info.append(0)
    
    images = len(post[1]['images'])
    basic_info.append(images)
    
    try:
        links = len(post[1]['links'])
        basic_info.append(links)
    except Exception:
        basic_info.append(0)
    
    return basic_info

#describing each post's Part of speech tagger (for each word) in array style
def vectorizingPOS(post):
    pos_vector = []
    pos_vector_count = []
    text = post[1]['text']
    doc = nlp(text)
    for token in doc:
        pos_vector.append(token.pos_)
    
    noun = pos_vector.count('NOUN')
    pos_vector_count.append(noun)
    
    propn = pos_vector.count('PROPN')
    pos_vector_count.append(propn)
    
    verb = pos_vector.count('VERB')
    pos_vector_count.append(verb)
    
    num = pos_vector.count('NUM')
    pos_vector_count.append(num)
    
    adj = pos_vector.count('ADJ')
    pos_vector_count.append(adj)
    
    conj = pos_vector.count('CONJ')
    pos_vector_count.append(conj)
    
    adv = pos_vector.count('ADV')
    pos_vector_count.append(adv)
    
    return pos_vector_count

#Name entity recognition for each word in a post. Result in array-style shape
def vectorizingNER(post):
    entities = []
    entities_count = []
    text = post[1]['text']
    ner_ent = nlp(text)
    for word in ner_ent.ents:
        entities.append(word.label_)

    person = entities.count('PERSON')
    entities_count.append(person)

    date = entities.count('DATE')
    entities_count.append(date)

    org = entities.count('ORG')
    entities_count.append(org)

    money = entities.count('MONEY')
    entities_count.append(money)

    gpe = entities.count('GPE')
    entities_count.append(gpe)

    norp = entities.count('NORP')
    entities_count.append(norp)
    
    event = entities.count('EVENT')
    entities_count.append(event)
    
    return entities_count

#analizing text lenghts. (When we talk about text we mean ALL the text in the post, so the description + the text appering in the link area)
def vectorizingTextLengths(post):
    text = post[1]['text']
    
    lengths = []
    
    doc = nlp(text)
    words = len(doc)
    lengths.append(words)
    
    chars = 0
    upper_chars = 0
    upper_words = 0
    sentences = 0
    for token in doc:
        chars = chars + len(token) #number of characters 
        if str(token).isupper(): #check if the word is upperCase. If it is, add 1 to the counter
            upper_words = upper_words + 1
        for char in str(token):
            if char.isupper():
                upper_chars = upper_chars + 1
    lengths.append(chars)
    lengths.append(upper_words)
    lengths.append(upper_chars)
    
    for sent in doc.sents:
        sentences = sentences + 1
        
    lengths.append(sentences)
    try:
        lengths.append(chars/words) #average word length
    except Exception as e:
        lengths.append(0)
    try:
        lengths.append(words/sentences) #average sentence length
    except Exception as e:
        lengths.append(0)
    
    return lengths
