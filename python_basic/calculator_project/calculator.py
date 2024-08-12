import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")

        # Entry widget for showing the input and results
        self.result_var = tk.StringVar()
        self.entry = tk.Entry(root, textvariable=self.result_var, font=("Arial", 18), bd=10, relief="ridge", justify="right")
        self.entry.grid(row=0, column=0, columnspan=4)

        # Define buttons and their positions
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('C', 5, 0, 4)  # 'C' button spans 4 columns
        ]

        for button in buttons:
            print(f"button {button}")
            if len(button) == 4:  # Button with colspan
                text, row, column, colspan = button
                colspan = colspan
            else:  # Button without colspan
                text, row, column = button
                colspan = 1

            btn = tk.Button(root, text=text, font=("Arial", 18), width=4, height=2, command=lambda t=text: self.on_button_click(t))
            btn.grid(row=row, column=column, columnspan=colspan, sticky="nsew")

        # Configure row and column weights
        for i in range(6):
            root.grid_rowconfigure(i, weight=1)
            root.grid_columnconfigure(i, weight=1)

        self.reset()

    def on_button_click(self, char):
        if char == 'C':
            self.reset()
        elif char == '=':
            try:
                expression = self.result_var.get()
                result = str(eval(expression))
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        else:
            current_text = self.result_var.get()
            self.result_var.set(current_text + char)

    def reset(self):
        self.result_var.set("")

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
