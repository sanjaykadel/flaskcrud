def routefile(data):
    name = data['ModelName'].lower()
    routecode = f'''
from views import create_{name}, get_{name}s, get_{name}, update_{name}, delete_{name}

def register_routes(app):
    app.add_url_rule('/{name}s', 'create_{name}', create_{name}, methods=['POST'],strict_slashes=False)
    app.add_url_rule('/{name}s', 'get_{name}s', get_{name}s, methods=['GET'],strict_slashes=False)
    app.add_url_rule('/{name}s/<int:id>', 'get_{name}', get_{name}, methods=['GET'],strict_slashes=False)
    app.add_url_rule('/{name}s/<int:id>', 'update_{name}', update_{name}, methods=['PUT'],strict_slashes=False)
    app.add_url_rule('/{name}s/<int:id>', 'delete_{name}', delete_{name}, methods=['DELETE'],strict_slashes=False)
    
    '''
    return routecode