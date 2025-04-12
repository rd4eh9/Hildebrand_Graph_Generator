#import the necessary code libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from tkinter import Tk, filedialog

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
l_end = df['Mean L % Stance Time']
l_cycle = df['Mean L % Stance Time']
r_end = df['Temporal Symmetry'] * 100
r_cycle = df['Mean R % Stance Time']
r_lag = 50 - (df['Temporal Symmetry'] * 100)
r_start = df['Mean R % Stance Time'] - (df['Temporal Symmetry'] * 100)
y_val = ['Left', 'Right']

#create a graph of a specific size (width,height) in inches
plt.figure(figsize=(8, 3))

#plot the bars for the right foot
p3=plt.barh( y=y_val[1],  width=r_cycle[0], height=0.4, left = r_end, xerr=[[r_cycle[1]],[r_cycle[1]]],  align='center', label = 'left hind', color='black', capsize=5 )
if r_lag[0] > 0:
   p4=plt.barh( y=y_val[1],  width=r_lag[0], height=0.4, left=150-r_lag[0], align='center', label = 'left hind', color='black')
p5=plt.barh( y=y_val[1],  width=r_start[0], height=0.4, align='center', label = 'left hind', xerr=[[r_start[0]],[r_start[0]]], color='black',  capsize=5 )        

#plot the bars for the left foot
p1=plt.barh( y=y_val[0],  width=l_end[0], height=0.4, align='center', xerr=[[l_end[1]],[l_end[1]]], label = 'left hind', color='black',   capsize=5 )
if l_cycle[0] > 50:
    p2=plt.barh(y=y_val[0], width=50, height=0.4, left=100,  align='center', xerr=[[l_cycle[1]],[l_cycle[1]]], label = 'left hind', color='black', capsize=5 )
else:
    p2=plt.barh(y=y_val[0], width=l_cycle[0], height=0.4, left=100, align='center', xerr=[[l_cycle[1]],[l_cycle[1]]], label = 'left hind', color='black', capsize=5 )

#add labels to the graph
plt.xlabel('Gait Cycle')
plt.ylabel('Foot')
plt.title('Hildebrand Graph')

#plot the Hildebrand graph
plt.show()

