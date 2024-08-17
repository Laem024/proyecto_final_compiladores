symbol_table = {}

def generate_code(parsed):
    if parsed[0] == 'function':
        function_type = parsed[1]
        function_name = parsed[2]
        params = ', '.join([f'{p[1]} {p[2]}' for p in parsed[3]])
        body = '\n'.join([generate_code(stmt) for stmt in parsed[4]])
        return f'{function_type} {function_name}({params}) {{\n{body}\n}}'
    elif parsed[0] == 'assign':
        symbol_table[parsed[2]] = parsed[1]
        return f'{parsed[1]} {parsed[2]} = {generate_code(parsed[3])};'
    elif parsed[0] == 'return':
        return f'return {generate_code(parsed[1])};'
    elif parsed[0] == 'binop':
        return f'{generate_code(parsed[2])} {parsed[1]} {generate_code(parsed[3])}'
    elif parsed[0] == 'num':
        return str(parsed[1])
    elif parsed[0] == 'id':
        return parsed[1]

def generate_javascript(parsed):
    if parsed[0] == 'function':
        params = ', '.join([f'{p[2]}' for p in parsed[3]])
        body = '\n'.join([generate_javascript(stmt) for stmt in parsed[4]])
        return f'function {parsed[2]}({params}) {{\n{body}\n}}'
    elif parsed[0] == 'assign':
        js_type = 'let'
        return f'{js_type} {parsed[2]} = {generate_javascript(parsed[3])};'
    elif parsed[0] == 'return':
        return f'return {generate_javascript(parsed[1])};'
    elif parsed[0] == 'binop':
        return f'{generate_javascript(parsed[2])} {parsed[1]} {generate_javascript(parsed[3])}'
    elif parsed[0] == 'num':
        return str(parsed[1])
    elif parsed[0] == 'id':
        return parsed[1]
