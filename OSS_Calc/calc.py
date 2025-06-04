import tkinter as tk


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x400")

        self.expression = ""

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # 버튼 생성
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['=']
        ]

        for row in buttons:
            frame = tk.Frame(root)
            frame.pack(expand=True, fill="both")
            for char in row:
                btn = tk.Button(
                    frame,
                    text=char,
                    font=("Arial", 18),
                    command=lambda ch=char: self.on_click(ch)
                )
                btn.pack(side="left", expand=True, fill="both")

        # 키보드 입력 처리용 키맵. 키=event.keysym, 값=버튼의 char
        self.ALLOW_KEYS = {str(x): str(x) for x in range(10)}
        self.ALLOW_KEYS |= {
            "period": ".",
            "plus": "+",
            "minus": "-",
            "asterisk": "*",
            "slash": "/",
            "equal": "=",
            "Return": "=",  # 엔터키는 =키의 동작에 대응
            "Escape": "C",  # Esc 키는 초기화 키에 대응
            "BackSpace": "⌫",  # PR#1에 대한 지원
            "exclam": "!",  # PR#11에 대한 지원
            "percent": "%",  # PR#48에 대한 지원
        }

        self.root.bind("<Key>", self.bind_keys)

    def bind_keys(self, event):
        keysym = event.keysym
        if keysym in self.ALLOW_KEYS:
            self.on_click(self.ALLOW_KEYS[keysym])

    def on_click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "에러"
        else:
            self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)



