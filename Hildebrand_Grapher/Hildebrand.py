#import the necessary code libraries
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np 
import pandas as pd
from tkinter import Tk, filedialog
import statistics
import math



#1st input option function
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
    r_cycle_toe_off = 50 - (df['Temporal Symmetry'] * 100)
    temporal_symmetry_cycle = df['Temporal Symmetry'] * 100 #delete
    r_toe_off = df['Mean R % Stance Time'] - (df['Temporal Symmetry'] * 100)
    y_label = ['Left', 'Right']

    l_standard_deviation = l_stance_time[0]
    r_standard_deviation = r_stance_time[0]
    num_terms = 6
    r_confidence_interval_right = r_stance_time + 1.96*(r_standard_deviation/(num_terms)**(1/2)) 
    l_confidence_interval_left = l_stance_time - 1.96*(l_standard_deviation/(num_terms)**(1/2))


    #create a graph of a specific size (width,height) in inches
    plt.figure(figsize=(6, 2))

    #plot the bars for the right foot
    p3=plt.barh( y=y_label[1],  width=r_stance_time[0], height=0.4, left = temporal_symmetry[0],  align='center', color='black', edgecolor='black')
    #error
    p6=plt.barh( y=y_label[1],  width=r_stance_time[1], height=0.4, left = temporal_symmetry[0] + r_stance_time[0],  align='center', color='lightgrey', edgecolor='black')

    if r_cycle_toe_off[0] > 0:
        p4=plt.barh( y=y_label[1],  width=r_cycle_toe_off[0], height=0.4, left=150-r_cycle_toe_off[0], align='center', color='black', edgecolor='black')
        #errors
        p9=plt.barh(y=y_label[1],  width=temporal_symmetry_cycle[1], height=0.4, left=150-r_cycle_toe_off[0]-temporal_symmetry_cycle[1], align='center',color='lightgrey', edgecolor='black')
    p5=plt.barh( y=y_label[1],  width=r_toe_off[0], height=0.4, align='center', color='black', edgecolor='black')
    #error
    p8=plt.barh( y=y_label[1],  width=r_toe_off[1], height=0.4, left=r_toe_off[0], align='center', color='lightgrey', edgecolor='black')

    #plot the bars for the left foot
    p1=plt.barh( y=y_label[0],  width=l_stance_time[0], height=0.4, align='center', color='black', edgecolor='black' )
    #error
    p10=plt.barh( y=y_label[0],  width=l_stance_time[1], height=0.4, left=l_stance_time[0], align='center',  color='lightgrey', edgecolor='black')

    if l_stance_cycle[0] > 50:
        p2=plt.barh(y=y_label[0], width=50, height=0.4, left=100,  align='center', color='black', edgecolor='black' )
        p12=plt.barh( y=y_label[0],  width=l_stance_cycle[1], height=0.4, left=100-l_stance_cycle[1], align='center', color='lightgrey', edgecolor='black')

    else:
        p2=plt.barh(y=y_label[0], width=l_stance_cycle[0], height=0.4, left=100, align='center', color='black',  edgecolor='black' )
        #error
        p11=plt.barh( y=y_label[0],  width=l_stance_cycle[1], height=0.4, left=50+l_stance_cycle[1], align='center', color='lightgrey', edgecolor='black')

    #add labels to the graph
    plt.xlabel('Gait Cycle (%)')
    plt.ylabel('Foot')
    plt.xticks(np.arange(0, 151, step=50)) 

    #plot the Hildebrand graph
    plt.show()

