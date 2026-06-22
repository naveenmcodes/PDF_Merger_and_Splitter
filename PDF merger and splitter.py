from pypdf import PdfReader, PdfWriter


def merge_pdfs():
    pdf1 = input("Enter first PDF path: ")
    pdf2 = input("Enter second PDF path: ")
    output = input("Enter output PDF name: ")

    writer = PdfWriter()

    for pdf in [pdf1, pdf2]:
        reader = PdfReader(pdf)

        for page in reader.pages:
            writer.add_page(page)

    with open(output, "wb") as file:
        writer.write(file)

    print("PDFs merged successfully!")

from datetime import datetime
import os

def split_pdf():
    pdf_path = input("Enter PDF path: ")

    try:
        reader = PdfReader(pdf_path)

        output_folder = "Split_Pages"
        os.makedirs(output_folder, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        for page_num in range(len(reader.pages)):

            writer = PdfWriter()
            writer.add_page(reader.pages[page_num])

            output_name = os.path.join(
                output_folder,
                f"page_{page_num + 1}_{timestamp}.pdf"
            )

            with open(output_name, "wb") as file:
                writer.write(file)

            print(f"Saved: {output_name}")

        print("\nPDF split successfully!")

    except FileNotFoundError:
        print("PDF file not found!")

    except Exception as e:
        print("Error:", e)


while True:

    print("\n===== PDF MERGER & SPLITTER =====")
    print("1. Merge PDFs")
    print("2. Split PDF")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        merge_pdfs()

    elif choice == "2":
        split_pdf()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")