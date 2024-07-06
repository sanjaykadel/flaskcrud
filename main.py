import os
import shutil
import zipfile
from io import BytesIO
from flask import Flask, send_file, render_template, request, jsonify
from mainfilecode import mainfile
from modelfilecode import modelfile
from routefilecode import routefile
from viewsfilecode import viewsfile
from databasecode import databasefile
from startfile import startfile

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/data', methods=['POST'])
def get_data():
    schema = request.json
    main_result = mainfile(schema)
    model_result = modelfile(schema)
    route_result = routefile(schema)
    views_result = viewsfile(schema)
    database_result = databasefile(schema)
    start_result = startfile(schema)
    data = {
        'main.pu': main_result,
        'model.py': model_result,
        'routes.py': route_result,
        'views.py': views_result,
        'database.py':database_result,
        'start.sh': start_result
    }

    return jsonify(data)

@app.route('/generate', methods=['POST'])
def generate_files():
    schema = request.json
    
    project_name = schema.get("ProjectName", "project")
    zip_filename = f'{project_name}.zip'

    temp_dir = project_name
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)

    files_to_generate = {
        'main.py': mainfile,
        'model.py': modelfile,
        'routes.py': routefile,
        'views.py': viewsfile,
        'start.sh': startfile,
    }

    for filename, generate_function in files_to_generate.items():
        content = generate_function(schema)
        with open(os.path.join(temp_dir, filename), 'w') as file:
            file.write(content)

    requirements_content = "Flask==2.3.2\nflask_sqlalchemy\n"
    with open(os.path.join(temp_dir, 'requirements.txt'), 'w') as file:
        file.write(requirements_content)

    memory_file = BytesIO()
    with zipfile.ZipFile(memory_file, 'w') as zf:
        for root, _, files in os.walk(temp_dir):
            for file in files:
                zf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), os.path.join(temp_dir, '..')))
        
    memory_file.seek(0)
    shutil.rmtree(temp_dir)

    return send_file(
        memory_file,
        mimetype='application/zip',
        as_attachment=True,
        download_name=f"{project_name}.zip"
    )

if __name__ == '__main__':
    app.run(debug=True)
