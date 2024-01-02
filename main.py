import tkinter
import random
import time
class SpeedTyping():
    def __init__(self,window):
        self.window = window
        self.sentence = self.random_sentence()
        self.user_input = tkinter.StringVar()
        self.typing_start = False
        self.start_time= 0


    def create_widgets(self):
        # create label with sentence
        self.label_sentence = tkinter.Label(self.window,text=self.sentence,font = ("Arial",16))
        self.label_sentence.pack(padx=20,pady=20)
        # create entry field
        self.entry_field =tkinter.Entry(self.window,textvariable=self.user_input,font = ("Arial",16))
        self.entry_field.config(width=50)
        self.entry_field.pack(padx = 20,pady = 40)
        self.entry_field.bind('<Key>', self.start_typing)
        #start timer
        self.result_label = tkinter.Label(self.window,text=time.perf_counter(),font = ("Arial",16))
        self.result_label.pack(padx = 20,pady =30)



    def start_typing(self, event):
        if not self.typing_start:
            self.typing_start = True
            self.start_time = time.time()
    def measuretime(self):
        if self.start_typing:
            end_time = time.time()
            total_time = end_time - self.start_time
            typed_sentence = self.user_input.get()
            words = typed_sentence.split()
            word_count = len(words)
            speed = int(word_count / total_time * 60)  # Words per minute
            self.result_label.config(text=f"Your typing speed: {speed} WPM")


    def random_sentence(self):
        sentence_list = ['I told him I’d spank ',
                        "I ask why she’s ."   
                        "She raised her ",
                        "Every store around "
                        "They got off on"
                         ]
        return random.choice(sentence_list)


def main():
    window = tkinter.Tk()
    typing_test = SpeedTyping(window)
    typing_test.create_widgets()
    typing_test.measuretime()
    window.mainloop()


if __name__ == "__main__":
    main()