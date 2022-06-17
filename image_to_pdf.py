import fitz
from svglib.svglib import svg2rlg
from reportlab.graphics.renderPDF import drawToString

def svg_to_doc(path):
    drawing = svg2rlg(path)
    pdfbytes = drawToString(drawing)
    return fitz.open("pdf", pdfbytes)

def main():
    layers_number = 2
    doc = fitz.open()
    for n in range(layers_number):
        page = doc.new_page()
        xref = doc.add_ocg(f'diapo_{n+1}', on=True)
        layer = svg_to_doc(f'presentacion/diapo_{n+1}.svg')
        bb = layer[0].rect
        page.set_mediabox(bb)
        page.show_pdf_page(bb, layer, 0, oc=xref)
    doc.save("output.pdf")

if __name__ == "__main__":
    main()