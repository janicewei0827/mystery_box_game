from tkinter import *
from functools import partial  # To prevent unwanted windows
import random


class Start:
    def __init__(self, parent):

        #GUI get starting balance and stakes
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        #Set Initial balance to zero
        self.starting_funds = IntVar()
        self.starting_funds.set(0)

        #Mystery Heading (row 0)
        self.mystery_box_label = Label(self.start_frame, text="Mystery Box Game",
                                       font="Arial 19 bold")
        self.mystery_box_label.grid(row=0)

        #Help Button (row 1)
        self.help_button = Button(self.start_frame, text="Help",
                                  font=("Arial", "14"),
                                  padx=10, pady=10, command=self.help)
        self.help_button.grid(row=1, pady=10)

    def help(self):
        print("You asked for help.")
        get_help = Help(self)

class Help:
    def __init__(self, partner):
        background="#DCDCDC"

        #disable help button
        partner.help_button.config(state=DISABLED)

        #Sets up child window (ie:help box)
        self.help_box = Toplevel()

        #if user click press at the top, closes help and releases help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        #set up GUI Frame
        self.help_frame = Frame(self.help_box, bg=background, width=300)
        self.help_frame.grid()

        #set up Help heading (row0)
        self.how_heading = Label(self.help_frame, text="Help / Instructions",
                                 font="arial 25 bold", bg=background)
        self.how_heading.grid(row=0)

        help_text="""
Choose an amount to play with and then choose the stakes. High stakes cost more per round but you can win more as well.\n
When you enter the play area, you will see three mystery boxes. To reveal the contents of the boxes, click the 'Open Boxes' button. It doesn't have enough money to play, the button will turn red and you will need to quit the game.\n  
The contents of the boxes will be added to your balance. The boxes could contain ...\n
Low: Lead($0)|Copper($1)|Silver($2)|Gold($5)
Medium: Lead($0)|Copper($2)|Silver($4)|Gold($10)
High: Lead($0)|Copper($3)|Silver($6)|Gold($15)

If each box contains gold, you will win $30(low stakes). If they contain copper, silver and gold, you would receive $13 and so on. """


        #help text (label, row 1)
        self.help_text = Label(self.help_frame, text=help_text,
                               justify=LEFT, width=40, bg=background, wrap=250,
                               padx=10,pady=10)
        self.help_text.grid(row=1)

        #Dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text= "Dismiss",
                                  width=20, highlightbackground="#AA4A44", font="arial 17 bold",
                                  command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        #put help button back to normal
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Convertor")
    something = Start(root)
    root.mainloop()
