import PyPDF2
import sys

# get file and watermark from usr
pages = sys.argv[1]
watermark = sys.argv[2]

read_wm = PyPDF2.PdfFileReader(open(f"{watermark}", "rb"))
read_pg = PyPDF2.PdfFileReader(open(f"{pages}", "rb"))
writer = PyPDF2.PdfFileWriter()


# loop through page in pages
for i in range(read_pg.getNumPages()):
    # open each page as page object
    page = read_pg.getPage(i)
    wmpage = read_wm.getPage(0)
    page.mergePage(wmpage)
    writer.addPage(page)

# write to new file
with open("WM File.pdf", "wb") as file:
    writer.write(file)






