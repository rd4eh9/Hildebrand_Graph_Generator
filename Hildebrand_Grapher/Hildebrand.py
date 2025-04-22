#import the necessary code libraries
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np 
import pandas as pd
from tkinter import Tk, filedialog
import math

#function to plot the left bipedal, left hind quadrupedal, and right fore quadrupedal steps 
def plot_l_lh_rf(l_stance, l_stance_cy, l_ci, y_ax):
    #plot initial left foot step
    p1=plt.barh( y=y_ax,  width=l_stance, height=0.4, align='center', color='black', edgecolor='black' )
    #plot initial  left foot step error
    p10=plt.barh( y=y_ax,  width=l_ci, height=0.4, left=l_stance, align='center',  color='lightgray', edgecolor='black')

    if l_stance_cy > 50: #if the second left foot strike goes past 150%
        #plot the second left foot strike up to 150%
        p2=plt.barh(y=y_ax, width=50, height=0.4, left=100,  align='center', color='black', edgecolor='black' )
        
    else:
        #plot the second left foot strike
        p2=plt.barh(y=y_ax, width=l_stance_cy, height=0.4, left=100, align='center', color='black',  edgecolor='black' )
        #plot the second left foot strike right error
        p11=plt.barh( y=y_ax,  width=l_ci, height=0.4, left=100+l_stance_cy, align='center', color='lightgrey', edgecolor='black')
    #plot the second left foot strike left error
    p12=plt.barh( y=y_ax,  width=l_ci, height=0.4, left=100-l_ci, align='center', color='lightgrey', edgecolor='black')

#function to plot the right bipedal, right hind quadrupedal, and left fore quadrupedal steps     
def plot_r_rh_lf(r_stance, r_toe_strike, r_cyc_toe_strike, temp_sym, r_ci, y_ax):
    #plot right foot strike bar
    p3=plt.barh( y=y_ax,  width=r_stance, height=0.4, left = temp_sym,  align='center', color='black', edgecolor='black')
    #plot right foot strike bar right error
    p6=plt.barh( y=y_ax,  width=r_ci, height=0.4, left = temp_sym + r_stance,  align='center', color='lightgrey', edgecolor='black')
    #plot right foot strike bar left error
    p6=plt.barh( y=y_ax,  width=r_ci, height=0.4, left = temp_sym - r_ci,  align='center', color='lightgrey', edgecolor='black')

    if r_toe_strike > 0: #if the right foot strikes again before 150%
        #plot second right foot strike bar
        p4=plt.barh( y=y_ax,  width=r_cyc_toe_strike, height=0.4, left=150-r_cyc_toe_strike, align='center', color='black', edgecolor='black')
        #plot second right foot strike bar
        p9=plt.barh(y=y_ax,  width=r_ci, height=0.4, left=150-r_cyc_toe_strike-r_ci, align='center',color='lightgrey', edgecolor='black')
    #plot initial right foot step
    p5=plt.barh( y=y_ax,  width=r_toe_strike, height=0.4, align='center', color='black', edgecolor='black')
    #plot initial right foot step error
    p8=plt.barh( y=y_ax,  width=r_ci, height=0.4, left=r_toe_strike, align='center', color='lightgrey', edgecolor='black')


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

    #calculate statistical values for graphing
    l_standard_deviation = l_stance_time[1]
    r_standard_deviation = r_stance_time[1]
    num_terms = 6
    r_confidence_interval =  1.96*(r_standard_deviation/(num_terms)**(1/2)) 
    l_confidence_interval =  1.96*(l_standard_deviation/(num_terms)**(1/2))

    #create a graph of a specific size (width,height) in inches
    plt.figure(figsize=(6, 2))

    #plot right foot from 1st row of excel data
    plot_r_rh_lf(r_stance_time[0],r_toe_strike[0], r_cycle_toe_strike[0], temporal_symmetry[0], r_confidence_interval, y_label[1])

    #plot left foot from 1st row of excel data
    plot_l_lh_rf(l_stance_time[0], l_stance_cycle[0], l_confidence_interval, y_label[0])

    #add labels to the graph
    plt.xlabel('Gait Cycle (%)')
    plt.ylabel('Foot')
    plt.xlim([0, 150])
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
    r_toe_strike = r_stance_time - (temporal_symmetry)
    y_label = ['Left', 'Right']

    #calculate statistical values for graphing
    l_standard_deviation =  np.std(df['Mean L % Stance Time'])
    r_standard_deviation = np.std(df['Mean R % Stance Time'])
    r_confidence_interval = 1.96*(r_standard_deviation/(num_terms)**(1/2)) 
    l_confidence_interval = 1.96*(l_standard_deviation/(num_terms)**(1/2))

    #create a graph of a specific size (width,height) in inches
    plt.figure(figsize=(6, 2))

    #plot right foot from mean of excel data
    plot_r_rh_lf(r_stance_time, r_toe_strike, r_cycle_toe_strike, temporal_symmetry, r_confidence_interval, y_label[1])

    #plot left foot from mean of excel data
    plot_l_lh_rf(l_stance_time, l_stance_cycle, l_confidence_interval, y_label[0])
  
    #add labels to the graph
    plt.xlabel('Gait Cycle (%)')
    plt.ylabel('Foot')
    plt.xlim([0, 150])
    plt.xticks(np.arange(0, 151, step=50)) 

    #plot the Hildebrand graph
    plt.show()

