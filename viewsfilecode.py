def viewsfile(data):
    name = data['ModelName']
    name_lower = name.lower()
    columns = data.get('columns', {})
    
    # Generate the create function
    create_lines = []
    for column_name in columns:
        create_lines.append(f"    if '{column_name}' in data:")
        if columns[column_name]['type'] == 'PickleType':
            create_lines.append(f"        new_{name_lower}.{column_name} = pickle.dumps(data['{column_name}'])")
        else:
            create_lines.append(f"        new_{name_lower}.{column_name} = data['{column_name}']")
    
    create_function = '\n'.join(create_lines)

    # Generate the update function
    update_lines = []
    for column_name in columns:
        update_lines.append(f"    if '{column_name}' in data:")
        update_lines.append(f"        {name_lower}_instance.{column_name} = data['{column_name}']")
    
    update_function = '\n'.join(update_lines)

    viewscode = f'''
from flask import request, jsonify, make_response
from model import db, {name}

def create_{name_lower}():
    data = request.get_json()
    if not data or '{list(columns.keys())[0]}' not in data:
        return jsonify({{'message': 'Invalid input'}}), 400
    
    new_{name_lower} = {name}()
{create_function}
    
    db.session.add(new_{name_lower})
    db.session.commit()
    return jsonify({{'message': '{name} created successfully'}}), 201

def get_{name_lower}s():
    {name_lower}s = {name}.query.all()
    return jsonify({{'{name_lower}s': [{name_lower}_instance.to_dict() for {name_lower}_instance in {name_lower}s]}})

def get_{name_lower}(id):
    {name_lower}_instance = {name}.query.get(id)
    if {name_lower}_instance:
        return jsonify({{'{name_lower}': {name_lower}_instance.to_dict()}})
    else:
        return make_response(jsonify({{'message': '{name} not found'}}), 404)

def update_{name_lower}(id):
    {name_lower}_instance = {name}.query.get(id)
    if {name_lower}_instance:
        data = request.get_json()
{update_function}
        db.session.commit()
        return jsonify({{'message': '{name} updated successfully'}})
    else:
        return jsonify({{'message': '{name} not found'}}), 404

def delete_{name_lower}(id):
    {name_lower}_instance = {name}.query.get(id)
    if {name_lower}_instance:
        db.session.delete({name_lower}_instance)
        db.session.commit()
        return jsonify({{'message': '{name} deleted successfully'}})
    else:
        return jsonify({{'message': '{name} not found'}}), 404
'''
    return viewscode