from PyPDF2 import PdfMerger

def merge_pdf(resume_path, cover_letter_path, transcript_path, application_package_path):
    pdfs = [resume_path, cover_letter_path, transcript_path]

    merger = PdfMerger()

    for pdf in pdfs:
        merger.append(pdf)

    merger.write(application_package_path)
    merger.close()
    return None