#3rd input function option (C) - Bipedal graph option (2)
def bi_from_data_points_user_input():

    #save the user input as variables needed to create the Hildebrand graph
    l_stance_time = float(input("Enter Mean Left % Stance Time\n"))
    r_stance_time = float(input("Enter Mean Right % Stance Time\n"))
    temporal_symmetry = float(input("Enter Mean % Temporal Symmetry\n"))
    l_stance_cycle = l_stance_time
    r_cycle_toe_strike = 50 - (temporal_symmetry)
    r_toe_strike = r_stance_time - temporal_symmetry 
    y_label = ['Left', 'Right']

    #calculate statistical values for graphing
    l_standard_deviation = float(input("Enter Left Stance Time Confidence Interval\n"))
    r_standard_deviation = float(input("Enter Right Stance Time Confidence Interval\n"))
    num_terms = float(input("Enter Number of Trials in Data Set\n"))
    r_confidence_interval =  1.96*(r_standard_deviation/(num_terms)**(1/2)) 
    l_confidence_interval =  1.96*(l_standard_deviation/(num_terms)**(1/2))


    #create a graph of a specific size (width,height) in inches
    plt.figure(figsize=(6, 2))

    #plot right foot from user input
    plot_r_rh_lf(r_stance_time, r_toe_strike, r_cycle_toe_strike, temporal_symmetry, r_confidence_interval, y_label[1])

    #plot left foot from user input
    plot_l_lh_rf(l_stance_time, l_stance_cycle, l_confidence_interval, y_label[0])

    #add labels to the graph
    plt.xlabel('Gait Cycle (%)')
    plt.ylabel('Foot')
    plt.xlim([0, 150])
    plt.xticks(np.arange(0, 151, step=50)) 

    #plot the Hildebrand graph
    plt.show()

