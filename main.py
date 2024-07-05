import json
import os
import zipfile
from io import BytesIO, StringIO
from flask import Flask, send_file, render_template, request, jsonify
from mainfilecode import mainfile
from modelfilecode import modelfile
from routefilecode import routefile
from viewsfilecode import viewsfile

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_files():
    # Receive schema data from the form
    schema = request.json

    # Create a directory to store the files
    if not os.path.exists('result'):
        os.makedirs('result')

    # Generate and write files
    files_to_generate = {
        'main.py': mainfile,
        'model.py': modelfile,
        'routes.py': routefile,
        'views.py': viewsfile
    }

    for filename, generate_function in files_to_generate.items():
        content = generate_function(schema)
        with open(f'result/{filename}', 'w') as file:
            file.write(content)

    # Create requirements.txt
    requirements_content = "Flask==2.3.2\nflask_sqlalchemy\n"
    with open('result/requirements.txt', 'w') as file:
        file.write(requirements_content)

    # Create an empty README.md
    from content import readme
    with open('result/README.md', 'w') as file:
        file.write(readme)

    from content import bashcode
    with open('result/env.sh', 'w') as file:
            file.write(bashcode)
    # Create a ZIP file in memory
    memory_file = BytesIO()
    with zipfile.ZipFile(memory_file, 'w') as zf:
        for filename in files_to_generate.keys():
            zf.write(f'result/{filename}', filename)
        zf.write('result/requirements.txt', 'requirements.txt')
        zf.write('result/README.md', 'README.md')
        zf.write('result/env.sh', 'env.sh')

    # Move to the beginning of the BytesIO buffer
    memory_file.seek(0)

    # Send the ZIP file for download
    return send_file(
        memory_file,
        mimetype='application/zip',
        as_attachment=True,
        download_name='generated_files.zip'
    )

if __name__ == '__main__':
    app.run(debug=True)