import PyPDF2 # pip install PyPDF2
import tkinter as tk
from tkinter import filedialog

window = tk.Tk()
window.title("PDF Reader")
window.geometry("800x600")

text = tk.Text(window, bd=5, font=("Arial", 12))
text.pack(expand=True, fill='both', padx=10, pady=10)

def clear_text():
   text.delete(1.0, tk.END)

def open_pdf():
   file = filedialog.askopenfilename(title="Select a PDF", filetype=(("PDF    Files","*.pdf"),("All Files","*.*")))
   if file:
      pdf_file= PyPDF2.PdfReader(file)
      for i in range(len(pdf_file.pages)):
         page = pdf_file.pages[i]
         content=page.extract_text()
         text.insert(tk.END, content)

def quit_app():
   window.destroy()

menu = tk.Menu(window)
window.config(menu=menu)
file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_pdf)
file_menu.add_command(label="Clear", command=clear_text)
file_menu.add_command(label="Quit", command=quit_app)


window.mainloop()