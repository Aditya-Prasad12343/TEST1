import streamlit as st
import PyPDF2
import docx
import io

# Function to extract text from a PDF file
def extract_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ''
    for page in reader.pages:
        text += page.extract_text()
    return text

# Function to extract text from a Word document
def extract_docx(file):
    doc = docx.Document(file)
    text = ''
    for paragraph in doc.paragraphs:
        text += paragraph.text + '\n'
    return text

# Function to convert the extracted text to LaTeX format
def to_latex(text):
    # Replace special characters with LaTeX equivalents
    text = text.replace('&', '\\&')
    text = text.replace('%', '\\%')
    text = text.replace('$', '\\$')
    text = text.replace('#', '\\#')
    text = text.replace('_', '\\_')
    text = text.replace('{', '\\{')
    text = text.replace('}', '\\}')
    text = text.replace('~', '\\textasciitilde{}')
    text = text.replace('^', '\\textasciicircum{}')

    # Replace line breaks with LaTeX newline characters
    text = text.replace('\n', '\\\\')

    # Wrap text in LaTeX document tags
    latex = '\\documentclass{article}\n\\begin{document}\n'
    latex += text
    latex += '\n\\end{document}\n'

    return latex

# Streamlit app
def app():
    st.title('PDF/Word to LaTeX Converter')

    # File upload widget
    file = st.file_uploader('Upload a PDF or DOCX file:', type=['pdf', 'docx'])

    # Convert file on button press
    if st.button('Convert'):
        if file is not None:
            # Get file contents
            file_contents = file.read()

            # Extract text from file
            file_type = file.name.split('.')[-1].lower()
            if file_type == 'pdf':
                text = extract_pdf(io.BytesIO(file_contents))
            elif file_type == 'docx':
                text = extract_docx(io.BytesIO(file_contents))
            else:
                st.error('Unsupported file type. Please upload a PDF or DOCX file.')

            # Convert text to LaTeX format
            latex = to_latex(text)

            # Display LaTeX code
            st.code(latex, language='latex')
        else:
            st.error('Please upload a file.')

if __name__ == '__main__':
    app()
