import tkinter as tk

def convert():
    cm = float(cm_entry.get())
    m = cm / 100
    km = cm / 100000
    m_entry.delete(0, tk.END)
    km_entry.delete(0, tk.END)
    m_entry.insert(0, str(m))
    km_entry.insert(0, str(km))

root = tk.Tk()
root.title("Length Converter")

cm_label = tk.Label(root, text="Centimeters:")
m_label = tk.Label(root, text="Meters:")
km_label = tk.Label(root, text="Kilometers:")

cm_entry = tk.Entry(root)
m_entry = tk.Entry(root)
km_entry = tk.Entry(root)

convert_button = tk.Button(root, text="Convert", command=convert)

cm_label.grid(row=0, column=0)
cm_entry.grid(row=0, column=1)
convert_button.grid(row=0, column=2)
m_label.grid(row=1, column=0,)
m_entry.grid(row=1, column=1,)
km_label.grid(row=2, column=0,)
km_entry.grid(row=2, column=1,)

root.mainloop()