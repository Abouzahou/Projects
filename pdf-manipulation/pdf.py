import PyPDF2
import sys

inputs = sys.argv[1:]  # get the input file from command line argument

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfMerger() #merger object
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('super.pdf')

pdf_combiner(inputs)        

# with open('dummy.pdf', 'rb') as file: #rb = read binary
#     reader = PyPDF2.PdfReader(file) #reads pdf
#     page = reader.pages[0]
#     #print(len(reader.pages)) #number of pages
#     #print(reader.pages[0])#returns first page object
#     page.rotate(90) #rotates the page 90 degrees clockwise
#     writer = PyPDF2.PdfWriter()
#     writer.add_page(page)
#     with open('tilt.pdf', 'wb') as new_file:
#         writer.write(new_file)
