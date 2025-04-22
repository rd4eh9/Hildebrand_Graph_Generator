User Guide for Hildebrand Graph Generator Code
IDE: Visual Studio Code
Language: Python
Libraries: matplotlib.pyplot, matplotlib.ticker, numpy, pandas, tkinter

Program Overview: This program consists of several functions which can generate Hildebrand graphs from different types of input. It also includes the option to generate bipedal or quadrupedal graphs from user input. Comments are included within the code to explain the program flow in detail. 
 
Function Definitions: 
The Hildebrand graph is created with the following two functions, using several horizontal bar plots plt.barh() with specific left= and width= values to align with the Hildebrand graph format. The details of these commands are explained as comments within the code.

plot_l_lh_rf(l_stance, l_stance_cy, l_ci, y_ax)
This function plots the step sequence for the left bipedal, left hind quadrupedal, and right fore quadrupedal datapoints. has the input parameters stance time, stance cycle time (this is the same value as the stance time, but is saved as a separate variable for graphing purposes), confidence interval, and y-axis label.
plot_r_rh_lf(r_stance, r_toe_strike, r_cyc_toe_strike, temp_sym, r_ci, y_ax)
This function plots the step sequence for the right bipedal, right hind quadrupedal, and left fore quadrupedal datapoints. has the input parameters stance time, toe strike time, toe strike cycle time (this is the same value as the stance time, but is saved as a separate variable for graphing purposes), temporal symmetry, confidence interval, and y-axis label.

This program accepts three different formats of user input. The processing of user input into generation of variables for graphing is encapsulated in a function for each of the three formats. In these functions, the data is saved to variables, and additional variables are created to store statistical calculations such as standard deviation, which are necessary for generating the Hildebrand graphs. Then, the function calls the functions listed above to plot the step sequences and generates a graph using plt.
from_data_points_excel()

The first input option function reads in data from a specific row of the Excel spreadsheet. The name of the sheet is specified as df = pd.read_excel(file_path, 'Sheet Name'), and the column number of the spreadsheet is indexed from each variable using square bracket notation. For example, to access the stance time value from the first column of data, the syntax would be r_stance_time[0].
from_data_ranges_excel()

The second input option function reads in data from an entire Excel sheet and creates a graph with the mean of this data. The name of the sheet is specified as df = pd.read_excel(file_path, 'Sheet Name'), and by default all rows of the sheet are included in the mean calculations. 
	bi_from_data_points_user_input()
	quad_from_data_points_user_input()
	both_from_data_points_user_input()
The third input option reads in data that the user enters into the terminal. There are three functions associated with this input type, which generate bipedal, quadrupedal, and combined bipedal and quadrupedal Hildebrand graphs, respectively.

Program Flow:
 ![image](https://github.com/user-attachments/assets/24d6f36b-7a14-4aee-9dde-95b74b8d1dc9)

user_choice = input("Select data format…”)

The program flow allows the user to select the type of data input to generate the graph. The user is prompted to make a selection in the terminal. The appropriate function is called based on the user input choice.

	 ![image](https://github.com/user-attachments/assets/a82480aa-3b82-4014-942b-5d13fd6130a2)

graph_type = input("Graph type…”)

If the user is manually inputting data, they can also select the type of graph to display. The appropriate function is called based on the user input choice. 
 ![image](https://github.com/user-attachments/assets/e98e3693-308c-483f-b04d-c18d6e9911bd)

Then, the user will input the individual data points into the terminal as they are prompted to.
