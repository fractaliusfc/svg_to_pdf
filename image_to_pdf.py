import fitz

def main():
    layers_number = 2
    doc = fitz.open()
    doc.new_page()
    doc.save("output.pdf")

if __name__ == "__main__":
    main()