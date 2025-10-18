from flask import Flask, render_template, request, send_file, flash
from docx import Document
import csv
import os
from datetime import datetime
import fitz  # PyMuPDF
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'supersecretkey'

CONVERTED_FOLDER = 'converted_files'
os.makedirs(CONVERTED_FOLDER, exist_ok=True)

ALLOWED_EXTENSIONS = {'txt', 'csv', 'docx', 'pdf'}

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----', ',': '--..--', '.': '.-.-.-', '?': '..--..',
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': '/'
}

REVERSED_MORSE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def text_to_morse(text):
    return ' '.join(MORSE_CODE_DICT.get(char.upper(), '') for char in text)


def morse_to_text(morse):
    words = morse.split(' / ')
    decoded = []
    for word in words:
        chars = word.split()
        decoded_word = ''.join(REVERSED_MORSE_DICT.get(ch, '') for ch in chars)
        decoded.append(decoded_word)
    return ' '.join(decoded)


@app.route('/')
def index():
    return render_template('index.html', result='', download_link='')


@app.route('/convert', methods=['POST'])
def convert():
    option = request.form.get('option')
    file = request.files.get('input_file')

    if not file or file.filename == '':
        flash('No file selected.')
        return render_template('index.html', result='', download_link='')

    if not allowed_file(file.filename):
        flash('Unsupported file type. Please upload a .txt, .csv, .docx, or .pdf file.')
        return render_template('index.html', result='', download_link='')

    filename = secure_filename(file.filename)
    ext = filename.rsplit('.', 1)[1].lower()
    content = ''

    try:
        if ext == 'txt':
            content = file.read().decode('utf-8')

        elif ext == 'csv':
            decoded = file.read().decode('utf-8').splitlines()
            reader = csv.reader(decoded)
            next(reader, None)  # Skip header if exists
            content = '\n'.join([' '.join(row) for row in reader])

        elif ext == 'docx':
            doc = Document(file)
            content = '\n'.join([para.text for para in doc.paragraphs])

        elif ext == 'pdf':
            try:
                pdf_doc = fitz.open(stream=file.read(), filetype="pdf")
                for page in pdf_doc:
                    content += page.get_text()
                if not content.strip():
                    raise ValueError("Empty or unreadable PDF content.")
            except Exception as e:
                flash(f"Failed to read PDF file. Error: {str(e)}")
                return render_template('index.html', result='', download_link='')
    except Exception as e:
        flash(f"Error reading file: {str(e)}")
        return render_template('index.html', result='', download_link='')

    # Perform Conversion
    if option == 'encode':
        result = text_to_morse(content)
        suffix = '_morse.txt'
    else:
        result = morse_to_text(content)
        suffix = '_decoded.txt'

    output_filename = datetime.now().strftime("%Y%m%d%H%M%S") + suffix
    output_path = os.path.join(CONVERTED_FOLDER, output_filename)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(result)

    flash('File converted successfully.')
    return render_template('index.html', result=result, download_link=output_filename)


@app.route('/download/<filename>')
def download_file(filename):
    path = os.path.join(CONVERTED_FOLDER, filename)
    return send_file(path, as_attachment=True)


if __name__ == '__main__':
    print("🚀 Starting Flask app at http://127.0.0.1:5000")
    app.run(debug=True)
