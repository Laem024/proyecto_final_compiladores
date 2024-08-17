import tkinter as tk
from tkinter import scrolledtext
from compiler.lexer import lexer, lexer_errors  # Asegúrate de que lexer_errors esté correctamente importado
from compiler.parser import parser, parser_errors
from compiler.codegen import generate_code, generate_javascript, symbol_table

class CompilerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Compilador en Python")

        self.input_label = tk.Label(root, text="Ingresa una función en Java:")
        self.input_label.grid(row=0, column=0, columnspan=2)

        self.text_input = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=10)
        self.text_input.grid(row=1, column=0, columnspan=2)

        self.run_button = tk.Button(root, text="Compilar", command=self.compile_code)
        self.run_button.grid(row=2, column=0, columnspan=2)

        self.tokens_label = tk.Label(root, text="Tokens:")
        self.tokens_label.grid(row=3, column=0)

        self.tokens_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=10)
        self.tokens_text.grid(row=4, column=0)

        self.symbol_table_label = tk.Label(root, text="Tabla de Símbolos:")
        self.symbol_table_label.grid(row=3, column=1)

        self.symbol_table_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=10)
        self.symbol_table_text.grid(row=4, column=1)

        self.intermediate_code_label = tk.Label(root, text="Código Intermedio:")
        self.intermediate_code_label.grid(row=5, column=0, columnspan=2)

        self.intermediate_code_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=100, height=10)
        self.intermediate_code_text.grid(row=6, column=0, columnspan=2)

        self.javascript_code_label = tk.Label(root, text="Código en JavaScript:")
        self.javascript_code_label.grid(row=7, column=0, columnspan=2)

        self.javascript_code_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=100, height=10)
        self.javascript_code_text.grid(row=8, column=0, columnspan=2)

        self.errors_label = tk.Label(root, text="Errores:")
        self.errors_label.grid(row=9, column=0, columnspan=2)

        self.errors_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=100, height=10)
        self.errors_text.grid(row=10, column=0, columnspan=2)

    def compile_code(self):
        # Limpiar las áreas de salida antes de mostrar los nuevos resultados
        self.tokens_text.delete("1.0", tk.END)
        self.symbol_table_text.delete("1.0", tk.END)
        self.intermediate_code_text.delete("1.0", tk.END)
        self.javascript_code_text.delete("1.0", tk.END)
        self.errors_text.delete("1.0", tk.END)
        lexer_errors.clear()
        parser_errors.clear()

        code = self.text_input.get("1.0", tk.END).strip()
        lexer.input(code)

        # Análisis léxico
        tokens_output = []
        while True:
            tok = lexer.token()
            if not tok:
                break
            tokens_output.append(f'{tok.type}: {tok.value}')

        self.tokens_text.insert(tk.END, "\n".join(tokens_output) + "\n")

        # Mostrar errores léxicos
        if lexer_errors:
            self.errors_text.insert(tk.END, "Errores Léxicos:\n" + "\n".join(lexer_errors) + "\n")

        # Análisis sintáctico y generación de código intermedio y JavaScript
        try:
            result = parser.parse(code)
            if result:
                code_gen = generate_code(result)
                js_code_gen = generate_javascript(result)
                self.intermediate_code_text.insert(tk.END, code_gen + "\n")
                self.symbol_table_text.insert(tk.END, str(symbol_table) + "\n")
                self.javascript_code_text.insert(tk.END, js_code_gen + "\n")
        except Exception as e:
            self.errors_text.insert(tk.END, f"Error: {str(e)}\n")

        # Mostrar errores sintácticos
        if parser_errors:
            self.errors_text.insert(tk.END, "Errores Sintácticos:\n" + "\n".join(parser_errors) + "\n")

if __name__ == "__main__":
    root = tk.Tk()
    gui = CompilerGUI(root)
    root.mainloop()
