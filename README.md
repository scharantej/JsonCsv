## Flask Application Design

### HTML Files

- **dropdown.html**:
   - Contains a dropdown menu with a list of available JSON files.
   - When a file is selected from the dropdown, its name is automatically passed to the Python program via AJAX.
- **index.html**:
   - Main page of the application.
   - Displays the dropdown menu and provides a button to trigger the generation of CSV files.

### Routes

- **dropdown**:
   - Route that handles the dropdown selection.
   - Receives the selected file name via AJAX.
   - Calls the Python program to generate the CSV version of the selected file.
- **generate_csv**:
   - Route that triggers the generation of CSV files for all available JSON files.
   - Calls the Python program to perform the conversion for each file.
- **home**:
   - Route for the main page of the application.
   - Renders the `index.html` file.