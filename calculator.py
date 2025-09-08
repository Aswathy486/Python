import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    current = entry.get()

    if text == "=":
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(0, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Simple Calculator")

entry = tk.Entry(root, font="Arial 20", bd=10, relief=tk.RIDGE, justify=tk.RIGHT)
entry.pack(fill=tk.BOTH, ipadx=8)

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    for btn in row:
        b = tk.Button(frame, text=btn, font="Arial 18", relief=tk.GROOVE)
        b.pack(side="left", expand=True, fill="both")
        b.bind("<Button-1>", click)

root.mainloop()
