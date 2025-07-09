import customtkinter as ctk
import sys
window = ctk.CTk()
window.title('Fenster')
window.geometry('800x500')
window.resizable(True, True)

nameLabel = ctk.CTkLabel(window, text="Name:")
nameLabel.grid(row = 0, column = 0, padx = 10, pady=10)

nameValue = ctk.CTkEntry(window, placeholder_text="enter your name")
nameValue.grid(row = 0, column = 1, padx = 10, pady=10)

ageLabel = ctk.CTkLabel(window, text="Age:")
ageLabel.grid(row = 1, column = 0, padx = 10, pady=10)

ageValue = ctk.CTkEntry(window, placeholder_text="enter your age")
ageValue.grid(row = 1, column = 1, padx = 10, pady=10)


messageLabel = ctk.CTkLabel(window, text="")
messageLabel.grid(row = 2, column = 0, padx = 10, pady=10)

def quit_handler():
    sys.exit()
    
def button_event():
    name = nameValue.get()
    age = ageValue.get()
    message = f'hello {name} you are {age} years old !'
    messageLabel.configure(text = message)


    print(message)

button = ctk.CTkButton(window, text="show message", command=button_event)
button.grid(row = 10, column = 1, padx = 10, pady=10)

quit = ctk.CTkButton(window, text="quit", command=quit_handler)
quit.grid(row = 10, column = 0, padx = 10, pady=10)


window.mainloop()