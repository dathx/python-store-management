from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import login
from database import Database

# creating a database object
db = Database()


class StaffControls:
    def __init__(self, root):
        self.root = root

        self.thanhToan = StringVar()

        # Call the tkinter frames to the window
        self.staffControlsFrame()
        self.staffFrameButtons()
        self.tableOutputFrame()
        self.viewProducts()

    def staffControlsFrame(self):
        # staff Control Frame Configurations
        self.entriesFrame = Frame(self.root, bg="#5856a0")
        self.entriesFrame.pack(side=TOP, fill=X)
        self.staff_frame_title = Label(self.entriesFrame, text="Staff Control Panel",
                                       font=("Goudy old style", 35),
                                       bg="#5856a0",
                                       fg="white")
        self.staff_frame_title.grid(row=0, columnspan=2, padx=10, pady=20, sticky="w")

        # Instructor Gender
        self.labelGender = Label(self.entriesFrame, text="Phương thức thanh toán", font=("Times New Roman", 16, "bold"),
                                 bg="#5856a0",
                                 fg="white")
        self.labelGender.grid(row=1, column=2, padx=10, pady=5, sticky="w")
        self.comboGender = ttk.Combobox(self.entriesFrame, textvariable=self.thanhToan, font=("Times New Roman", 15),
                                        width=28,
                                        state="readonly")
        self.comboGender['values'] = ("Thanh toán trực tiếp", "Thẻ tín dụng")
        self.comboGender.grid(row=1, column=3, padx=10, pady=5, sticky="w")

    # event trigger Method to display the chosen data from the TreeView back in respective fields
    def getData(self, event):
        try:
            self.selectedRow = self.out.focus()
            self.selectedData = self.out.item(self.selectedRow)
            self.chosenRow = self.selectedData["values"]
        except IndexError as error:
            pass

    def viewProducts(self):
        self.out.delete(*self.out.get_children())  # emptying the table before reloading
        for row in db.viewProducts():
            self.out.insert('', 'end', values=tuple(row))

    def staffFrameButtons(self):
        # Button Frame Configurations
        self.buttonsFrame = Frame(self.entriesFrame, bg="#5856a0")
        self.buttonsFrame.grid(row=9, column=1, padx=10, pady=10, sticky="w", columnspan=8)

        # Add a new Record
        self.btnAdd = Button(self.buttonsFrame, command='', text="Chọn mua", bd=0, cursor="hand2",
                             bg="#EADDF7",
                             fg="#5856a0", width=15, font=("Impact", 15))
        self.btnAdd.grid(row=0, column=0, padx=10)

        # Update Selected Record
        self.btnUpdate = Button(self.buttonsFrame, command='', text="Thanh toán", bd=0,
                                cursor="hand2",
                                bg="#EADDF7",
                                fg="#5856a0", width=15, font=("Impact", 15))
        self.btnUpdate.grid(row=0, column=1, padx=10)

        # Reset Widget Inputs
        self.btnReset = Button(self.buttonsFrame, command='', text="Xóa", bd=0, cursor="hand2",
                               bg="#EADDF7", fg="#5856a0", width=10, font=("Impact", 15))
        self.btnReset.grid(row=0, column=3, padx=10)

        # LogOut
        self.btnLogOut = Button(self.entriesFrame, command=self.logOut, text="Log Out", bd=0, cursor="hand2",
                                bg="#EADDF7",
                                fg="#5856a0", width=15, font=("Impact", 15))
        self.btnLogOut.grid(row=0, column=5, padx=20, sticky="e")


    def logOut(self):
        self.entriesFrame.destroy()
        self.buttonsFrame.destroy()
        self.tableFrame.destroy()
        login.Login(self.root)

    def tableOutputFrame(self):
        # Treeview Frame Configurations
        self.tableFrame = Frame(self.root, bg="#DADDE6")
        self.tableFrame.place(x=0, y=400, width=1200, height=560)
        self.yScroll = Scrollbar(self.tableFrame)
        self.yScroll.pack(side=RIGHT, fill=Y)

        # ttk style object to add configurations
        self.style = ttk.Style()
        self.style.configure("mystyle.Treeview", font=('Calibri', 12),
                             rowheight=70)
        self.style.configure("mystyle.Treeview.Heading", font=('Times New Roman', 14, "bold"), sticky="w")

        # Formatting the output table view
        self.out = ttk.Treeview(self.tableFrame, yscrollcommand=self.yScroll.set, columns=(0, 1, 2, 3, 4, 5),
                                style="mystyle.Treeview")
        self.out.column("0", width=70)
        self.out.heading("0", text="Mã SP")
        self.out.column("1", width=450)
        self.out.heading("1", text="Tên sản phẩm")
        self.out.heading("2", text="Giá")
        self.out.column("3", width=150)
        self.out.heading("3", text="Số lượng")
        self.out.column("4", width=150)
        self.out.heading("4", text="Hình ảnh")
        self.out.heading("5", text="Mô tả")
        self.out['show'] = 'headings'

        # Virtual Events to trigger methods
        self.out.bind("<ButtonRelease-1>", self.getData)

        # TreeView output layout configurations
        self.out.pack(fill=BOTH)
        self.yScroll.config(command=self.out.yview)
