import customtkinter as ctk
from Views import LoginView

def main():
    root = ctk.CTk()
    root.geometry("300x250")
    app = LoginView.LoginView(root)
    root.mainloop()

if __name__ == "__main__":
    main()
