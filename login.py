from tkinter import *
from tkinter import messagebox

import admin
import staff
from database import Database

# creating a database object
db = Database()

class Login:
    def __init__(self, root):
        self.root = root

        self.username = StringVar()
        self.password = StringVar()

        # Background Color
        self.root.config(bg="#5856a0")

        # Call the tkinter frame to the window
        self.loginControlFrame()

    """CTA Methods"""

    # login method to redirect to the next frames
    def login_func(self):
        nhan_vien = db.login(self.txtUsername.get(), self.txtPassword.get())
        if nhan_vien:
            self.loginFrame.destroy()
            self.rightFrame.destroy()
            if nhan_vien[0][5]:
                staff.StaffControls(self.root)
                # Employee screen
            else:
                admin.AdminControls(self.root)
                # Admin screen

        else:
            messagebox.showerror("Lỗi!", "Vui lòng kiểm tra lại tài khoản của bạn!")
            self.username.set("")
            self.password.set("")


    def loginControlFrame(self):
        # Login Frame Configurations
        self.loginFrame = Frame(self.root, bg="white")
        self.loginFrame.pack(side=LEFT, fill=X, padx=60)
        self.login_frame_title = Label(self.loginFrame, text="Đăng nhập", font=("Impact", 35), bg="white",
                                       fg="#5856a0")
        self.login_frame_title.grid(row=0, columnspan=2, padx=10, pady=20, sticky="w")

        # Username
        self.labelUsername = Label(self.loginFrame, text="Username", font=("Times New Roman", 16, "bold"), bg="white",
                                   fg="#5856a0")
        self.labelUsername.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.txtUsername = Entry(self.loginFrame, textvariable=self.username, font=("Times New Roman", 15), width=30,
                                 bd=5)
        self.txtUsername.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        # Password
        self.labelPassword = Label(self.loginFrame, text="Password", font=("Times New Roman", 16, "bold"), bg="white",
                                   fg="#5856a0")
        self.labelPassword.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.txtPassword = Entry(self.loginFrame, textvariable=self.password, font=("Times New Roman", 15), width=30,
                                 bd=5, show="*")
        self.txtPassword.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        # Login Button
        self.btnLogin = Button(self.loginFrame, command=self.login_func, text="Login", bd=0, cursor="hand2",
                               fg="white", bg="#5856a0", width=10, font=("Impact", 15))
        self.btnLogin.grid(row=3, column=1, padx=10, sticky="e")

        # empty label for spacing in grid
        self.emptyLabel = Label(self.loginFrame, font=("Times New Roman", 16, "bold"), bg="white",
                                fg="#5856a0")
        self.emptyLabel.grid(row=4, column=1, padx=10, pady=5, sticky="w")

        # Right Side Frame as Welcome Message
        self.rightFrame = Frame(self.root, bg="#5856a0")
        self.rightFrame.pack(side=RIGHT)

        self.labelCompanyName = Label(self.rightFrame, text="Quản lý cửa hàng", font=("Goudy Old Style", 55),
                                      bg="#5856a0",
                                      fg="white")
        self.labelCompanyName.grid(row=0, column=2, columnspan=2, padx=10)
        self.labelDesc = Label(self.rightFrame, text="Store Management", font=("Times New Roman", 25, "italic"),
                               bg="#5856a0",
                               fg="white")
        self.labelDesc.grid(row=1, column=2, columnspan=2, padx=10, pady=6)
