#writes both lists to file

from tkinter import *
from functools import partial  #to prevent unwanted windows
import random
import re



class Game:
    def __init__(self, parent):

        #Formatting variables...
        self.game_stats_list = [50,6]

        #In actual program this is blank and is populated with user calculations
        self.round_stats_list = ['lead ($0) | lead ($0) | silver ($4) - Cost: $10 | Payback: $4 | Current Balance: $44',
                                 'copper ($2) | lead ($0) | copper ($2) - Cost: $10 | Payback: $4 | Current Balance: $38',
                                 'copper ($2) | lead ($0) | copper ($2) - Cost: $10 | Payback: $4 | Current Balance: $32',
                                 'copper ($2) | copper ($2) | lead ($0) - Cost: $10 | Payback: $4 | Current Balance: $26',
                                 'lead ($0) | gold ($10) | lead ($0) - Cost: $10 | Payback: $10 | Current Balance: $26',
                                 'silver ($4) | copper ($2) | copper ($2) - Cost: $10 | Payback: $8 | Current Balance: $24',
                                 'copper ($2) | copper ($2) | lead ($0) - Cost: $10 | Payback: $4 | Current Balance: $18',
                                 'silver ($4) | lead ($0) | lead ($0) - Cost: $10 | Payback: $4 | Current Balance: $12',
                                 'silver ($4) | gold ($10) | silver ($4) - Cost: $10 | Payback: $18 | Current Balance: $20',
                                 'lead ($0) | lead ($0) | silver ($4) - Cost: $10 | Payback: $4 | Current Balance: $14',
                                 'lead ($0) | lead ($0) | copper ($2) - Cost: $10 | Payback: $2 | Current Balance: $6']

        self.game_frame = Frame()
        self.game_frame.grid()

        #Heading Row
        self.heading_label = Label(self.game_frame, text="Play...",
                                   font="Arial 24 bold", padx=10,
                                   pady=10)
        self.heading_label.grid(row=0)

        #History Button (row=1)
        self.stats_button = Button(self.game_frame,
                                   text="Game Stats",
                                   font="Arial 14", padx=10, pady=10,
                                   command=lambda: self.to_stats(self.round_stats_list, self.game_stats_list))
        self.stats_button.grid(row=1)

    def to_stats(self, game_history, game_stats):
        GameStats(self, game_history, game_stats)


class GameStats:
    def __init__(self, partner, game_history, game_stats):

        print(game_history)

        #disable help button
        partner.stats_button.config(state=DISABLED)

        heading = "Arial 12 bold"
        content = "Arial 12"

        #Sets up child window (ie: help box)
        self.stats_box = Toplevel()

        #If users press cross at top, closes help and 'releases' help button

        self.stats_box.protocol('WM_DELETE_WINDOW', partial(self.close_stats,
                                                            partner))

        #Set up GUI Frame
        self.stats_frame = Frame(self.stats_box)
        self.stats_frame.grid()

        #Set up Help heading (row=0)
        self.stats_heading_label = Label(self.stats_frame, text="Game Statistics",
                                         font="arial 19 bold")
        self.stats_heading_label.grid(row=0)

        #To Export <instructionns> (row=1)
        self.export_instructions = Label(self.stats_frame,
                                         text="Here are your Game Statistics."
                                              "Please use the Export button to "
                                              "access the results of each "
                                              "round that you played", wrap=250,
                                         font="arial 10 italic",
                                         justify=LEFT, fg="green",
                                         padx=10, pady=10)
        self.export_instructions.grid(row=1)

        #Starting Balance (row=2)
        self.details_frame = Frame(self.stats_frame)
        self.details_frame.grid(row=2)

        #Starting balance (row 2.0)

        self.start_balance_label = Label(self.details_frame,
                                         text="Starting Balance:", font=heading,
                                         anchor="e")
        self.start_balance_label.grid(row=0, column=0, padx=0)

        self.start_balance_value_label = Label(self.details_frame, font=content,
                                               text="${}".format(game_stats[0]),anchor="w")
        self.start_balance_value_label.grid(row=0, column=1, padx=0)

        #Current Balance (row 2.2)
        self.current_balance_label = Label(self.details_frame,
                                           text="Current Balance", font=heading,
                                           anchor="e")
        self.current_balance_label.grid(row=1, column=0, padx=0)

        self.current_balance_value_label = Label(self.details_frame, font=content,
                                                 text='${}'.format(game_stats[1]), anchor="w")
        self.current_balance_value_label.grid(row=1, column=1, padx=0)

        if game_stats[1] > game_stats[0]:
            win_loss = "Amount Won: "
            amount=game_stats[1] - game_stats[0]
            win_loss_fg = "green"
        else:
            win_loss = "Amount Lost: "
            amount = game_stats[0] - game_stats[1]
            win_loss_fg="#660000"

        #Amount won/lost (row2.3)
        self.wind_loss_label = Label(self.details_frame,
                                     text=win_loss, font=heading,
                                     anchor="e")
        self.wind_loss_label.grid(row=2, column=0, padx=0)

        self.wind_loss_value_label = Label(self.details_frame, font=content,
                                           text="${}".format(amount),
                                           fg=win_loss_fg,anchor="w")
        self.wind_loss_value_label.grid(row=2, column=1, padx=0)

        #Rounds Played (row 2.4)
        self.games_played_label = Label(self.details_frame,
                                        text="Round Played: ", font=heading,
                                        anchor="e")
        self.games_played_label.grid(row=4, column=0, padx=0)

        self.games_played_value_label = Label(self.details_frame, font=content,
                                              text=len(game_history),
                                              anchor="w")
        self.games_played_value_label.grid(row=4, column=1, padx=0)

        #Dismiss & Export button (row=3)
        self.dismiss_export_frame = Frame(self.stats_frame)
        self.dismiss_export_frame.grid(row=3, pady=10)

        #Export Button
        self.export_button = Button(self.dismiss_export_frame, text="Export",
                                    font="Arial 12 bold",
                                    highlightbackground="#00008B",
                                    command=lambda: self.export(game_history, game_stats))
        self.export_button.grid(row=0, column=0)

        #dismiss button
        self.dismiss_button = Button(self.dismiss_export_frame, text="Dismiss",
                                     font="arial 12 bold",
                                     highlightbackground="#AA4A44",
                                     command=partial(self.close_stats, partner))
        self.dismiss_button.grid(row=0, column=1)

    def export(self, game_history, game_stats):
        Export(self, game_history, game_stats)

    def close_stats(self, partner):
        #put stats button back to normal
        partner.stats_button.config(state=NORMAL)
        self.stats_box.destroy()



