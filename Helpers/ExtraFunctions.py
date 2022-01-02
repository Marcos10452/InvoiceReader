import pandas as pd
import re

def check_option2(classnumber,checknumber,getstring,onestring):
    """
    This function gets what is 
    the part of invoice
    1-checknumber is number to be checked again checklist
    2-getstring list conctatenates all string

    >>> checkoption(1,[1,2,3,4],["hola pepe","regular", "azul"], " como estas")
    out:"hola pepe como estas"
    """
    #print (checknumber,alist)
    if classnumber==checknumber:
        getstring[0]+=onestring 
    return getstring  

#_____For regular expression________________________________ 
def RegExpression(text,restrings):
    reaux=re.compile(restrings)
    try:
        m = reaux.findall(text)[0]
        return m
    except IndexError:
        return text   

def checkclass(classtotest, listclass,maintextlist, auxtext):
    for v, classtext in enumerate(listclass):
        if classtotest==classtext: maintextlist[v]+=auxtext
    return maintextlist

###________________ Data FRAME processing data____________________
def process_df(tempdf,tmp_code):

    #reset index because index is for every page
    tempdf=tempdf.reset_index()
    tempdf=tempdf.drop(columns=['index'])

    tempdf['Providercode']= tmp_code

    #checking if decimal is , or . https://regex101.com/
    #Campturing all group (?:) all digit before'.' and all digit after '.' and , and two decimal
    for i,s in enumerate(tempdf['text']):
        test=re.findall(r"(?:\d+\.\d+\,\d\d)", s)
        test2=re.findall(r"(?:\d+\,\d\d)", s)
        if test:
            #check index i and read df.text.iloc[i] the text to be replaced.
            tempdf.loc[i,'text']=s.replace('.', '')
            tempdf.loc[i,'text']=tempdf.text.iloc[i].replace(',', '.')
        elif test2:
            tempdf.loc[i,'text']=tempdf.text.iloc[i].replace(',', '.')

    #Take out semi colons from text
    tempdf['text']=tempdf['text'].str.replace(';', " ")

    # Define Xo and top box as float
    tempdf['x0'] = tempdf['x0'].astype(float).round(0)
    tempdf['top'] = tempdf['top'].astype(float).round(0)
    tempdf['x1'] = tempdf['x1'].astype(float).round(0)
    tempdf['bottom'] = tempdf['bottom'].astype(float).round(0)
    tempdf = tempdf.sort_values(["fname","page_number","top", "x0"], ascending = (True,True,True, True))
    return tempdf
###________________   END  ____________________