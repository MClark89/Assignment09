# ---------------------------------------------------------- #
# Title: TestHarness
# Description: A main module for testing
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created script
# MClark, 3.13.2021, Created Script
# ---------------------------------------------------------- #
if __name__ == "__main__":
    import DataClasses as DC
    import ProcessingClasses as PC
    import IOClasses as IC
else:
    raise Exception("This file was not created to be imported")

# Test data module
objP1 = DC.Employee(1, "Don", "Johnson")
objP2 = DC.Employee(2, "Carl", "Sagan")
lstTable = [objP1, objP2]
for row in lstTable:
    print(row.to_string(), type(row))

# Test processing module
PC.FileProcessor.save_data_to_file("EmployeeData.txt", lstTable)
lstFileData = PC.FileProcessor.read_data_from_file("EmployeeData.txt")
for row in lstFileData:
    nim = DC.Employee(row[0], row[1], row[2])
    print(nim.to_string().strip(), type(nim))

# Test IO classes
IC.EmployeeIO.print_menu_items()
IC.EmployeeIO.print_current_list_items(lstTable)
m1 = IC.EmployeeIO.input_employee_data()
print(m1)