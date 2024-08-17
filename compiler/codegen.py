symbol_table = {}

def generate_code(parsed):
    if parsed[0] == 'assign':
        symbol_table[parsed[2]] = parsed[1]
        return f'{parsed[1]} {parsed[2]} = {generate_code(parsed[3])};'
    elif parsed[0] == 'binop':
        return f'{generate_code(parsed[2])} {parsed[1]} {generate_code(parsed[3])}'
    elif parsed[0] == 'num':
        return str(parsed[1])
    elif parsed[0] == 'id':
        return parsed[1]

def generate_javascript(parsed):
    if parsed[0] == 'assign':
        js_type = convert_type_to_js(parsed[1])
        return f'let {parsed[2]} = {generate_javascript(parsed[3])};'
    elif parsed[0] == 'binop':
        return f'{generate_javascript(parsed[2])} {parsed[1]} {generate_javascript(parsed[3])}'
    elif parsed[0] == 'num':
        return str(parsed[1])
    elif parsed[0] == 'id':
        return parsed[1]

def convert_type_to_js(java_type):
    if java_type in ['int', 'float', 'double']:
        return 'let'
    return 'let'
