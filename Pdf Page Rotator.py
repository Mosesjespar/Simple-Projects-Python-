from PyPDF2 import PdfFileReader, PdfFileWriter
import easygui as eg

input_pdf_path = eg.fileopenbox(title='Choose a Pdf File.', default='*.pdf')

if input_pdf_path is None:
    exit()

rotate_degreeSize = eg.buttonbox(
    title='Degree rotation size',
    msg='By How Many degrees would you like to rotate the pages',
    choices=['90', '180', '270', '360']
)
rotate_degreeSize = int(rotate_degreeSize)

save_title = 'Save new pdf as...'
file_type = '*.pdf'
eg.msgbox(title='Warning', msg='As you are saving, please append the file name with .pdf extension ')
saved_pdf_path = eg.filesavebox(title=save_title, default=file_type)

while saved_pdf_path == input_pdf_path:
    eg.msgbox('Cannot Overwrite Existing Document')
    saved_pdf_path = eg.filesavebox(title=save_title, default=file_type)

if saved_pdf_path is None:
    exit()

input_file = PdfFileReader(input_pdf_path)
rotated_pdf = PdfFileWriter()

for page in input_file.pages:
    page = page.rotateClockwise(rotate_degreeSize)
    rotated_pdf.addPage(page)

with open(saved_pdf_path, 'wb') as final_pdf:
    rotated_pdf.write(final_pdf)

eg.msgbox(msg='All done', title='Result')
