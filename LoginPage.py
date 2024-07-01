"""
Program   : LoginPage.py
Author    : Puteri Nurin Aisya binti Ainul Hasni (23035742)
Date      : 27 April 2024

Entry point for the application.
Features included:
    1. Login with username and password.
    2. Sign up to create an account.
    3. Saves user account information to file
    .
"""

from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import json
from ByLuxeCatalog import catalogMain

userfile = "user_account.txt"


class LoginPage:
    def __init__(self, window):
        self.window = window  # class initialized with name "window" for Tk()
        self.window.geometry('1166x718')  # width x height
        self.window.resizable(False, False)  # cannot resize the window whether height or width
        self.window.state('zoomed')  # maximize the window when open
        self.window.title('Login Page')

        # ============ background image ======================================
        self.bg_frame = Image.open('backgroundlogin.png')  # open using PIL module
        photo = ImageTk.PhotoImage(self.bg_frame)  # from PIL module so that Tkinter can display images
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both')  # fill horizontal and vertical

        # ============= Login Frame ==========================================
        self.lgn_frame = Frame(self.window, bg='#f5ece5', width=950, height=600)  # frame widget
        self.lgn_frame.place(x=200, y=70)

        # ============ Left Side Image =======================================
        self.side_image = Image.open('frontlogin3.png')
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.lgn_frame, image=photo, bg='#f5ece5', width=500, height=600)
        self.side_image_label.image = photo
        self.side_image_label.place(x=-2, y=40)

        # ============= LINE ==================================================

        self.frame_line = Canvas(self.lgn_frame, width=950, height=2.0, bg="#45523e", highlightthickness=0)
        self.frame_line.place(x=-2, y=76)

        self.txt = "SHOP NOW"
        self.txt2 = "BYLUXE"
        self.txt3 = "˖✧"
        self.heading = Label(self.lgn_frame, text=self.txt, font=('HELVETICA', 13), bg="#f5ece5",
                             fg='#45523e', bd=5, relief=FLAT)
        self.heading.place(x=45, y=26, width=100, height=30)

        self.heading = Label(self.lgn_frame, text=self.txt2, font=('times new roman', 20), bg="#f5ece5",
                             fg='#45523e', bd=5, relief=FLAT)
        self.heading.place(x=440, y=24, width=110, height=30)

        self.heading = Label(self.lgn_frame, text=self.txt3, font=('times new roman', 16), bg="#f5ece5",
                             fg='#45523e', bd=5, relief=FLAT)
        self.heading.place(x=860, y=26, width=50, height=30)

        # ============ LOGO Log In Image =============================================
        self.sign_in_image = Image.open('logo.png')
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.lgn_frame, image=photo, bg='#f5ece5')
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=650, y=120)

        # ============ Log In label =============================================
        self.sign_in_label = Label(self.lgn_frame, text="Log In", bg="#f5ece5", fg="#4f4e4d",
                                   font=("yu gothic ui", 17, "bold"))
        self.sign_in_label.place(x=685, y=240)

        # ============= Enter username =============================================

        def on_enter(e):  # when cursor go to username box, text in box disappear
            self.usernameLoginpage_entry.delete(0, "end")

        def on_leave(e):  # when fill in, get the username to know it already fill in
            name = self.usernameLoginpage_entry.get()
            if name == "":  # if name is empty, reappear "Username"
                self.usernameLoginpage_entry.insert(0, "Username")

        self.username_label = Label(self.lgn_frame, text="Username", bg="#f5ece5", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))  # change background "username"
        self.username_label.place(x=550, y=310)

        self.usernameLoginpage_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#ad7d50",
                                             fg="white",
                                             font=("yu gothic ui ", 12), insertbackground='#f5ece5')
        self.usernameLoginpage_entry.place(x=580, y=345, width=300)
        self.usernameLoginpage_entry.insert(0, "Username")  # make text "Username" is in the box
        self.usernameLoginpage_entry.bind("<FocusIn>",
                                          on_enter)  # when user click at the box, it will do function on_enter
        self.usernameLoginpage_entry.bind("<FocusOut>", on_leave)  # when user not click

        # ========= Username icon =============================================
        self.username_icon = Image.open('username_icon.png')
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.lgn_frame, image=photo, bg='white')
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=550, y=345)

        # ========= login button===============================================
        self.lgn_button = Image.open('buttonlogin.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg='#f5ece5')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=580, y=455)
        self.login = Button(self.lgn_button_label, text='LOGIN', font=("yu gothic ui", 13, "bold"), width=10, bd=0,
                            bg='#45523e', cursor='hand2', activebackground='#45523e', fg='white', command=self.login)
        self.login.place(x=95, y=10)

        # =========== Sign Up Label ==================================================
        self.sign_label = Label(self.lgn_frame, text='Not a member?', font=("yu gothic ui", 11, "bold"),
                                relief=FLAT, borderwidth=0, background="#f5ece5", fg='#4f4e4d')
        self.sign_label.place(x=620, y=530)
        self.signup_button_label = Button(self.lgn_frame, text="Sign up", font=("yu gothic ui", 11, "bold"),
                                          bg='#98a65d',
                                          cursor="hand2", borderwidth=0, background="#f5ece5",
                                          activebackground="#f5ece5",
                                          fg='#45523e',command=self.signupPage)
        self.signup_button_label.place(x=765, y=523)

        # ========== Enter Password ==================================================

        def on_enter(e):
            self.passwordLoginpage_entry.delete(0, "end")

        def on_leave(e):
            name = self.passwordLoginpage_entry.get()
            if name == "":
                self.passwordLoginpage_entry.insert(0, "Password")

        self.passwordLoginpage_label = Label(self.lgn_frame, text="Password", bg="#f5ece5", fg="#4f4e4d",
                                             font=("yu gothic ui", 13, "bold"))
        self.passwordLoginpage_label.place(x=550, y=380)

        self.passwordLoginpage_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#ad7d50",
                                             fg="white",
                                             font=("yu gothic ui", 12), show="*", insertbackground='#f5ece5')
        self.passwordLoginpage_entry.place(x=580, y=411, width=300)

        self.passwordLoginpage_entry.insert(0, "Password")
        self.passwordLoginpage_entry.bind("<FocusIn>", on_enter)
        self.passwordLoginpage_entry.bind("<FocusOut>", on_leave)

        # ======== Password icon ================
        self.password_icon = Image.open('password_icon.png')
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.lgn_frame, image=photo, bg='white')
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=550, y=411)

        # ========= Show/hide password =========
        self.show_image = ImageTk.PhotoImage(file='show.png')

        self.hide_image = ImageTk.PhotoImage(file='hide.png')

        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white", borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=900, y=411)

    def show(self):
        self.hide_button = Button(self.lgn_frame, image=self.hide_image, command=self.hide, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.hide_button.place(x=900, y=411)
        self.passwordLoginpage_entry.config(show='')  # show real password

    def hide(self):
        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=900, y=411)
        self.passwordLoginpage_entry.config(show='*')  # hide password by masking them with "*"

    # ======================================================================
    # =============== SIGN UP PAGE =========================================
    # ======================================================================

    def signupPage(self):
        self.screen = Toplevel(self.window)  # build a secondary window after self.window, with the name is screen
        # Toplevel window is a separate window that can be used for displaying additional content
        self.screen.title("Sign up")
        self.screen.geometry('1166x718')
        self.screen.resizable(False, False)
        self.screen.state('zoomed')

        self.bg_frame = Image.open('backgroundlogin.png')
        self.bg_photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.screen, image=self.bg_photo)
        self.bg_panel.image = self.bg_photo
        self.bg_panel.pack(fill='both', expand='yes')

        # ============= frame =============================================
        self.screen_frame = Frame(self.screen, bg='#f5ece5', width=500, height=600)
        self.screen_frame.place(x=450, y=70)

        # ============= logo ==============================================
        self.sign_in_image = Image.open('logo.png')
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.screen, image=photo, bg='#f5ece5')
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=620, y=90)

        # ========== instruction ==========================================
        self.signupPage_instruction_label = Label(self.screen, text='Please enter your information',
                                                  font=("yu gothic ui", 11, "bold"), relief=FLAT, borderwidth=0,
                                                  background="#f5ece5", fg='#4f4e4d')
        self.signupPage_instruction_label.place(x=600, y=210)

        # ========= enter username ========================================
        def on_enter(e):
            self.signUpPage_username_entry.delete(0, "end")

        def on_leave(e):
            name = self.signUpPage_username_entry.get()
            if name == "":
                self.signUpPage_username_entry.insert(0, "Username")

        self.signupPage_username_label = Label(self.screen, text='Username', font=("yu gothic ui", 11, "bold"),
                                               relief=FLAT, borderwidth=0, background="#f5ece5", fg='#4f4e4d')
        self.signupPage_username_label.place(x=520, y=240)

        self.signUpPage_username_entry = Entry(self.screen, highlightthickness=0, relief=FLAT, bg="#ad7d50", fg="white",
                                               font=("yu gothic ui ", 12), insertbackground='#f5ece5')
        self.signUpPage_username_entry.place(x=520, y=270, width=350)
        self.signUpPage_username_entry.insert(0, "Username")
        self.signUpPage_username_entry.bind("<FocusIn>", on_enter)
        self.signUpPage_username_entry.bind("<FocusOut>", on_leave)

        # ========== enter password ======================================
        def on_enter(e):
            self.signUpPage_password_entry.delete(0, "end")

        def on_leave(e):
            name = self.signUpPage_password_entry.get()
            if name == "":
                self.signUpPage_password_entry.insert(0, "Password")

        self.signupPage_password_label = Label(self.screen, text='Password', font=("yu gothic ui", 11, "bold"),
                                               relief=FLAT, borderwidth=0, background="#f5ece5", fg='#4f4e4d')
        self.signupPage_password_label.place(x=520, y=300)

        self.signUpPage_password_entry = Entry(self.screen, highlightthickness=0, relief=FLAT, bg="#ad7d50", fg="white",
                                               font=("yu gothic ui ", 12), insertbackground='#f5ece5')
        self.signUpPage_password_entry.place(x=520, y=330, width=350)
        self.signUpPage_password_entry.insert(0, "Password")
        self.signUpPage_password_entry.bind("<FocusIn>", on_enter)
        self.signUpPage_password_entry.bind("<FocusOut>", on_leave)

        # =========== enter name =========================================
        def on_enter(e):
            self.signUpPage_name_entry.delete(0, "end")

        def on_leave(e):
            name = self.signUpPage_name_entry.get()
            if name == "":
                self.signUpPage_name_entry.insert(0, "Name")

        self.signupPage_name_label = Label(self.screen, text='Name', font=("yu gothic ui", 11, "bold"),
                                           relief=FLAT, borderwidth=0, background="#f5ece5", fg='#4f4e4d')
        self.signupPage_name_label.place(x=520, y=360)

        self.signUpPage_name_entry = Entry(self.screen, highlightthickness=0, relief=FLAT, bg="#ad7d50", fg="white",
                                           font=("yu gothic ui ", 12), insertbackground='#f5ece5')
        self.signUpPage_name_entry.place(x=520, y=390, width=350)
        self.signUpPage_name_entry.insert(0, "Name")
        self.signUpPage_name_entry.bind("<FocusIn>", on_enter)
        self.signUpPage_name_entry.bind("<FocusOut>", on_leave)

        # ======== enter number phone=====================================
        def on_enter(e):
            self.signUpPage_numfon_entry.delete(0, "end")

        def on_leave(e):
            name = self.signUpPage_numfon_entry.get()
            if name == "":
                self.signUpPage_numfon_entry.insert(0, "Num. phone")

        self.signupPage_numfon_label = Label(self.screen, text='Num. phone', font=("yu gothic ui", 11, "bold"),
                                             relief=FLAT, borderwidth=0, background="#f5ece5", fg='#4f4e4d')
        self.signupPage_numfon_label.place(x=520, y=420)

        self.signUpPage_numfon_entry = Entry(self.screen, highlightthickness=0, relief=FLAT, bg="#ad7d50", fg="white",
                                             font=("yu gothic ui ", 12), insertbackground='#f5ece5')
        self.signUpPage_numfon_entry.place(x=520, y=450, width=350)
        self.signUpPage_numfon_entry.insert(0, "Num. phone")
        self.signUpPage_numfon_entry.bind("<FocusIn>", on_enter)
        self.signUpPage_numfon_entry.bind("<FocusOut>", on_leave)

        # ========= enter address =======================================
        def on_enter(e):
            self.signUpPage_address_entry.delete(0, "end")

        def on_leave(e):
            name = self.signUpPage_address_entry.get()
            if name == "":
                self.signUpPage_address_entry.insert(0, "Address")

        self.signupPage_address_label = Label(self.screen, text='Address', font=("yu gothic ui", 11, "bold"),
                                              relief=FLAT, borderwidth=0, background="#f5ece5", fg='#4f4e4d')
        self.signupPage_address_label.place(x=520, y=480)

        self.signUpPage_address_entry = Entry(self.screen, highlightthickness=0, relief=FLAT, bg="#ad7d50", fg="white",
                                              font=("yu gothic ui ", 12), insertbackground='#f5ece5')
        self.signUpPage_address_entry.place(x=520, y=510, width=350)
        self.signUpPage_address_entry.insert(0, "Address")
        self.signUpPage_address_entry.bind("<FocusIn>", on_enter)
        self.signUpPage_address_entry.bind("<FocusOut>", on_leave)

        # ========== signup button ======================================
        self.signupPage_button = Image.open('signupbutton.png')
        photo = ImageTk.PhotoImage(self.signupPage_button)
        self.signupPage_button_label = Label(self.screen, image=photo, bg='#f5ece5')
        self.signupPage_button_label.image = photo
        self.signupPage_button_label.place(x=550, y=550)
        self.signup = Button(self.signupPage_button_label, text='SIGN UP', font=("yu gothic ui", 13, "bold"),
                             width=10, bd=0, bg='#45523e', cursor='hand2', activebackground='#45523e', fg='white',
                             command=self.signup)
        self.signup.place(x=95, y=10)

        # ========== back to login page =================================
        self.backtoLogin_button_label = Button(self.screen, text="Back", font=("yu gothic ui", 11, "bold"),
                                               bg='#98a65d',
                                               cursor="hand2", borderwidth=0, background="#f5ece5",
                                               activebackground="#f5ece5", fg='#45523e', command=self.goToLoginPage)
        self.backtoLogin_button_label.place(x=680, y=615)

    def goToLoginPage(self):
        self.screen.destroy()  # close Sign up page
        self.window.deiconify()  # reappear the login page

        # ======== End of Sign Up page ==================================

    def signup(self):
        try:
            # Read existing data from the file
            with open(userfile, "r") as file:
                data = file.read()
                user_dict = json.loads(data)

            # Get user data from the entry fields
            username_signup = self.signUpPage_username_entry.get()
            password_signup = self.signUpPage_password_entry.get()
            name_signup = self.signUpPage_name_entry.get()
            numfon_signup = self.signUpPage_numfon_entry.get()
            address_signup = self.signUpPage_address_entry.get()

            # Check if username already exists
            if username_signup in user_dict:
                messagebox.showerror("Signup Error", "Username already exists. Please choose another username.")
                return

            # Add user data to the dictionary
            user_dict[username_signup] = {
                'password': password_signup,
                'name': name_signup,
                'numfon': numfon_signup,
                'address': address_signup
            }

            # Write updated dictionary to the file
            with open(userfile, 'w') as file:
                json.dump(user_dict, file, indent=2)

            messagebox.showinfo("Signup", "Successfully signed up")
            self.screen.destroy()  # Destroy the signup page window
            self.window.deiconify()  # Reappear the Login Page

        except:
            file = open(userfile, 'w')
            empty_dict = str({})
            file.write(empty_dict)
            file.close()

    def login(self):
        username_login = self.usernameLoginpage_entry.get()
        password_login = self.passwordLoginpage_entry.get()

        try:
            with open(userfile, "r") as file:
                user_dict = json.load(file)

                if username_login in user_dict:
                    if user_dict[username_login]['password'] == password_login:
                        messagebox.showinfo("Login", "Successfully logged in")
                        self.window.destroy()  # Close the LoginPage window  
                        self.catalogPage(username_login)  # Pass username

                    else:
                        messagebox.showerror("Login Error", "Wrong password")
                else:
                    messagebox.showerror("Login Error", "Username not exist, please signup")

        except FileNotFoundError:  # userfile not exist
            messagebox.showerror("Login Error", "No user accounts found")
        except json.JSONDecodeError:  # if there is error parsing the JSON data from userfile
            messagebox.showerror("Login Error", "Error reading user accounts file")

    def catalogPage(self, USERNAME):
        import LxGraphics
        LxGraphics
        catalogMain(USERNAME)


def main():
    window = Tk()  # Create instance of tkinter frame or window from Tk class
    LoginPage(window)  # pass Tkinter to class
    window.mainloop()


if __name__ == '__main__':
    main()