#2nd input option function 
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
        df = pd.read_excel(file_path, 'Raw Data')
        print(df.head())
    else:
        print("No file selected.")


    #extract the variables (spreadsheet columns) needed to create the Hildebrand graph
    l_stance_time = df['Mean L % Stance Time']
    l_stance_time = sum(l_stance_time) / len(l_stance_time)
    l_stance_cycle = l_stance_time
    temporal_symmetry = df['Temporal Symmetry'] * 100
    temporal_symmetry = sum(temporal_symmetry) / len(temporal_symmetry)
    r_stance_time = df['Mean R % Stance Time']
    r_stance_time = sum(r_stance_time) / len(r_stance_time)
    r_cycle_toe_off = 50 - (temporal_symmetry * 100)
    temporal_symmetry_cycle = temporal_symmetry * 100 #delete
    r_toe_off = r_stance_time - (temporal_symmetry * 100)
    y_label = ['Left', 'Right']

    l_standard_deviation = l_stance_time
    r_standard_deviation = r_stance_time
    num_terms = 6
    r_confidence_interval_right = r_stance_time + 1.96*(r_standard_deviation/(num_terms)**(1/2)) 
    l_confidence_interval_left = l_stance_time - 1.96*(l_standard_deviation/(num_terms)**(1/2))


    #create a graph of a specific size (width,height) in inches
    plt.figure(figsize=(6, 2))

    #plot the bars for the right foot
    p3=plt.barh( y=y_label[1],  width=r_stance_time, height=0.4, left = temporal_symmetry,  align='center', color='black', edgecolor='black')
    #error
    p6=plt.barh( y=y_label[1],  width=r_stance_time, height=0.4, left = temporal_symmetry + r_stance_time,  align='center', color='lightgrey', edgecolor='black')

    if r_cycle_toe_off > 0:
        p4=plt.barh( y=y_label[1],  width=r_cycle_toe_off, height=0.4, left=150-r_cycle_toe_off, align='center', color='black', edgecolor='black')
        #errors
        p9=plt.barh(y=y_label[1],  width=temporal_symmetry_cycle, height=0.4, left=150-r_cycle_toe_off-temporal_symmetry_cycle, align='center',color='lightgrey', edgecolor='black')
    p5=plt.barh( y=y_label[1],  width=r_toe_off, height=0.4, align='center', color='black', edgecolor='black')
    #error
    p8=plt.barh( y=y_label[1],  width=r_toe_off, height=0.4, left=r_toe_off, align='center', color='lightgrey', edgecolor='black')

    #plot the bars for the left foot
    p1=plt.barh( y=y_label[0],  width=l_stance_time, height=0.4, align='center', color='black', edgecolor='black' )
    #error
    p10=plt.barh( y=y_label[0],  width=l_stance_time, height=0.4, left=l_stance_time, align='center',  color='lightgrey', edgecolor='black')

    if l_stance_cycle > 50:
        p2=plt.barh(y=y_label[0], width=50, height=0.4, left=100,  align='center', color='black', edgecolor='black' )
        p12=plt.barh( y=y_label[0],  width=l_stance_cycle, height=0.4, left=100-l_stance_cycle, align='center', color='lightgrey', edgecolor='black')

    else:
        p2=plt.barh(y=y_label[0], width=l_stance_cycle, height=0.4, left=100, align='center', color='black',  edgecolor='black' )
        #error
        p11=plt.barh( y=y_label[0],  width=l_stance_cycle, height=0.4, left=50+l_stance_cycle, align='center', color='lightgrey', edgecolor='black')

    #add labels to the graph
    plt.xlabel('Gait Cycle (%)')
    plt.ylabel('Foot')
    plt.xticks(np.arange(0, 151, step=50)) 

    #plot the Hildebrand graph
    plt.show()

#3rd input function option
def from_data_points_user_input():

    l_stance_time = float(input("Enter Left % Stance Time\n"))
    r_stance_time = float(input("Enter Right % Stance Time\n"))
    temporal_symmetry = float(input("Enter Temporal Symmetry\n"))
    
    l_stance_cycle = l_stance_time
    r_cycle_toe_off = 50 - (temporal_symmetry)
    temporal_symmetry_cycle = temporal_symmetry #delete
    r_toe_off = r_stance_time - temporal_symmetry 
    y_label = ['Left', 'Right']

    l_standard_deviation = l_stance_time
    r_standard_deviation = r_stance_time
    num_terms = 6
    r_confidence_interval_right = r_stance_time + 1.96*(r_standard_deviation/(num_terms)**(1/2)) 
    l_confidence_interval_left = l_stance_time - 1.96*(l_standard_deviation/(num_terms)**(1/2))


    #create a graph of a specific size (width,height) in inches
    plt.figure(figsize=(6, 2))

    #plot the bars for the right foot
    p3=plt.barh( y=y_label[1],  width=r_stance_time, height=0.4, left = temporal_symmetry,  align='center', color='black', edgecolor='black')
    #error
    p6=plt.barh( y=y_label[1],  width=r_stance_time, height=0.4, left = temporal_symmetry + r_stance_time,  align='center', color='lightgrey', edgecolor='black')

    if r_cycle_toe_off > 0:
        p4=plt.barh( y=y_label[1],  width=r_cycle_toe_off, height=0.4, left=150-r_cycle_toe_off, align='center', color='black', edgecolor='black')
        #errors
        p9=plt.barh(y=y_label[1],  width=temporal_symmetry_cycle, height=0.4, left=150-r_cycle_toe_off-temporal_symmetry_cycle, align='center',color='lightgrey', edgecolor='black')
    p5=plt.barh( y=y_label[1],  width=r_toe_off, height=0.4, align='center', color='black', edgecolor='black')
    #error
    p8=plt.barh( y=y_label[1],  width=r_toe_off, height=0.4, left=r_toe_off, align='center', color='lightgrey', edgecolor='black')

    #plot the bars for the left foot
    p1=plt.barh( y=y_label[0],  width=l_stance_time, height=0.4, align='center', color='black', edgecolor='black' )
    #error
    p10=plt.barh( y=y_label[0],  width=l_stance_time, height=0.4, left=l_stance_time, align='center',  color='lightgrey', edgecolor='black')

    if l_stance_cycle > 50:
        p2=plt.barh(y=y_label[0], width=50, height=0.4, left=100,  align='center', color='black', edgecolor='black' )
        p12=plt.barh( y=y_label[0],  width=l_stance_cycle, height=0.4, left=100-l_stance_cycle, align='center', color='lightgrey', edgecolor='black')

    else:
        p2=plt.barh(y=y_label[0], width=l_stance_cycle, height=0.4, left=100, align='center', color='black',  edgecolor='black' )
        #error
        p11=plt.barh( y=y_label[0],  width=l_stance_cycle, height=0.4, left=50+l_stance_cycle, align='center', color='lightgrey', edgecolor='black')

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