#3rd input function option (C) - Quadrupedal graph option (4)
def quad_from_data_points_user_input():
    #save the user input as variables needed to create the Hildebrand graph
    lh_stance_time = float(input("Enter Mean Left Hind % Stance Time\n"))
    lf_stance_time = float(input("Enter Mean Left Fore % Stance Time\n"))
    l_temporal_symmetry = float(input("Enter Mean Left % Temporal Symmetry\n"))
    rf_stance_time = float(input("Enter Mean Right Fore % Stance Time\n"))
    rh_stance_time = float(input("Enter Mean Right Hind % Stance Time\n"))
    r_temporal_symmetry = float(input("Enter Mean Right % Temporal Symmetry\n"))
    rf_stance_cycle = rf_stance_time
    lh_stance_cycle = lh_stance_time
    rh_cycle_toe_strike = 50 - (r_temporal_symmetry)
    rh_toe_strike = rh_stance_time - r_temporal_symmetry 
    lf_cycle_toe_strike = 50 - (l_temporal_symmetry)
    lf_toe_strike = lf_stance_time - l_temporal_symmetry 
    y_label = ['LH','LF', 'RF', 'RH']

    #calculate statistical values for graphing
    lh_standard_deviation = float(input("Enter Left Hind Stance Time Confidence Interval\n"))
    lf_standard_deviation = float(input("Enter Left Fore Stance Time Confidence Interval\n"))
    rf_standard_deviation = float(input("Enter Right Fore Stance Time Confidence Interval\n"))
    rh_standard_deviation = float(input("Enter Right Hind Stance Time Confidence Interval\n"))
    num_terms = float(input("Enter Number of Trials in Data Set\n"))
    rh_confidence_interval =  1.96*(rh_standard_deviation/(num_terms)**(1/2)) 
    lh_confidence_interval =  1.96*(lh_standard_deviation/(num_terms)**(1/2))
    rf_confidence_interval =  1.96*(rf_standard_deviation/(num_terms)**(1/2)) 
    lf_confidence_interval =  1.96*(lf_standard_deviation/(num_terms)**(1/2))

    #create a graph of a specific size (width,height) in inches
    plt.figure(figsize=(6, 2))

    #plot right hind foot from user input
    plot_r_rh_lf(rh_stance_time, rh_toe_strike, rh_cycle_toe_strike, r_temporal_symmetry, rh_confidence_interval, y_label[3])

    #plot right fore foot from user input
    plot_l_lh_rf(rf_stance_time, rf_stance_cycle, rf_confidence_interval, y_label[2])

    #plot left fore foot from user input
    plot_r_rh_lf(lf_stance_time, lf_toe_strike, lf_cycle_toe_strike, l_temporal_symmetry, lf_confidence_interval, y_label[1])

    #plot left hind foot from user input
    plot_l_lh_rf(lh_stance_time, lh_stance_cycle, lh_confidence_interval, y_label[0])

    #add labels to the graph
    plt.xlabel('Gait Cycle (%)')
    plt.ylabel('Foot')
    plt.xticks(np.arange(0, 151, step=50)) 
    plt.xlim([0, 150])

    #plot the Hildebrand graph
    plt.show()

