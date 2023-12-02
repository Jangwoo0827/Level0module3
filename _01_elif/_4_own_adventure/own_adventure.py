from tkinter import simpledialog, messagebox, Tk

# TODO Tell the user a story, but give them options so they can decide the
#  path of the plot.
#  Use pop-ups, if statements, and your imagination to make an interesting
#  story


#THIS STORY IS REALLY WERID.


if __name__ == '__main__':
    w = Tk()
    w.withdraw()
    a = simpledialog.askstring(title=None, prompt="Do you want to be weird? (yes or no)")
    if a == "no":
        messagebox.showinfo(title=None, message="YOU CHOSE EXIT!!")
        messagebox.showinfo(title=None, message="FAILED")
        exit()
    elif a == "yes":
        a = simpledialog.askstring(title=None, prompt="Do you want to kill dragon? (yes or no)")
    if a == "no":
        messagebox.showinfo(title=None, message="YOU BECAME WEIRD!!")
        messagebox.showinfo(title=None, message="FAILED")
        exit()
    elif a == "yes":
        a = simpledialog.askstring(title=None, prompt="Do you want to grow first? (yes or no)")
    if a == "no":
        messagebox.showinfo(title=None, message="YOU DIED!!")
        messagebox.showinfo(title=None, message="FAILED")
        exit()
    elif a == "yes":
        a = simpledialog.askstring(title=None, prompt="You killed dragon. Do you want to be famous? (yes or no)")
    if a == "yes":
        messagebox.showinfo(title=None, message="YOU BECAME FAMOUS WEIRD KNIGHT!!")
        messagebox.showinfo(title=None, message="FAILED")
        exit()
    elif a == "no":
        messagebox.showinfo(title=None, message="You became an great unknown knight.")
    pass
