from tkinter import *
from tkinter import filedialog, messagebox


class NaiveBayesClassifier:
    def __init__(self, master):
        self.master = master
        master.title("Naive Bayes Classifier")

        self.path = StringVar()
        self.path.trace_add('write', self.turn_on_build_button)
        self.bins = IntVar()
        # self.bins.trace_add('write', self.turn_on_build_button)

        self.labelPath = Label(master, text="Directory Path:")
        self.labelPath.place(x=30, y=50)

        vcmd = master.register(self.validate_path)  # we have to wrap the command
        self.entryPath = Entry(master, validate="key", validatecommand=(vcmd, '%P'), textvariable=self.path)
        self.entryPath.place(x=150, y=50, width=350)

        self.labelBins = Label(master, text="Discretization Bins:")
        self.labelBins.place(x=30, y=90)

        vcmd2 = master.register(self.validate_bins)  # we have to wrap the command
        self.entryBins = Entry(master, validate="key", validatecommand=(vcmd2, '%P'))
        self.entryBins.place(x=150, y=90, width=350)

        # -- File Browser Button --
        self.browse_button = Button(master, text="Browse", command=lambda: self.browse_files())
        self.browse_button.place(x=510, y=45, width=80)

        # -- Build Model Button --
        self.build_button = Button(master, text="Build", command=lambda: self.build_model())
        self.build_button.place(x=250, y=130, width=100)
        self.build_button.config(state="disabled")

        # -- Classify Records Button --
        self.classify_button = Button(master, text="Classify", command=lambda: self.classify_rec())
        self.classify_button.place(x=250, y=170, width=100)
        self.classify_button.config(state="disabled")

    def validate_path(self, new_text_path):
        if not new_text_path:  # the field is being cleared
            self.path = ""
            return True
        try:
            self.path = str(new_text_path)
            return True
        except ValueError:
            return False

    def validate_bins(self, new_text_bins):
        if not new_text_bins:  # the field is being cleared
            self.bins = 0
            return True
        try:
            self.bins = int(new_text_bins)
            return True
        except ValueError:
            return False

    def turn_on_build_button(self, *args):
        if self.path != "" and self.bins != 0:
            self.build_button.config(state="normal")

    def browse_files(self):
        folder_path = filedialog.askdirectory(title="Naive Bayes Classifier")
        self.path.set(folder_path)
        self.path = folder_path

    def build_model(self):
        self.classify_button.config(state="normal")
        messagebox.showinfo("Naive Bayes Classifier", "Building classifier using train-set is done!")

    def classify_rec(self):
        messagebox.showinfo("Naive Bayes Classifier", "The classification was completed successfully")


root = Tk()
root.geometry("600x375")
my_gui = NaiveBayesClassifier(root)
root.mainloop()
