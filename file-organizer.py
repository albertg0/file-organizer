import os
import os.path
import shutil
import re


try:
    from Tkinter import *

except ImportError:
    import tkinter as tk
    import tkinter.ttk as ttk

bgColor = '#262a30'
ugly_patterns = '(?i)(-BTN|720px265|-Snahp|sujaidr|XviD-YL4|XviD-AFG|\[Kyle-E\]|-BRISK\[\]|-CRAVERS|PRiME|CodeDonut|AC3|DADDY|INTERNAL|2009|hdtv-lol|.HDTV.x264-KILLERS\[eztv\]|-BATV|-SVA|X264|.x264-AVS\eztv\]|-W4F|x264|-MiNDTHEGAP|-DIMENSION|-AVS|.PROPER|.HDTV.|.x264|.x264-AVS\[eztv\]|-KILLERS|-FLEET|\[eztv\]|\[ettv\]|-FUM)'


class FileCopier():

    def startCopy(self):
        dir_files = os.listdir()
        print(dir_files)
        self.rename_files(dir_files)
        self.copy_to_dir()

    def rename_files(self, dir_files):

        whatdo = "\t\t[ RENAMING FILES ] "
        self.textbox.insert(tk.END, whatdo+'\n')

        print (whatdo)

        for file in dir_files:
            if os.path.isfile(file) :
                if file.endswith(".mkv") or file.endswith(".avi") or file.endswith(".mp4"):
                    previous_name = file

                    if re.search(ugly_patterns,previous_name):

                        previous_name = re.sub(ugly_patterns, '', previous_name)
                        previous_name = previous_name.split(".")

                        i = len(file)-3
                        j = len(file)

                        file_ext = {}
                        file_ext[file] = file[i : j]

                        previous_name = " ".join(previous_name)
                        new_filename = previous_name[0:i]
                        x = len(new_filename)-4

                        new_filename = new_filename[0: x]
                        new_filename += "." + file_ext[file]

                        print(new_filename)

                        self.textbox.insert(tk.END,new_filename+'\n')
                        new_filename.strip();
                        os.rename(file,new_filename)

    def copy_to_dir(self):

        whatdo = "\n\t\t[ COPYING FILES ]"
        src = "D:\\Tv Shows"
        dest_dir = os.listdir(src)
        file_list = os.listdir()

        print (whatdo)
        self.textbox.insert(tk.END,whatdo+'\n')
        for file in file_list:
            if file.endswith(".mkv") or file.endswith(".avi") or file.endswith(".mp4"):
                for folder in dest_dir:

                    rex = re.escape(folder) + r".(S[0-9][0-9]| E[0-9][0-9])"
                    if re.match(rex,file,re.IGNORECASE) and not os.path.isfile(os.path.join(src,folder)):

                        print(src + '\\' + folder + " <- "+file + "\n")
                        self.textbox.insert(tk.END, src + '\\' + folder + ' <- ' + file + '\n')
                        shutil.copy(file,src+"\\"+folder)
                        os.remove(file)

        src = "F:\\Tv Shows"
        dest_dir = os.listdir(src)
        file_list = os.listdir()

        print (whatdo)

        for file in file_list:
            if file.endswith(".mkv") or file.endswith(".avi") or file.endswith(".mp4"):
                for folder in dest_dir:

                    rex = re.escape(folder) + r".(S[0-9][0-9]| E[0-9][0-9])"
                    if re.match(rex,file,re.I) and not os.path.isfile(os.path.join(src, folder)):

                        print( src + '\\' + folder + " <- "+file + "\n")

                        self.textbox.insert(tk.END, src + '\\' + folder + ' <- ' + file + '\n')
                        shutil.copy(file, src+"\\"+folder)
                        os.remove(file)

        src = "E:\\Tv Shows"
        dest_dir = os.listdir(src)
        file_list = os.listdir()

        print(whatdo)

        for file in file_list:
            if file.endswith(".mkv") or file.endswith(".avi") or file.endswith(".mp4"):
                for folder in dest_dir:

                    rex = re.escape(folder) + r".(S[0-9][0-9]| E[0-9][0-9])"
                    if re.match(rex,file,re.I) and not os.path.isfile(os.path.join(src, folder)):

                        print( src + '\\' + folder + " <- "+file + "\n")

                        self.textbox.insert(tk.END, src + '\\' + folder + ' <- ' + file + '\n')
                        shutil.copy(file, src+"\\"+folder)
                        os.remove(file)

    def hello(self):
     
        pWindow = tk.Tk()
        pWindow.config(bg=bgColor)
        pTextbox = tk.Text(pWindow,bg=bgColor,fg='#fff')
        pTextbox.grid(row=0,column=0,columnspan=2)
        pTextbox.insert(tk.END,ugly_patterns)

        startButton = tk.Button(pTextbox,text='add pattern',bg=bgColor,fg='#fff')
        patternEntryLabel = tk.Label(pWindow,bg=bgColor,fg='#FFF',text='Add New Pattern:')
        patternEntryLabel.grid(row=1,column=0)
        patternEntry = tk.Entry(pWindow,bg=bgColor,fg='#fff',width=50)
        patternEntry.grid(row=1,column=1)
        

    def __init__(self, parent):

        labelframe_color = 'cyan'
        parent.wm_title("File Copier")
        parent.iconbitmap(r'c:\Python27\DLLs\py.ico')

        labelFrameColor = '#0092bf'
        windowWidth = 600
        windowHeight = 600

        #patternButton = tk.Button(root, text="Patterns", fg='#FFF', relief=tk.FLAT, bg=bgColor, command=self.hello)
        #patternButton.grid(row=0,column=0, sticky='N')

        labelframe0 = tk.LabelFrame(parent, bg=labelframe_color) 
        startButton = tk.Button(root, text="Start", relief=tk.FLAT, fg="#fff", bg=bgColor, command=self.startCopy)
        self.textbox = tk.Text(root, bg=bgColor, fg='#fff', wrap='char', width=55, height=25, relief=tk.FLAT) 
        labelframe0.config(height=1, width=windowWidth)
        self.textbox.grid(padx=25, pady=27, row=0, column=0, columnspan=4)
        labelframe0.grid(row=2, column=0, columnspan=4)

        startButton.grid(row=3, column=0, columnspan=4)

        #parent.config(menu=menubar)
        parent.configure(background=bgColor)
        parent.resizable(width=False, height=False)
        parent.geometry('{}x{}'.format(windowWidth, windowHeight))




if __name__ == '__main__':
    root = tk.Tk()
    FileCopier(root)
    root.mainloop()








