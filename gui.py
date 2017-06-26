import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from plotter import CbbStats
import matplotlib.pyplot as plt
from matplotlib import style


import tkinter as tk
from tkinter import ttk
style.use("ggplot")


LARGE_FONT = ("Verdana", 12)

f = Figure(figsize=(5, 5), dpi=100)
ax = f.add_subplot(111)


class CbbCompareApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.iconbitmap(self, default="bballicon.ico")
        tk.Tk.wm_title(self, "CBB Compare")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageThree):
            frame = F(container, self)

            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text=("""ALPHA college basketball comparison application.
                                Use at your own risk."""), font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Agree",
                             command=lambda: controller.show_frame(PageThree))
        button1.pack()

        button2 = ttk.Button(self, text="Disagree",
                             command=quit)
        button2.pack()




class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button3 = ttk.Button(self, text="Visit Graph Page",
                             command=lambda: controller.show_frame(PageThree))
        button3.pack()

class PageThree(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Graph Page!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()

        #f = Figure(figsize=(5, 5), dpi=100)
        #ax = f.add_subplot(111)
        #a.plot([1, 2, 3, 4, 5, 6, 7, 8],[5,6,1,3,8,9,3,5])
        team = input("Enter Team Name: ")
        #df = CbbStats(team).player_game_stats_dataframe()
        df = CbbStats(team).team_schedule_dataframe()
        #df['PPG'].plot(kind='bar', ax=ax)
        #df.plot(kind='bar', ax=ax)
        #df['MIN'].plot(kind='bar', ax=ax)
        df['DIFFERENTIAL'].plot(kind="bar", rot=75, ax=ax)


        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


app = CbbCompareApp()
app.mainloop()
