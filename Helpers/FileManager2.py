#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#for GUI
from tkinter import filedialog
import pdfplumber
import pandas as pd

from PIL import Image

#for path
import glob
import os

class FileManager():
    def __init__(self, invoicepath="./Invoice/",
                 providerName={'PROVIDER1':['AR003176',1]}):
        self.invoicepath = invoicepath
        self.providerName = providerName

        #self.model = model
    
    def look_path(self):
        filepath =  filedialog.askopenfilename(initialdir =self.invoicepath,title = "Select file",
                                                    filetypes = (("pdf files","*.pdf"),("pdf files","*.PDF"),
                                                                 ("all files","*.*")))
        
        filepath = glob.glob(filepath)[0]
        #destroy()
        return filepath
    
    def get_provider_data(self,filepath):
        flagexit=False
        res = filepath.split('/')
        #print(res)
        for name in self.providerName:
            #print(name)
            #Check provider's name with file selected
            if res[len(res)-2]==name:
                flagexit=True
                #return prov code
                ProvCode=self.providerName[name][0]
                provNum=self.providerName[name][1]
                break
        #exit if error
        if flagexit==False:
            print('Provider name was not found!!. Exit')
            exit()
        return  ProvCode,provNum,name
        
    def open_file(self,filepath):
        df=None
        for pdf_file in filepath:
            filename=pdf_file.replace(self.invoicepath,"")
            
            with pdfplumber.open(pdf_file) as pdf:
                pages = pdf.pages
                
                for i,pg in enumerate(pages):
                    tmp = pd.DataFrame(pg.extract_words(keep_blank_chars=True,extra_attrs=['page_number']))
                    tmp['fname'] = filename
                    df=pd.concat([df,tmp])
                    #Creat png file from invoice
                    if i!=0: 
                        img = Image.open(filepath[0]+".png")
                        #using pdfplumber to get image and to save
                        im = pdf.pages[i].to_image(resolution=110)
                        #adding words boxes detected by pdfplumber
                        im.save("aux.png", format="png")
                        #uploading again as Image fron Pillow
                        im = Image.open("aux.png")
                        max_width = max(img.size[0],im.size[0])
                        total_height = img.size[1]+im.size[1]

                        new_im = Image.new('RGB', (max_width, total_height))
                        new_im.paste(img, (0,0))

                        new_im.paste(im, (0,img.size[1]))
                        new_im.save(filepath[0]+".png", format="png")      

                    else:
                        #using pdfplumber to get image and to save
                        im = pdf.pages[i].to_image(resolution=110)
                        im.save(filepath[0]+".png", format="png")
                    
        pdf_width=pdf.pages[0].width
        pdf_height=pdf.pages[0].height
        pdf.close()
        return df,pdf_width,pdf_height,i


