#import the necessary code libraries
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np 
import pandas as pd
from tkinter import Tk, filedialog
import math



#1st input option function (A)
def from_data_points_excel():
    #create the graphic interface for the file explorer
    root = Tk()
    root.withdraw() 

    #open the file explorer, allow user to select the Excel file to open
    file_path = filedialog.askopenfilename(
    title="Select Excel File",
    filetypes=[("Excel files", "*.xlsx *.xls")]
)
    #save the Excel file data (from the sheet titled 'Conversion') to a python dataframe 
    if file_path:
        df = pd.read_excel(file_path, 'Conversion')
        print(df.head())
    else:
        print("No file selected.")


    #extract the variables (spreadsheet columns) needed to create the Hildebrand graph
    l_stance_time = df['Mean L % Stance Time']
    l_stance_cycle = df['Mean L % Stance Time']
    temporal_symmetry = df['Temporal Symmetry'] * 100
    r_stance_time = df['Mean R % Stance Time']
    r_cycle_toe_strike = 50 - (df['Temporal Symmetry'] * 100)
    r_toe_strike = df['Mean R % Stance Time'] - (df['Temporal Symmetry'] * 100)
    y_label = ['Left', 'Right']

    l_standard_deviation = l_stance_time[1]
    r_standard_deviation = r_stance_time[1]
    num_terms = 6 #fix this one
    r_confidence_interval =  1.96*(r_standard_deviation/(num_terms)**(1/2)) 
    l_confidence_interval =  1.96*(l_standard_deviation/(num_terms)**(1/2))


    #create a graph of a specific size (width,height) in inches
    plt.figure(figsize=(6, 2))

    #plot right foot strike bar
    p3=plt.barh( y=y_label[1],  width=r_stance_time[0], height=0.4, left = temporal_symmetry[0],  align='center', color='black', edgecolor='black')
    #plot right foot strike bar right error
    p6=plt.barh( y=y_label[1],  width=r_confidence_interval, height=0.4, left = temporal_symmetry[0] + r_stance_time[0],  align='center', color='lightgrey', edgecolor='black')
    #plot right foot strike bar left error
    p6=plt.barh( y=y_label[1],  width=r_confidence_interval, height=0.4, left = temporal_symmetry[0] - r_confidence_interval,  align='center', color='lightgrey', edgecolor='black')

    if r_cycle_toe_strike[0] > 0: #if the right foot strikes again before 150%
        #plot second right foot strike bar
        p4=plt.barh( y=y_label[1],  width=r_cycle_toe_strike[0], height=0.4, left=150-r_cycle_toe_strike[0], align='center', color='black', edgecolor='black')
        #plot second right foot strike bar
        p9=plt.barh(y=y_label[1],  width=r_confidence_interval, height=0.4, left=150-r_cycle_toe_strike[0]-r_confidence_interval, align='center',color='lightgrey', edgecolor='black')
    #plot initial right foot step
    p5=plt.barh( y=y_label[1],  width=r_toe_strike[0], height=0.4, align='center', color='black', edgecolor='black')
    #plot initial right foot step error
    p8=plt.barh( y=y_label[1],  width=r_confidence_interval, height=0.4, left=r_toe_strike[0], align='center', color='lightgrey', edgecolor='black')

    #plot initial left foot step
    p1=plt.barh( y=y_label[0],  width=l_stance_time[0], height=0.4, align='center', color='black', edgecolor='black' )
    #plot initial  left foot step error
    p10=plt.barh( y=y_label[0],  width=l_confidence_interval, height=0.4, left=l_stance_time[0], align='center',  color='lightgray', edgecolor='black')

    if l_stance_cycle[0] > 50: #if the second left foot strike goes past 150%
        #plot the second left foot strike up to 150%
        p2=plt.barh(y=y_label[0], width=50, height=0.4, left=100,  align='center', color='black', edgecolor='black' )
        
    else:
        #plot the second left foot strike
        p2=plt.barh(y=y_label[0], width=l_stance_cycle[0], height=0.4, left=100, align='center', color='black',  edgecolor='black' )
        #plot the second left foot strike right error
        p11=plt.barh( y=y_label[0],  width=l_confidence_interval, height=0.4, left=100+l_stance_cycle[0], align='center', color='lightgrey', edgecolor='black')
    #plot the second left foot strike left error
    p12=plt.barh( y=y_label[0],  width=l_confidence_interval, height=0.4, left=100-l_confidence_interval, align='center', color='lightgrey', edgecolor='black')
    
    #add labels to the graph
    plt.xlabel('Gait Cycle (%)')
    plt.ylabel('Foot')
    plt.xticks(np.arange(0, 151, step=50)) 

    #plot the Hildebrand graph
    plt.show()

