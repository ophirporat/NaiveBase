from os import listdir
from tkinter import *
from tkinter import filedialog, messagebox

from model import Model
from preprocessing import Preprocessing as pr


class NaiveBayesClassifier:
    def __init__(self, master):
        self.master = master
        master.title("Naive Bayes Classifier")

        # -- Path and bins variables and labels --
        self.path = StringVar()
        self.pathStr = ""
        self.path.trace_add('write', self.turn_on_build_button)
        self.bins = IntVar()

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

    # -- Checks if the path from register is valid --
    def validate_path(self, new_text_path):
        if not new_text_path:  # the field is being cleared
            self.path = ""
            return True
        try:
            self.pathStr = str(new_text_path)
            return True
        except ValueError:
            return False

    # -- Checks if the bins from register is valid --
    def validate_bins(self, new_text_bins):
        if not new_text_bins:  # the field is being cleared
            self.bins = 0
            return True
        try:
            self.bins = int(new_text_bins)
            self.turn_on_build_button()
            return True
        except ValueError:
            return False

    # -- Validate if files are in the folder --
    def turn_on_build_button(self, *args):
        try:
            if type(self.bins) is int and not ("Structure.txt" not in listdir(self.pathStr) or "train.csv" not in
                                               listdir(self.pathStr) or "test.csv" not in listdir(
                        self.pathStr)) and self.bins > 0:
                self.build_button.config(state="normal")
        except:
            pass

    # -- Select folder from files browser --
    def browse_files(self):
        folder_path = filedialog.askdirectory(title="Naive Bayes Classifier")
        self.path.set(folder_path)
        self.pathStr = folder_path

    # -- Builds the model --
    def build_model(self):
        p = pr(self.pathStr, self.bins)
        message = p.preprocess()
        if(message != "all good"):
            messagebox.showinfo("Naive Bayes Classifier",message)
            return
        self.model = Model(p.train_df, p.test_df, 2, p.attributes, self.pathStr)  # m=1
        self.model.build_model()
        self.classify_button.config(state="normal")
        messagebox.showinfo("Naive Bayes Classifier", "Building classifier using train-set is done!")

    # -- Classify the records --
    def classify_rec(self):
        self.model.classify_records()
        messagebox.showinfo("Naive Bayes Classifier", "The classification was completed successfully")


root = Tk()
root.geometry("600x375")
my_gui = NaiveBayesClassifier(root)
root.mainloop()
