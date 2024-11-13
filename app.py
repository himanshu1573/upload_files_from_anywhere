from flask import Flask, request, send_from_directory
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return '''
        <h1>Upload a File</h1>
        <form method="post" action="/upload" enctype="multipart/form-data">
            <input type="file" name="file">
            <input type="submit">
        </form>
        <h1>Access Uploaded Files</h1>
        <ul>
            ''' + ''.join([f'<li><a href="/files/{file}">{file}</a></li>' for file in os.listdir(UPLOAD_FOLDER)]) + '''
        </ul>
    '''

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file:
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)
        return f'File uploaded successfully: <a href="/files/{file.filename}">{file.filename}</a>'

@app.route('/files/<path:filename>')
def download_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)
