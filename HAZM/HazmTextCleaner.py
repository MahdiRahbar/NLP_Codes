from __future__ import unicode_literals
from hazm import *
from string import punctuation
from collections import Counter


def TextCleaner(Data, stopwordsList):
'''
This function does some preprocessing tasks on persian words using 
Hazm Persian toolkit & a self defined list of stopwords. \n 
****Note that the stop_words list has to be imported in your program before calling this function.
\n
input   | Data List : [ROW : string rows containing its seperated words components, COLUMNS : each word  ]\n
        | stopwordsList : the list of stopwords that was previously imported.
        \n
Output  | A list of strings
'''
    stemmer = Stemmer()
    lemmatizer = Lemmatizer()

    dataList = Data
    table = str.maketrans('', '', punctuation)
    stop_words = stopwordsList

    for i in range(0, len(dataList)):
        vocabulary = []
        for j in range(0, len(dataList[i])):

            dataList[i][j] = stemmer.stem(dataList[i][j])  # Calling Hazm stemmer on the words list

            dataList[i][j] = lemmatizer.lemmatize(dataList[i][j])  # Calling Hazm Lemmatizer on the words list

        
        
        #if !( Regex.IsMatch(Console.ReadLine(), "^[a-zA-Z0-9]*$") ):     # To check the wor

        dataList[i] = [word for word in dataList[i] if word.isalpha()] # Checking if the remained words consist of letters note numbers and etc. 
        dataList[i] = [w for w in dataList[i] if not(w in stop_words)] # Checking the stop words
        dataList[i] = [w.translate(table) for w in dataList[i]] # Using the table to check the punctuations in lists
        dataList[i] = [word for word in dataList[i] if len(word) > 3]  # Checking the lenght of the words. if they were less than 3 letters, probably they are not useful for our purpose.

        vocabulary.append(dataList[i])

    return dataList