class Export:
    def __init__(self, partner, game_history, game_stats):

        print(game_history)

        background="#DCDCDC"

        #disable export button
        partner.export_button.config(state=DISABLED)

        #Sets up child window (ie:export box)
        self.export_box = Toplevel()

        #if user click press at the top, closes export and releases export button
        self.export_box.protocol('WM_DELETE_WINDOW',
                                 partial(self.close_export, partner))

        #set up GUI Frame
        self.export_frame = Frame(self.export_box, width = 300, bg=background)
        self.export_frame.grid()

        #set up Export heading (row0)
        self.how_heading = Label(self.export_frame,
                                 text="Export / Instructions",
                                 font="arial 25 bold", bg=background)
        self.how_heading.grid(row=0)

        #export text (label, row 1)
        self.export_text = Label(self.export_frame, text="Enter a file name "
                                 "in the box below "
                                 "and press the Save "
                                 "button to save your "
                                 "game history "
                                 "to a text file. ",
                                 justify=LEFT, width=40,
                                 bg=background, wrap=250)
        self.export_text.grid(row=1)

        #Warning text(label, row 2)
        self.export_text = Label(self.export_frame, text="If the filename "
                                 "you entered below "
                                 "already exists "
                                 "its content will "
                                 "be replaced with "
                                 "your calculation "
                                 "history",
                                 justify=LEFT, bg="#ffafaf", fg="maroon",
                                 font="arial 10 italic", wrap=225, padx=10,
                                 pady=10)
        self.export_text.grid(row=2, pady=10)

        #Filename Entry Box (row 3)
        self.filename_entry = Entry(self.export_frame, width=20,
                                    font="Arial 14 bold", justify=CENTER)
        self.filename_entry.grid(row=3, pady=10)

        #Error message labels (initally blank, row4)
        self.save_error_label = Label(self.export_frame, text="", fg="maroon",
                                      bg=background)
        self.save_error_label.grid(row=4)

        #Save/Cancel Frame (row 5)
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=5, pady=10)

        #Save and Cancel Buttons (row 0 of save_cancel_frame)
        self.save_button = Button(self.save_cancel_frame, text="Save",
                                  highlightbackground="#00008B",
                                  fg="white", font="arial 15 bold",
                                  command=partial(lambda: self.save_history(partner, game_history, game_stats)))
        self.save_button.grid(row=0, column=0)

        self.cancel_button = Button(self.save_cancel_frame, text="Cancel",
                                    highlightbackground="#AA4A44",
                                    fg="white", font="arial 15 bold",
                                    command=partial(self.close_export, partner))
        self.cancel_button.grid(row=0, column=1)

    def save_history(self, partner, game_history, game_stats):

        #Regular expression
        valid_char="[A-Za-z0-9_]"
        has_error="no"

        filename=self.filename_entry.get()
        print(filename)

        for letter in filename:
            if re.match(valid_char,letter):
                continue
            elif letter == "":
                problem="(no spaces allowed)"
            else:
                problem=("(no {}'s allowed)".format(letter))
            has_error="yes"
            break
        if filename=="":
            problem="can't be blank"
            has_error="yes"

        if has_error=="yes":
            #display error message
            self.save_error_label.config(text="Invalid filename - {}".format(problem))
            #Change entry box
            self.filename_entry.config(bg="#ffafaf")
            print()

        else:
            #if there are no errors, generate text file nd then close dialogue
            #add .txt suffix
            filename=filename+".txt"

            #create file to hold data
            f = open(filename, "w+")

            #Heading for stats
            f.write("Game Statistics\n\n")

            #Game Stats
            for round in game_stats:
                f.write(round + "\n")

            #Heading for Rounds
            f.write("\nRound Details\n\n")

            #add new line the end of each item
            for item in game_history:
                f.write(item + "\n")

            #close file
            f.close()

            #close dialogue
            self.close_export(partner)


    def close_export(self, partner):
        #put export button back to normal
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()

#main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box Game")
    something = Game(root)
    root.mainloop()
