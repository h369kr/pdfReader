import pyttsx3    #pyttsx3 is a text-to-speech conversion library in Python. Unlike alternative libraries, it works offline, and is compatible with both Python 2 and 3.
import PyPDF2     #PyPDF2 is a pure-python PDF library capable of splitting, merging together, cropping, and transforming the pages of PDF files

pdf_file = open('keyboard-shortcuts-windows.pdf','rb')   #Open pdf file in read only mode (in binary fromat) 
reading_pdf = PyPDF2.PdfFileReader(pdf_file)             #Reading the book using PyPDF2 lib function
pdf_pages = reading_pdf.numPages                         #Read a particular page we use numPages

pdf_speaker = pyttsx3.init()                             #initializing pyttsx3 lib
choose_page = reading_pdf.getPage(0)                     #choose page to read out "index-wise"
pdf_text = choose_page.extractText()                     #extact only text from a page
pdf_speaker.say(pdf_text)                                #...to start reading
pdf_speaker.runAndWait()                                 # run and wait method to processes the voice commands