#3rd input function option (C) - Quadrupedal and Bipdedal Combined graph option (6)
def both_from_data_points_user_input():
    #save the user input as variables needed to create the Hildebrand graph
    lh_stance_time = float(input("Enter Quadrupedal Mean Left Hind % Stance Time\n"))
    lf_stance_time = float(input("Enter Quadrupedal Mean Left Fore % Stance Time\n"))
    l_temporal_symmetry = float(input("Enter Quadrupedal Mean Left % Temporal Symmetry\n"))
    rf_stance_time = float(input("Enter Quadrupedal Mean Right Fore % Stance Time\n"))
    rh_stance_time = float(input("Enter Quadrupedal Mean Right Hind % Stance Time\n"))
    r_temporal_symmetry = float(input("Enter Quadrupedal Mean Right % Temporal Symmetry\n"))
    l_stance_time = float(input("Enter Bipedal Mean Left % Stance Time\n"))
    r_stance_time = float(input("Enter Bipedal Mean Right % Stance Time\n"))
    temporal_symmetry = float(input("Enter Bipedal Mean % Temporal Symmetry\n"))
    rf_stance_cycle = rf_stance_time
    lh_stance_cycle = lh_stance_time
    rh_cycle_toe_strike = 50 - (r_temporal_symmetry)
    rh_toe_strike = rh_stance_time - r_temporal_symmetry 
    lf_cycle_toe_strike = 50 - (l_temporal_symmetry)
    lf_toe_strike = lf_stance_time - l_temporal_symmetry 
    l_stance_cycle = l_stance_time
    r_cycle_toe_strike = 50 - (temporal_symmetry)
    r_toe_strike = r_stance_time - temporal_symmetry 
    y_label = ['LH','LF', 'RF', 'RH', 'L', 'R']

    #calculate statistical values for graphing
    lh_standard_deviation = float(input("Enter Quadrupedal Left Hind Stance Time Confidence Interval\n"))
    lf_standard_deviation = float(input("Enter Quadrupedal Left Fore Stance Time Confidence Interval\n"))
    rf_standard_deviation = float(input("Enter Quadrupedal Right Fore Stance Time Confidence Interval\n"))
    rh_standard_deviation = float(input("Enter Quadrupedal Right Hind Stance Time Confidence Interval\n"))
    num_terms = float(input("Enter Number of Trials in Quadrupedal Data Set\n"))
    rh_confidence_interval =  1.96*(rh_standard_deviation/(num_terms)**(1/2)) 
    lh_confidence_interval =  1.96*(lh_standard_deviation/(num_terms)**(1/2))
    rf_confidence_interval =  1.96*(rf_standard_deviation/(num_terms)**(1/2)) 
    lf_confidence_interval =  1.96*(lf_standard_deviation/(num_terms)**(1/2))
    l_standard_deviation = float(input("Enter Bipdeal Left Stance Time Confidence Interval\n"))
    r_standard_deviation = float(input("Enter Bipedal Right Stance Time Confidence Interval\n"))
    num_terms = float(input("Enter Number of Trials in Bipedal Data Set\n"))
    r_confidence_interval =  1.96*(r_standard_deviation/(num_terms)**(1/2)) 
    l_confidence_interval =  1.96*(l_standard_deviation/(num_terms)**(1/2))

    #create a graph of a specific size (width,height) in inches
    plt.figure(figsize=(6, 2))

    #plot right foot from user input
    plot_r_rh_lf(r_stance_time, r_toe_strike, r_cycle_toe_strike, temporal_symmetry, r_confidence_interval, y_label[5])

    #plot left foot from user input
    plot_l_lh_rf(l_stance_time, l_stance_cycle, l_confidence_interval, y_label[4])

    #plot right hind foot from user input
    plot_r_rh_lf(rh_stance_time, rh_toe_strike, rh_cycle_toe_strike, r_temporal_symmetry, rh_confidence_interval, y_label[3])

    #plot right fore foot from user input
    plot_l_lh_rf(rf_stance_time, rf_stance_cycle, rf_confidence_interval, y_label[2])

    #plot left fore foot from user input
    plot_r_rh_lf(lf_stance_time, lf_toe_strike, lf_cycle_toe_strike, l_temporal_symmetry, lf_confidence_interval, y_label[1])

    #plot left hind foot from user input
    plot_l_lh_rf(lh_stance_time, lh_stance_cycle, lh_confidence_interval, y_label[0])

    #add labels to the graph
    plt.xlabel('Gait Cycle (%)')
    plt.ylabel('Foot')
    plt.xticks(np.arange(0, 151, step=50)) 
    plt.xlim([0, 150])
    #plot the Hildebrand graph
    plt.show()

#prompt user to select data input type
user_choice = input("Select data format\n 'A' - from one Excel rows\n 'B' - avg from all excel rows\n 'C' - from user input\n  ")

#create Hildebrand graph based on selected data input type
if user_choice == 'A':
    from_data_points_excel()
elif user_choice == 'B':
    from_data_ranges_excel()
else:
    graph_type = input("Graph type:\n '2' - Bipedal\n '4' Quadrupedal\n '6' - Both\n ")
    if graph_type == '2':
        bi_from_data_points_user_input()
    elif graph_type == '4':
        quad_from_data_points_user_input()
    elif graph_type == '6':
        both_from_data_points_user_input()