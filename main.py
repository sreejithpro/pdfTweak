# Import Python libraries
import shutil
import io
import os
# Import PyPDF
from PyPDF2 import PdfWriter, PdfReader

# Import reportlab
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A1
from reportlab.lib.units import inch

directory = r'C:\Users\pari1218\Downloads\Flood Maps\ABD-Set II' # Target Directory
# Make a folder path for keeping edited files named 'edited' inside the target folder
editedFolder = os.path.join(directory, "edited")

if os.path.exists(editedFolder):  # Remove existing 'edited' folder if exists
    shutil.rmtree(editedFolder)
os.mkdir(editedFolder) # Make 'edited' folder

for filename in os.listdir(directory): # Iterate through files in Target Directory
    f = filename
    fPath = os.path.join(directory, filename)
    fPath2 = os.path.join(directory, "edited", filename)
    text_to_add, fileExtension = os.path.splitext(filename) # Defining the text to be placed
    if os.path.isfile(fPath):  # Check whether it is a file
        # PyPDF operations, set parameters for writing text
        packet = io.BytesIO()
        can = canvas.Canvas(packet, pagesize=A1) # Size of new PDF, suggest to keep it as A4 or as same as
        # the size of original PDF
        can.setFont("Helvetica-Bold", 16) # Choose a Font and Font size
        # Defining the place where text to be placed, you might have to experiment with these numbers
        # to get the exact position
        can.drawString(13.5 * inch, 9.2 * inch, str(text_to_add)) # Placing the text
        can.save()

        # Move to the beginning of the StringIO buffer
        packet.seek(0)

        # create a new PDF with Reportlab
        new_pdf = PdfReader(packet)
        # read your existing PDF
        originalFile = f
        existing_pdf = PdfReader(open(fPath, "rb"))
        output = PdfWriter()
        # add the "Text" (which is the new pdf) on the existing page
        page = existing_pdf.pages[0]
        page.merge_page(new_pdf.pages[0])
        output.add_page(page)
        # Write "output" to the destination file in 'edited' folder
        output_stream = open(fPath2, "wb")
        output.write(output_stream)
        output_stream.close()






