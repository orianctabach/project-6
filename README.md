# project-6

**Used Car Sales Analysis**

This Streamlit app explores various factors that might influence how long it takes to sell a used car. 
You can see it deployed on Render here: [link](https://project-6-orianctabach.onrender.com/)

**Data Source:**

The data used in this app is from a CSV file named "vehicles_us.csv". It includes details on various used cars sold in the US.

**Analysis**

The app investigates the impact of the following factors on the number of days a car is listed before being sold:

* **Car Color:** Whether including the car's color in the listing affects the number of days the car is listed. 
* **Car Condition:** Whether the car's condition affects the number of days the car is listed. 
* **Listing Date:**  Whether there are any changes in car sales market trends across different listing dates. 
* **Car Price:** The relationship between the car's price and its sales speed. 


**How to Run the App Localy**

1. **Set up a Virtual Environment (Recommended):**

   It's recommended to run this app in a virtual environment to isolate its dependencies from other Python projects on your system. Here's how to create and activate a virtual environment using `venv`:

   ```
   python -m venv venv  # Replace 'venv' with your desired virtual environment name
   source venv/bin/activate  # Activate the virtual environment (Linux/macOS)
   venv\Scripts\activate.bat  # Activate the virtual environment (Windows)
   ```

2. **Install Dependencies**


Once your virtual environment is activated, install the required packages listed in the `requirements.txt` file using pip:

```
pip install -r requirements.txt
```

3. **Running the App**
Navigate to the root of the project and run the following command:

```
python3 -m streamlit run app.py
```
