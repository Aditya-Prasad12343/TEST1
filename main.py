import streamlit as st
import PyPDF2
import docx2txt

# Function to extract text from a PDF file
def extract_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
        return text

# Function to extract text from a Word document
def extract_docx(file_path):
    return docx2txt.process(file_path)

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
    file_path = st.text_input('Enter the file path of a PDF or DOCX file:')
    file_type = file_path.split('.')[-1].lower()

    # Convert file on button press
    if st.button('Convert'):
        if file_path:
            # Extract text from file
            if file_type == 'pdf':
                text = extract_pdf(file_path)
            elif file_type == 'docx':
                text = extract_docx(file_path)
            else:
                st.error('Unsupported file type. Please upload a PDF or DOCX file.')

            # Convert text to LaTeX format
            latex = to_latex(text)

            # Display LaTeX code
            st.code(latex, language='latex')
        else:
            st.error('Please enter a file path.')

if __name__ == '__main__':
    app()
