from tkinter import *
import webbrowser

## import nltk
## from nltk.tokenize import word_tokenize
## import nltk.classify.util
## from nltk.classify import NaiveBayesClassifier
## from nltk.corpus import names

## from wordcloud import WordCloud, STOPWORDS
## import os
## from PIL import image
## import numpy as np
## import wikipedia


## --------- Functions for the Properties Used Further --------- ##
def printThis():  
    print("........Work in Progress..........")

## ---------- Function For Tokenization Of Words ---------------##
def token():
    tokens = word_tokenize(entry)
    print(tokens)

## ----------- Function For Sentimental Analysis ---------------##
def word_feats(words):
    return dict([(word, True) for word in words])

positive_vocab = ['awesome', 'outstanding', 'fantastic', 'terrific', 'good', 'nice', 'great', ':)']
negative_vocab = ['bad', 'terrible','useless', 'hate', ':(']
neutral_vocab = ['movie','the','sound','was','is','actors','did','know','words','not']

positive_features = [(word_feats(pos), 'positive') for pos in positive_vocab]
negative_features = [(word_feats(neg), 'negative') for neg in negative_vocab]
neutral_features = [(word_feats(neu), 'neutral') for neu in neutral_vocab]

train_set = positive_features + negative_features + neutral_features

## classifier = NaiveBayesClassifier.train(train_set)

neg = 0
pos = 0

## sentence = entry(root)
## sentence = sentence.lower()
## words = sentence.split(' ')

## for word in words:
##     classResult = classifier.classify(word_feast(word))
##     if classResult == 'neg':
##         neg = neg + 1
##     if classResult == 'pos':
##         pos = pos + 1

## print('Positive: ' + str(flot(pos)/len(words)))
## print('Negative: ' + str(float(neg)/len(words)))

## ------------------------ Remove All The Commented Code Before Running For The Sentimental Analysis--------------------##

## ------------------------ Function For Creating Word Cloud ----------------- ##


## currdir = os.path.dirname(__file__) ## This is For Giving the Path to Word Cloud 

def create_wordcloud(entry):
    mask = np.array(Image.open(os.path.join(currdir, "image.png")))
    stopwords = set(STOPWORDS)
    wc = WordCloud(background_color = "white",
                   mask = mask,
                   max_words = 200,
                   stopwords = stopwords)

    wc.generate(text)

    wc.to_file(os.path.join(currdir, "cloudword.png"))

## create_wordcloud(get_wiki(entry))

## --------------------- Remove The Comments From The Above Function For The Word Cloud ---------------------------- ##

## --------------------- Creation Of Function To Choose Specific Open Specific Folder ---------------------------- ##

def callback(event):
    webbrowser.open_new(r"D:\Users\850034273\Desktop")

## ------------- Callback Function Created ---------------- ##

root = Tk()

## --------Creation Of Main Menu Bar---------- ##
menu = Menu(root)
## ----------Configuration Of Main Menu Bar---------- ##
root.config(menu = menu)

## ---------Creation Of Submenu inside Main Menu Bar-------- ##
subMenu = Menu(menu)

## -----------Creation Of Options For Main Menu Bar-------- ##
menu.add_cascade(label="Import File", menu=subMenu)

## ----------Creation Of Submenu's For File Menu---------- ##
subMenu.add_command(label="For Tokenization", command=printThis) 
subMenu.add_command(label="For Sentimental Analysis", command=printThis)
subMenu.add_command(label="For word Cloud Generation", command=printThis)

## ----------Seperator is used to divide the Submenu into sections------------ ##
subMenu.add_separator()
subMenu.add_command(label="Close", command=printThis)
subMenu.add_command(label="Exit", command=printThis)

## ----------Submenu's For the File Menu Created---------- ##

## -------------Creation Of SubMennu inside Main Menu Bar--------- ##
subMenu2 = Menu(menu)

## -------------Creations Of Options For Main Menu Bar---------- ##
menu.add_cascade(label="Edit", menu=subMenu2)

## --------Creation Of SubMenu's For Edit Menu----------- ##
subMenu2.add_command(label="New File For Tokenization", command=printThis)
subMenu2.add_command(label="New File For Sentimental Analysis", command=printThis)
subMenu2.add_command(label="New File For Word Cloud Generation", command=printThis)

## ---------------Created SubMenu For the Edit Menu------------- ##

## --------Creation Of Space To Get User Input To Analyse Text---------- ##
label = Label(root, text="Enter Text Here")
entry = Entry(root)

label.grid(row=4, sticky=E)
entry.grid(row=4, column=1)

button = Button(root, text="Tokenize Text", fg="black", command=token)
button.grid(row=5, column=1)

button2 = Button(root, text="Analyse Sentiments", fg="black", command=word_feats)
button2.grid(row=6, column=1)

button3 = Button(root, text="Generate Cloud Word", fg="black", command=create_wordcloud)
button3.grid(row=7, column=1)

## ------Analyse Text Created------ ##

## -------Creation Of Status Bar-------- ##
##status = Label(root, text=".............................Work in Progress.........................",
##               bd=1, relief= SUNKEN, anchor=W) ##bd is borden and SUNKEN is to import/merge in screen
##status.pack(side=BOTTOM, fill=X)    

## ----------Status Bar Created---------- ##

root.mainloop()
