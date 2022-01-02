# Project description

Invoice Reader

Predict and get data from invoices  such as  invoice’s number, date, total amount, etc. 
The idea was read in a CUTIE paper (check Acknowledgement) . However instead of using an CNN and ORC detec, a classic multy-layer was used instead  powered by pdfplumber.

Basically, it reads a PDF file with pdfplumber library, getting the word’s bounding boxes. Then, those positions pass through a trained  multilayer network  in order to predict in which class that words belong. This is treated as a multi-class classification problem.

### Classes are :
	- 0-None
	- 1-Invoice’s number
	- 2-Invoice’s date
	- 3-CAE number  ( Electronic Authorization Code only for Argentina)
	- 4-CAE Date 
	- 5-Total amount

Works best on machine-generated, rather than scanned PDFs.

## Table of Contents
* [Requirements](#requirements)
* [General Info](#general-information)
* [Training File](#training-file)
* [Getting data from invoice](#getting-data-from-invoice)
* [Setup Usage](#setup-usage)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)


##  Requirements

- Hardware: GPU was not needed in this first approch. However if more parameters are added and neurons are incremented  GPU will be needed or training on Colab.
Intel(R) Core(TM) i5-4200M CPU @ 2.50GHz Memory 8GB

- It was developed in Linux Ubuntu 16.04.7 LTS

- Python 3.7

Libraries
- pdfpluber 0.6.0 → pip install pdfplumber
https://pypi.org/project/pdfplumber/

- SMOTE:Synthetic Minority Oversampling Technique (SMOTE) 
Over-sampling method.
https://imbalanced-learn.org/stable/over_sampling.html#smote-adasyn


- GUI library: tkinter 8.6
https://docs.python.org/3/library/tkinter.html#module-tkinter

- Keras 2.4.3

## General Information

The idea of making an Invoice Reader was to automatize data capture from invoices sent by different providers in PDF format in monthly basis.
Basically, this project is divided in two,

1)Training
file is:
	/10_filefortraining_V2.0ipynb 
	/Helpers/
		|-mlp_helper.py
			“plot_confusion_matrix”
			-plots confusion matrix

2)Reading and predicting

	/Invoice_reader_v2.1.ipynb
	/Helpers/
		|-ExtraFunctions.py
			“RegExpression” function
			-activates regular expressions.
			“fprocess_df” function
				-changes “,”  for “.” in decimal
				-casting to float : X0, X1, Bottom and Top 
		|-FileManager2.py
			class FileManager
				“get_provider_data” function 
				-gets providers’s code from provider’s folder name
				“open_file function” 
				-generates DataFrame  from all PDF’s pages.
				-gets PDF’s with and hight 
				
		|-ImageReader.py
			class ScrollableImage
				“mouse_scrol”
				-moves the PDF’s image
		|-Mlprediction.py
				“prediction_func”
				-uploads model and predict classes. 


## Training File 
→ 10_filefortraining_V2.0ipynb 

As I have mentioned before, pdfplumber reads PDF file and recovers position of every words in invoice inside of red bonding boxes as they are showed in next picture.





As example, file InovoiceSample2.csv is share. It has all samples for training from twelve different providers with an average of 6 invoices as sample each one.

However, a first analysis revels  that data is unbalanced.

![Alt text](/pic/Unbalanced.png?raw=true "Unbalanced data")








Thus, the next step was to use SMOTE creating overlapping samples and solve the problem mentioned above.

![Alt text](/pic/Unbalanced.png?raw=true "Unbalanced data")





Finally, data was balanced as follow. This can be check in the notebook.

![Alt text](/pic/Balanced.png?raw=true "Balanced data")









Other issue I have been facing was that  invoice format changes depending on provider and page. Check pictures  below. 
So, to improve accuracy two additional inputs were added  to multi-network layer:
	a ) Add a provider code. Depending on provider, invoice format changes.
	b) Add number of pages. This it to identify the invoice’s structure

Finally, multi-layer configuration will be:
![Alt text](/pic/model.png?raw=true "final Mul-layer model")













Using Keras to create the Multi-layer model:

![Alt text](/pic/Multi layer network.png?raw=true "final Mul-layer model")











	
## Getting data from invoice 
→ Inovice_reader_v2.1.ipynb 

Invoice reader is using tkinter library as GUI. 
Using is simple, only in menu select File→ Open and then select the PDF file to be read
As example inside provider folder is BASE provider.
![Alt text](/pic/Reader1.png?raw=true "Example of using")

Getting invoice’s number and date. Also CAE’s number and date. Total amount in this case brings more information due to pour labeling in bounding boxes. It must be improved.

![Alt text](/pic/Read2.png?raw=true "Example of using")


Other problem is depending on how the PDF was created, pdfplumber can retrieves more than an word in one bounding box. 
So the solution to minimize it was to use regular expression

Below there is a regular  expression list for recover, invoice’s number, invoice’s date, (*) 	CAE’s number and CAE’s date

	"BASE":  [r'\d{4}\-\d{8}',r"\d{2}\/\d{2}\/\d{4}",r"\d{14}$",r"\d{2}.\d{2}.\d{4}"]



## Setup_Usage
Running the notebooks you shouldn’t have any issue.

_ Training _: if increase the number of samples, a GPU is going to be needed.

_ Predict _: It is based on GUI so is intuitive. There is not additional requirement already mentioned  above.

## Project Status
I can divide this project two stages.

- First stage has been completed. It shows that is possible to get data from invoices
-Second stage is still in progress. As you can read in “Room for Improvement”. 
	


## Room for Improvement

As I have mentioned before, in example Total amount’s value are not accurate. 
Besides, the idea is to read all invoice information in order to get and description item by item. 

So it ca be summarize as:

Room for improvement:
- Improve  labeling in samples taken. This is in order to get  more accurate values. In example, the error in “total amount” mentioned before. 
- Increase  neuron in hidden layers in order to improve  training.

To do:
- Get all information from invoice, to read item by item.
- Save all values in Excel format in order to be processed and storage as a database.


## Acknowledgements

-  CUTIE: Learning to Understand Documents with Convolutional Universal Text
Information Extractor
https://arxiv.org/abs/1903.12363



## Contact
Created by Marcos Tagliapietra [(https://www.linkedin.com/in/marcos-e-tagliapietra)]
Any question feel free to contact me!

