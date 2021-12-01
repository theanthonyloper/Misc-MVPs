
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk 
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
import numpy as np
import matplotlib.pyplot as plt

import tkinter as tk
from tkinter import ttk, LEFT, RIGHT, IntVar


LARGE_FONT= ("Verdana", 12)
style.use("ggplot")

f = Figure(figsize=(5,5), dpi=100)
axis = f.add_subplot(111)

def animate(i):   
    pullData = open("testydconeoz.txt","r").read()
    abcData = open("testabc.txt","r").read()
    abcs_vals = abcData.split('\n')
    dataList = pullData.split('\n')
    tList = []
    yList = []
    dcList = []
    ozList = []
    abclist = []

    for letter in abcs_vals:
        if len(letter)> 0:
            abclist.append(round(float(letter), 2))
    for eachLine in dataList:
        if len(eachLine) > 1:
            t, y, dc, oneoz = eachLine.split(',')
            tList.append(float(t))
            yList.append(float(y))
            dcList.append(int(dc[0:1]))
            ozList.append(int(oneoz[0:1]))
    a, b, c, d = abclist[:]        
    axis.clear()
    axis.plot(tList, yList, '-r', label=r'$y = ' + str(a) + 'e^{-' + str(b) + '(x-' + str(d) + ')} + ' + str(c) + '$')
    axis.plot(tList, dcList, '--b', label = '8 oz drip coffee')
    axis.plot(tList, ozList, '--g', label = '1 oz drip coffee')

    axis.set_xlabel('Military Time in Hours')
    axis.set_ylabel('Equivalent Oz of Black Coffee')
    axis.set_title('Caffeine Availability Throughout the Day')
    axis.legend(loc='upper right')


def get_inps(input_t, input_q, v):
    drink_sclr = v.get()  #Get inputs: Type, Time, & Amount               
    t1 = input_t.get(1.0, "end-1c")
    oz1 = input_q.get(1.0, "end-1c")

    #  Cast as maybe
    
def plotData(input_t, input_q, v, lbl):         #  Maybe this is doing way too much and should be broken up
    drink_sclr = float(v.get())  #Get inputs: Type, Time, & Amount 
    t1 = float(input_t.get(1.0, "end-1c"))
    oz1 = float(input_q.get(1.0, "end-1c"))
#     drink_sclr, t1, oz1 = 64, 14, 3
        
    mg = oz1 * drink_sclr
    #  Time, 8oz dc pts, & 1 oz
    t = np.linspace(0 + t1, 24 + t1, 250)   
    ones = np.ones(len(t))
    dc = 8 * ones
    oneoz =  ones
    ##########  Exponential Decay Params
    a = (8/96)*mg #y intercept at t = 0 --> scaled to oz of dc
    b = np.log(1/2)/(-5.5)#half life scalar in units per hours.  Large B --> Quick decay, small B --> Long decay
    c = 0 #shifts plot up(+) or down (-)
    d = t1 #shifts plot right(+) or left(-)
    ##########  Exponential Points & Leftovers
    y = a*(np.exp(-b*(t - d))) + c
    y_EOD = a*(np.exp(-b*(18 - d))) + c
    y_midnight = a*(np.exp(-b*(24 - d))) + c

    ########## Update Label with Summary
    full_msg = f"""
    When: {t1}\nHow much: {oz1} oz

    About how many ounces of black drip coffee\nare left in system at 6pm?
    ~ {round(y_EOD, 1)} oz

    At midnight?
    ~ {round(y_midnight, 1)} oz
"""
    lbl.config(text = full_msg)  #  This is the style for the outputs

    all_data = np.array([t, y, dc, oneoz])
    data_t = np.transpose(all_data)
    np.savetxt('testydconeoz.txt', data_t, delimiter=',')
    abc_data = np.array([a, b, c, d])
    abcs = np.transpose(abc_data)
    np.savetxt('testabc.txt', abcs, delimiter=',')

class AutoGrapher(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Live Plotter")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        
        frame = GraphPage(container, self)
        self.frames[GraphPage] = frame
        frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(GraphPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

class GraphPage(tk.Frame):

    def __init__(self, parent, controller):       
        tk.Frame.__init__(self, parent)
        title = "Caffeine Metabolic Dynamics"  #\n\nWhat's the time until approx\n1 oz of drip coffee in system?"
        label = tk.Label(self, text=title, font=LARGE_FONT)
        label.pack(pady=10,padx=10)  
        
        v = tk.IntVar()
        v.set(1)  # initializing the choice, i.e. Python

        drink_dict = [("Black Coffee", 96/8),  #mg/oz
                        ("Espresso", 64/1),
                        ("Black Tea", 47/8),
                        ("Green Tea", 28/8)]
        
        left_frame = tk.Frame(self)
        left_frame.pack(side = 'left', fill="both", expand = True)

        right_frame = tk.Frame(self)
        right_frame.pack(side = 'left', fill="both", expand = True)

        vtop_frame = tk.Frame(right_frame)
        vtop_frame.pack(side = 'top', fill="both", expand = True )

        top_frame = tk.Frame(right_frame)
        top_frame.pack(side = 'top', fill="both", expand = True)

        btm_frame = tk.Frame(right_frame)
        btm_frame.pack(side = 'top', fill="both", expand = True)

        ########## Prompts & Inputs
        txt_lbl_k = tk.Label(vtop_frame, text = """What drink?
""")
        txt_lbl_k.pack(side = 'top', fill="both", expand = True)

        for drink, mg in drink_dict:
            tk.Radiobutton(vtop_frame, 
                           text=drink,
                           padx = 20, 
                           variable=v, 
#                            command=plotData,
                           value=mg).pack(anchor=tk.W)

        txt_lbl_t = tk.Label(top_frame, text = """
What hour did you drink it?
(Military - 16.5 for 4:30pm, etc.)""", anchor="w")
        txt_lbl_t.pack(side = 'top', fill="both", expand = True)
        
        input_t = tk.Text(top_frame, #bd = 10,
                        height = 1,
                        width = 10)  #, anchor="e", justify=RIGHT)
        input_t.pack(side = 'top', pady = 10, fill="y", expand = True)

        txt_lbl_q = tk.Label(top_frame, text = """
How many fluid ounces (oz) did you drink?
(Espresso shots are about 1 oz)""", anchor="w")
        txt_lbl_q.pack(side = 'top', fill="both", expand = True)
        
        input_q = tk.Text(top_frame, #bd = 10,
                        height = 1,
                        width = 10)  #, anchor="e", justify=RIGHT)
        input_q.pack(side = 'top', pady = 10, fill="y", expand = True)  

        # Label & Button Creation
        lbl = tk.Label(btm_frame, text = "", anchor="w", justify=LEFT)
        lbl.pack(side = 'bottom', fill="both", expand = True)
        
        printButton = tk.Button(top_frame, bd = 3,
                                text = "Plot Data",
                                command = lambda: plotData(input_t, input_q, v, lbl))  #   
        printButton.pack(pady = 10, fill="both", expand = True)
        
        #  Plot!
        canvas = FigureCanvasTkAgg(f, left_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        toolbar = NavigationToolbar2Tk(canvas, left_frame)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

app = AutoGrapher() 
ani = animation.FuncAnimation(f, animate, interval=2500)
app.lift()
app.mainloop()