#2nd input option function (B)
def from_data_ranges_excel():

    #create the graphic interface for the file explorer
    root = Tk()
    root.withdraw() 

    #open the file explorer, allow user to select the Excel file to open
    file_path = filedialog.askopenfilename(
    title="Select Excel File",
    filetypes=[("Excel files", "*.xlsx *.xls")]
    )    
    #save the Excel file data (from the sheet titled 'Raw Data') to a python dataframe 
    if file_path:
        df = pd.read_excel(file_path, 'Test B')
        print(df.head())
    else:
        print("No file selected.")


    #extract the variables (spreadsheet columns) needed to create the Hildebrand graph
    l_stance_time = df['Mean L % Stance Time']
    num_terms = len(l_stance_time)
    l_stance_time = sum(l_stance_time) / num_terms
    l_stance_cycle = l_stance_time
    temporal_symmetry = df['Temporal Symmetry'] * 100
    temporal_symmetry = sum(temporal_symmetry) / num_terms
    r_stance_time = df['Mean R % Stance Time']
    r_stance_time = sum(r_stance_time) / num_terms
    r_cycle_toe_strike = 50 - (temporal_symmetry)
    #temporal_symmetry_cycle = temporal_symmetry * 100 #delete
    r_toe_strike = r_stance_time - (temporal_symmetry)
    y_label = ['Left', 'Right']

    
    l_standard_deviation =  np.std(df['Mean L % Stance Time'])
    r_standard_deviation = np.std(df['Mean R % Stance Time'])
    r_confidence_interval = 1.96*(r_standard_deviation/(num_terms)**(1/2)) 
    l_confidence_interval = 1.96*(l_standard_deviation/(num_terms)**(1/2))


    #create a graph of a specific size (width,height) in inches
    plt.figure(figsize=(6, 2))

    #plot the bars for the right foot
    p3=plt.barh( y=y_label[1],  width=r_stance_time, height=0.4, left = temporal_symmetry,  align='center', color='black', edgecolor='black')
    #plot right foot strike bar right error
    p6=plt.barh( y=y_label[1],  width=r_confidence_interval, height=0.4, left = temporal_symmetry + r_stance_time,  align='center', color='lightgrey', edgecolor='black')
    #plot right foot strike bar left error
    p6=plt.barh( y=y_label[1],  width=r_confidence_interval, height=0.4, left = temporal_symmetry - r_confidence_interval,  align='center', color='lightgrey', edgecolor='black')

    if r_cycle_toe_strike > 0:#if the right foot strikes again before 150%
        #plot second right foot strike bar
        p4=plt.barh( y=y_label[1],  width=r_cycle_toe_strike, height=0.4, left=150-r_cycle_toe_strike, align='center', color='black', edgecolor='black')
        #plot second right foot strike bar error
        p9=plt.barh(y=y_label[1],  width=r_confidence_interval, height=0.4, left=150-r_cycle_toe_strike-r_confidence_interval, align='center',color='lightgrey', edgecolor='black')
     #plot initial right foot step
    p5=plt.barh( y=y_label[1],  width=r_toe_strike, height=0.4, align='center', color='black', edgecolor='black')
    #plot initial right foot step error
    p8=plt.barh( y=y_label[1],  width=r_confidence_interval, height=0.4, left=r_toe_strike, align='center', color='lightgrey', edgecolor='black')

    #plot initial left foot step
    p1=plt.barh( y=y_label[0],  width=l_stance_time, height=0.4, align='center', color='black', edgecolor='black' )
    #plot initial  left foot step error
    p10=plt.barh( y=y_label[0],  width=l_confidence_interval, height=0.4, left=l_stance_time, align='center',  color='lightgray', edgecolor='black')

    if l_stance_cycle > 50: #if the second left foot strike goes past 150%
        #plot the second left foot strike up to 150%
        p2=plt.barh(y=y_label[0], width=50, height=0.4, left=100,  align='center', color='black', edgecolor='black' )
       
    else:
        #plot the second left foot strike
        p2=plt.barh(y=y_label[0], width=l_stance_cycle, height=0.4, left=100, align='center', color='black',  edgecolor='black' )
        #plot the second left foot strike right error
        p11=plt.barh( y=y_label[0],  width=l_confidence_interval, height=0.4, left=100+l_stance_cycle, align='center', color='lightgrey', edgecolor='black')
    #plot the second left foot strike left error
    p12=plt.barh( y=y_label[0],  width=l_confidence_interval, height=0.4, left=100-l_confidence_interval, align='center', color='lightgrey', edgecolor='black')
    
    #add labels to the graph
    plt.xlabel('Gait Cycle (%)')
    plt.ylabel('Foot')
    plt.xticks(np.arange(0, 151, step=50)) 

    #plot the Hildebrand graph
    plt.show()

