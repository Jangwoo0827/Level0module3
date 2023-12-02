from tkinter import Tk, simpledialog, messagebox


if __name__ == '__main__':
    w = Tk()
    w.withdraw()
    # TODO: Look at the AreYouHappy.png image
    #       Use pop-ups to recreate the chart using if and elif statements
    a = simpledialog.askstring(title=None, prompt="Are you happy? (yes or no)")
    if a == "yes":
        messagebox.showinfo(title=None, message="Keep doing whatever you're doing.")
        exit()
    elif a == "no":
        a = simpledialog.askstring(title=None, prompt="Do you want to be happy? (yes or no)")
    if a == "yes":
        messagebox.showinfo(title=None, message="Change something.")
        exit()
    elif a == "no":
        messagebox.showinfo(title=None, message="Keep doing whatever you're doing.")
        exit()
    pass
