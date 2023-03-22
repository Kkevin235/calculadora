import tkinter as tk

class Calculator(tk.Frame):
    def __init__(self, master=None, size=250):
        super().__init__(master, width=size, height=size)
        self.master = master
        self.master.title("Calculadora")

        # Marco para entradas y salida
        input_frame = tk.Frame(self)
        input_frame.pack(padx=5, pady=5)

        # Campos de entrada
        self.a = tk.Entry(input_frame, width=5)
        self.a.grid(row=0, column=0, padx=5, pady=5)
        self.b = tk.Entry(input_frame, width=5)
        self.b.grid(row=0, column=1, padx=5, pady=5)

        # Etiqueta de salida
        output_frame = tk.Frame(input_frame)
        output_frame.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        self.result_label = tk.Label(output_frame, text="Resultado:")
        self.result_label.pack(side="left")

        self.result_value = tk.Label(output_frame, text="0", width=5)
        self.result_value.pack(side="left")

        # Botones de operadores
        operator_frame = tk.Frame(self)
        operator_frame.pack(padx=5, pady=5)

        for i, operator in enumerate(["+", "-", "*", "/"]):
            button = tk.Button(operator_frame, text=operator, width=5, height=2,
                               command=lambda op=operator: self.operation(op))
            button.grid(row=i // 2, column=i % 2, padx=5, pady=5)

        # Botones de resultado y limpieza
        bottom_frame = tk.Frame(self)
        bottom_frame.pack(padx=5, pady=5)

        self.result_button = tk.Button(bottom_frame, text="=", width=5, height=2, command=self.result)
        self.result_button.grid(row=0, column=0, padx=5, pady=5)
        self.clear_button = tk.Button(bottom_frame, text="C", width=5, height=2, command=self.clear)
        self.clear_button.grid(row=0, column=1, padx=5, pady=5)

        self.pack()

    def operation(self, operator):
        a, b = map(int, (self.a.get(), self.b.get()))
        result = eval(f"{a} {operator} {b}")
        self.a.delete(0, tk.END)
        self.b.delete(0, tk.END)
        self.a.insert(tk.END, str(result))
        self.result_value.config(text=str(result))

    def result(self):
        self.master.focus()
        self.operation("+")

    def clear(self):
        self.a.delete(0, tk.END)
        self.b.delete(0, tk.END)
        self.a.insert(tk.END, "0")
        self.b.insert(tk.END, "0")
        self.result_value.config(text="0")

root = tk.Tk()
app = Calculator(master=root, size=300)
app.mainloop()
