# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# MClark,3.13.2021,Modified code to complete assignment 9
# ------------------------------------------------------------------------ #
# Import Modules

import DataClasses as DC
import ProcessingClasses as PC
import IOClasses as IOC


# Start Data -------------------------------------------------------------------- #

strFileName = 'EmployeeData.txt'
lstNewEmployee = []
lstOfEmployee = []
strChoice = ""

# End Data -------------------------------------------------------------------- #

# Start Main Body of Script  ---------------------------------------------------- #

# Load data from file into a list of employee objects when script starts
lstOfEmployee = PC.FileProcessor.read_data_from_file(strFileName)
for row in lstOfEmployee:
    lstNewEmployee.append(DC(row[0], row[1], row[2].strip()))

while(True):
    IOC.EmployeeIO.print_menu_items()
    strChoice = IOC.EmployeeIO.input_menu_options()

# Process user's menu choice
    #Show Data
    if strChoice.strip() == "1":
        IOC.EmployeeIO.print_current_list_items(lstOfEmployee)
# Add Data
    elif strChoice == "2":
        objNewEmployee = IOC.EmployeeIO.input_employee_data()
        lstOfEmployee.append(objNewEmployee)
# Save Data
    elif strChoice == "3":
        PC.FileProcessor.save_data_to_file(strFileName, lstOfEmployee)
# Exit Program
    elif strChoice == "4":  # Let user exit program
        print("Thank you, Goodbye!")
        break