#3rd input function option (C)
def from_data_points_user_input():

    l_stance_time = float(input("Enter Mean Left % Stance Time\n"))
    r_stance_time = float(input("Enter Mean Right % Stance Time\n"))
    temporal_symmetry = float(input("Enter Mean Temporal Symmetry\n"))
    
    l_stance_cycle = l_stance_time
    r_cycle_toe_strike = 50 - (temporal_symmetry)
    r_toe_strike = r_stance_time - temporal_symmetry 
    y_label = ['Left', 'Right']

    l_standard_deviation = float(input("Enter Left Stance Time Confidence Interval\n"))
    r_standard_deviation = float(input("Enter Right Stance Time Confidence Interval\n"))
    num_terms = float(input("Enter Number of Trials in Data Set\n"))
    r_confidence_interval =  1.96*(r_standard_deviation/(num_terms)**(1/2)) 
    l_confidence_interval =  1.96*(l_standard_deviation/(num_terms)**(1/2))


    #create a graph of a specific size (width,height) in inches
    plt.figure(figsize=(6, 2))

    #plot right foot strike bar
    p3=plt.barh( y=y_label[1],  width=r_stance_time, height=0.4, left = temporal_symmetry,  align='center', color='black', edgecolor='black')
    #plot right foot strike bar right error
    p6=plt.barh( y=y_label[1],  width=r_confidence_interval, height=0.4, left = temporal_symmetry + r_stance_time,  align='center', color='lightgrey', edgecolor='black')
    #plot right foot strike bar left error
    p6=plt.barh( y=y_label[1],  width=r_confidence_interval, height=0.4, left = temporal_symmetry - r_confidence_interval,  align='center', color='lightgrey', edgecolor='black')

    if r_cycle_toe_strike > 0: #if the right foot strikes again before 150%
        #plot second right foot strike bar
        p4=plt.barh( y=y_label[1],  width=r_cycle_toe_strike, height=0.4, left=150-r_cycle_toe_strike, align='center', color='black', edgecolor='black')
        #plot second right foot strike bar
        p9=plt.barh(y=y_label[1],  width=r_confidence_interval, height=0.4, left=150-r_cycle_toe_strike-r_confidence_interval, align='center',color='lightgrey', edgecolor='black')
    #plot initial right foot step
    p5=plt.barh( y=y_label[1],  width=r_toe_strike, height=0.4, align='center', color='black', edgecolor='black')
    #plot initial right foot step error
    p8=plt.barh( y=y_label[1],  width=r_confidence_interval, height=0.4, left=r_toe_strike, align='center', color='lightgrey', edgecolor='black')

    #plot initial left foot step
    p1=plt.barh( y=y_label[0],  width=l_stance_time, height=0.4, align='center', color='black', edgecolor='black' )
    #plot initial  left foot step error
    p10=plt.barh( y=y_label[0],  width=l_confidence_interval, height=0.4, left=l_stance_time, align='center',  color='lightgray', edgecolor='black')

    if l_stance_cycle > 50: #if the second left foot strike goes past 150%
        #plot the second left foot strike up to 150%
        p2=plt.barh(y=y_label[0], width=50, height=0.4, left=100,  align='center', color='black', edgecolor='black' )
        
    else:
        #plot the second left foot strike
        p2=plt.barh(y=y_label[0], width=l_stance_cycle, height=0.4, left=100, align='center', color='black',  edgecolor='black' )
        #plot the second left foot strike right error
        p11=plt.barh( y=y_label[0],  width=l_confidence_interval, height=0.4, left=100+l_stance_cycle, align='center', color='lightgrey', edgecolor='black')
    #plot the second left foot strike left error
    p12=plt.barh( y=y_label[0],  width=l_confidence_interval, height=0.4, left=100-l_confidence_interval, align='center', color='lightgrey', edgecolor='black')
    



    #add labels to the graph
    plt.xlabel('Gait Cycle (%)')
    plt.ylabel('Foot')
    plt.xticks(np.arange(0, 151, step=50)) 

    #plot the Hildebrand graph
    plt.show()

user_choice = input("Select data format\n 'A' - from one Excel rows\n 'B' - avg from all excel rows\n 'C' - from user input  ")


if user_choice == 'A':
    from_data_points_excel()
elif user_choice == 'B':
    from_data_ranges_excel()
else:
    from_data_points_user_input()




