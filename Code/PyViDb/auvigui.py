#!/usr/bin/python
# TODO optional GUI

# python 2.7 < 3
import Tkinter as tk

def main():
    root = tk.Tk()
    components(root)
    root.mainloop()

def components(frame):
    quit = tk.Button(frame)
    quit["text"]    =   "QUIT"
    quit["fg"]      =   "red"
    quit["command"] =   frame.quit
    quit.pack({"side":"left"})

    label =tk.Label(frame)
    label["text"]   =   "This is just a Test"
    label.pack({"side":"right"})

if __name__ == '__main__':
    main()
