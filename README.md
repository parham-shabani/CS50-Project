# Budget Management System
#### Video Demo: https://youtu.be/7J31npq_LP0
#### Description:
This is a simple command-line budget management system implemented in Python. It allows users to add monthly budgets, display budget details for a specific month, calculate total savings, and quit the program.

project.py file :
Features:
- Add Month Budget: Users can enter the income and expenses for a specific month, and the system will calculate and store the corresponding savings.

- Display Month Budget: Users can view the budget details (income, expenses, and savings) for a specific month.

- Calculate Total Savings: The system can calculate and display the total savings across all the stored budgets.

Menu Interface: The program provides a menu-based interactive interface where users can choose the desired operation.

Usage:
1- Add Month Budget
- Enter the corresponding number for the "Add month budget" option in the menu.
- Provide the name of the month.
- Enter the income amount for the specified month.
- Enter the expenses amount for the specified month.
- The system will calculate and store the savings for the specified month.

2- Display Month Budget
- Select the "Display month budget" option from the menu.
- Enter the name of the month for which you want to display the budget details.
- The system will display the income, expenses, and savings for the specified month.

3- Calculate Total Savings
- Choose the "Calculate total savings" option from the menu.
- The system will calculate and display the total savings across all the stored budgets.

4- Quit
- To exit the program, select the "Quit" option from the menu.


The project includes several unit tests implemented using the pytest framework. These tests ensure the correct functionality of the budget management system.
test_project.py :

test_add_month_budget:
This test verifies the add_month_budget function. It sets up a scenario where the user provides an income of 1000 and expenses of 600 for the month of January. The test then checks if the budget dictionary is correctly updated with the income, expenses, and calculated savings. It asserts that the income is 1000, expenses are 600, and savings are 400.

test_display_month_budget:
This test focuses on the display_month_budget function. It first clears the budget dictionary and initializes a budget for the month of January with specific income, expenses, and savings. The test then captures the output of calling display_month_budget for both January and February. It asserts that the captured output matches the expected output for each case, ensuring that the function displays the budget details correctly and handles the case when a budget for a specific month is not found.

test_calculate_total_savings:
This test validates the calculate_total_savings function. It starts by clearing the budget dictionary and asserts that the total savings are 0 when no budgets are initialized. Then, budgets for January, February, and March are added with different income, expenses, and savings values. The test checks if calculate_total_savings correctly calculates and displays the total savings across all the budgets. It asserts that the captured output matches the expected output, which ensures that the function accurately calculates the total savings.

Running the Tests
To run the tests, you can use the pytest framework. Open a terminal or command prompt, navigate to the project directory, and execute the command: "pytest test_project.py"

This command will automatically discover and execute all the tests in the project. The test results will be displayed in the console, indicating whether each test passed or failed.
