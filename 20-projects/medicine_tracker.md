# Medicine Tracker

Simple python terminal based application to track the medicines you take. It allows you to add, view, and delete medicines from your list.

## Features

- Add a new medicine to your list
- View all medicines in your list
- Delete a medicine from your list

## Technical detail

Use file operations to store the medicines in a text file.
Each medicine will be stored in a new line in the text file.

Application should read the text file and print the details of each medicine in a table form.

Number of medicines in the list should be displayed at the end of the table.

Ex.
Medicine Name | Dosage | Frequency | In Store | Last Purchase Date
Paracetamol | 500mg | Twice a day | 10 | 2024-06-01

## Consume a Medicine

To consume a medicine, the application should allow the user to select a medicine from the list and specify the quantity to consume.

The application should then update the "In Store" count for that medicine and save the changes back to the text file.

Ex.
Medicine Name | Dosage | Frequency | In Store | Last Purchase Date
Paracetamol | 500mg | Twice a day | 9 | 2024-06-01
