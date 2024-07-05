def modelfile(data):
    name = data['name']
    columns = data.get('columns', {})
    moddata = []
    to_dict_items = []
    imports = set(['from flask_sqlalchemy import SQLAlchemy'])

    # Create variables for columns and their values
    for column_name, column_info in columns.items():
        column_type = column_info.get('type', '')
        length = column_info.get('length', '')
        
        if column_type == 'DateTime':
            imports.add('from datetime import datetime')
            models = f"    {column_name} = db.Column(db.DateTime, default=datetime.utcnow)"
            to_dict_items.append(f"            '{column_name}': self.{column_name} ")
        elif length:
            models = f"    {column_name} = db.Column(db.{column_type}({length}))"
            to_dict_items.append(f"            '{column_name}': self.{column_name}")
        else:
            models = f"    {column_name} = db.Column(db.{column_type})"
            to_dict_items.append(f"            '{column_name}': self.{column_name}")
        
        moddata.append(models)

    # Join the moddata list into a single string
    moddata_str = '\n'.join(moddata)

    # Create the to_dict method
    to_dict_str = ',\n'.join(to_dict_items)
    to_dict_method = f"""
    def to_dict(self):
        return {{
            'id': self.id,
{to_dict_str}
        }}
    """

    # Join imports
    imports_str = '\n'.join(imports)

    modelcode = f'''
{imports_str}

db = SQLAlchemy()

class {name}(db.Model):
    __tablename__ = '{name.lower()}'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
{moddata_str}

{to_dict_method}
'''
    return modelcode