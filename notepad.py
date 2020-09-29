from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

if __name__ == "__main__":
    root = Tk()
    root.title("Notepad!")
    root.geometry("450x500")
    root.wm_iconbitmap("1.ico")


    def newfile() :
        global file
        root.title("Untitled-Notepad")
        file = None
        text_area.delete(1.0, END)  #"1.0" refers to pehli line ke 0th character se lekar end(END) tak sab kuch delete kar do

    def openfile():
        global file
        file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

        if file == "":
            file = None

        else:
            root.title(os.path.basename(file) + " - Notepad")
            text_area.delete(1.0, END)
            f = open(file, "r")
            text_area.insert(1.0, f.read())
            f.close()


    def savefile():
        global file
        if file == None:    #Agar new file h to 
            file = asksaveasfilename(initialfile = "Untitled.txt", defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")] )

            if file == "":  #Agar file khai h to kuch mat karo
                file = None

            else:
                #Saving new file here
                f = open(file, "w")
                f.write(text_area.get(1.0, END))
                f.close()
                root.title(os.path.basename(file) + "-Notepad")
                print("File Saved Successfully...........") #Just to check ki file save hui ki nhi. Chaho to comment out bhi kar sakte ho



        else:
                #Saving old file here
                f = open(file, "w")
                f.write(text_area.get(1.0, END))
                f.close()

    def cut():
        text_area.event_generate(("<<Cut>>"))   #This is handled by Tkinter internally

    def copy():
        text_area.event_generate(("<<Copy>>"))

    def paste():
        text_area.event_generate(("<<Paste>>"))

    def about():
        tmsg.showinfo("About", "This is developed by R@thi Industries")
        
    def quit_app():
        root.destroy()



#Definitions of all the commands
    #Here goes the text area:
    text_area = Text(root, font="lucida 19")
    file=None
    text_area.pack(expand=TRUE, fill=BOTH)  #"expand" means jab aap expand karte ho to apka text area  parent ki poori width le lega

    

    #Now let's create menubar
    menubar = Menu(root)

#File menu starts
    file_menu = Menu(menubar, tearoff=0)

    #To open a new file:
    file_menu.add_command(label="New", command=newfile)

    #To open an already existing file
    file_menu.add_command(label="Open", command=openfile)

    #To open the current file
    file_menu.add_command(label="Save", command=savefile)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=quit_app)   #You can also write "command=quit" as quit is internal command and hence need not to be defined

    menubar.add_cascade(label="File", menu=file_menu)
    
#File menu ends




#Edit menu starts
    edit_menu = Menu(menubar, tearoff=0)

    #To cut:
    edit_menu.add_command(label="Cut", command=cut)

    #To copy
    edit_menu.add_command(label="Copy", command=copy)
    edit_menu.add_separator()
    #To paste
    edit_menu.add_command(label="Paste", command=paste)
    
    

    menubar.add_cascade(label="Edit", menu=edit_menu)
    
#Edit menu ends


#Help menu starts

    help_menu = Menu(menubar, tearoff=0)

    help_menu.add_command(label="About Notepad", command=about)
    menubar.add_cascade(label="Help", menu=help_menu)
#Help menu ends

    root.config(menu=menubar)
    


    #Adding scrollbar
    scroll = Scrollbar(text_area)
    scroll.pack(side=RIGHT, fill=Y)
    scroll.config(command=text_area.yview)
    text_area.config(yscrollcommand=scroll.set)

root.mainloop()     