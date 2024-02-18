from PyPDF2 import PdfReader, PdfWriter
import sys
from typing import Union, Literal, List

input1 = sys.argv[1]
input2 = sys.argv[2]
wtrmrk = "water_marked_document.pdf"

def watermark(
    content_pdf : input1, # type: ignore
    stamp_pdf :  input2, # type: ignore
    pdf_result :  wtrmrk, # type: ignore
    page_indices: Union[Literal["ALL"], List[int]] = "ALL"
    ):

    reader = PdfReader(content_pdf)
    if page_indices == "ALL":
        page_indices = list(range(0, len(reader.pages)))

    writer = PdfWriter()
    for index in page_indices:
        content_page = reader.pages[index]
        mediabox = content_page.mediabox

        # You need to load it again, as the last time it was overwritten
        reader_stamp = PdfReader(stamp_pdf)
        image_page = reader_stamp.pages[0]

        image_page.merge_page(content_page)
        image_page.mediabox = mediabox
        writer.add_page(image_page)

    with open(pdf_result, "wb") as fp:
        writer.write(fp)

watermark(input1,input2,wtrmrk)        