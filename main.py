from tkinter import *
import login

#main method
def main():
    root = Tk()
    root.title("Quản lý cửa hàng")
    root.geometry("1200x930+50+50")
    root.resizable(False, True)

    #Parsing the root window to the Login class
    #Initiating the System
    login.Login(root)

    root.mainloop()

if __name__ == '__main__':
    main()
