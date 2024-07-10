from tkinter import *
import pyqrcode 
import png
from tkinter import filedialog
from PIL import Image, ImageTk

root = Tk()
root.title("QR Code Generator")
root.geometry('500x500')
root.configure(bg='#add8e6')

def save_qr_code():
    # File dialog to save the QR code image
    save_path = filedialog.asksaveasfilename(title="Save Image as", filetypes=[("PNG File", ".png"), ("All Files", "*.*")])

    if save_path:
        if not save_path.endswith(".png"):
            save_path = f'{save_path}.png'
        
        # Create QR code from entry box text
        qr_code = pyqrcode.create(entry_field.get())
        # Save QR code as PNG file
        qr_code.png(save_path, scale=5)
        
        # Load QR code image to display on screen
        global qr_image
        qr_image = ImageTk.PhotoImage(Image.open(save_path))
        
        # Update label with the new QR code image
        qr_label.config(image=qr_image)
        
        # Clear entry box and show a finished message
        entry_field.delete(0, END)
        entry_field.insert(0, "QR GENERATED")

def clear_fields():
    entry_field.delete(0, END)
    qr_label.config(image='')


# Entry field for input text
entry_field = Entry(root, font=("Helvetica", 18))
entry_field.pack(pady=20)

# Button to generate the QR code
generate_button = Button(root, text="Create QR Code", command=save_qr_code, font=("Helvetica", 10))
generate_button.pack(pady=20)

# Button to clear the entry field and image
clear_button = Button(root, text="Clear", command=clear_fields, font=("Helvetica", 10))
clear_button.pack()

# Label to display the generated QR code image
qr_label = Label(root, text='')
qr_label.pack(pady=20)

root.mainloop()
