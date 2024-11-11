import customtkinter as ctk
from Systems.AuthenticationSystem import AuthenticationSystem as Auth
from tkinter import messagebox, Tk, StringVar

class LoginView:
	def __init__(self, master):
		self.master = master
		master.title("Login")

		self.usernameVar = StringVar()
		self.passwordVar = StringVar()

		self.usernameLabel = ctk.CTkLabel(master, text="Username")
		self.usernameLabel.pack()

		self.usernameEntry = ctk.CTkEntry(master, textvariable=self.usernameVar)
		self.usernameEntry.pack()

		self.passwordLabel = ctk.CTkLabel(master, text="Password")
		self.passwordLabel.pack()

		self.passwordEntry = ctk.CTkEntry(master, textvariable=self.passwordVar, show="*")
		self.passwordEntry.pack()

		self.loginButton = ctk.CTkButton(master, text="Login", command=self.login)
		self.loginButton.pack()

	def login(self):
		username = self.usernameVar.get()
		password = self.passwordVar.get()
		response = Auth.login(username,password)
		if response:  # If the login was successful
			# Start another process here
			self.master.destroy()  # Close the login window
		else:  # If the login was not successful
			messagebox.showerror("Error", "Invalid username or password!")  # Show an error message

def main():
	root = Tk()
	loginView = LoginView(root)
	root.mainloop()

if __name__ == "__main__":
	main()
