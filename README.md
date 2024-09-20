# Automated Web Interaction Script

This project is a **Python** script that automates web interactions with a specific website using **Selenium WebDriver**. It is designed to log in to the site, navigate through several steps, and input geographical data points. The script uses **WAMPServer** for database management.

## Features

- **Automated Login**: Logs into the website automatically using Selenium.
- **Dynamic Waiting**: Utilizes explicit waits to handle dynamic web elements.
- **Data Input Automation**: Automates the process of selecting options and entering data points on the website.
- **Geographical Data Handling**: Inputs geographical coordinates to the web application.
- **Error Handling**: Includes try-except blocks to handle exceptions during the automation process.

## Technologies Used

- **Python 3.x**: The programming language used for the script.
- **Selenium WebDriver**: Automates browser interactions.
- **Chromedriver**: A WebDriver implementation for Chrome.

## Installation

1. **Python Installation**:
   - Ensure that **Python 3.x** is installed on your machine.
   - You can download it from [python.org](https://www.python.org/downloads/).

2. **Install Selenium**:
   - Open a command prompt or terminal.
   - Run the following command to install Selenium:
     ```python
     pip install selenium
     ```

3. **Download Chromedriver**:
   - Download the Chromedriver that matches your installed version of Chrome from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).
   - Place the `chromedriver.exe` file in the same directory as your script or specify the path in the script.


## Usage

1. **Configure Login Credentials**:
   - Open the script file in a text editor.
   - Locate the section where the username and password are set:
     ```python
     username_field.send_keys("your_username")
     password_field.send_keys("your_password")
     ```
   - Replace `"your_username"` and `"your_password"` with your actual login credentials for the website.

2. **Set the SMS Time** (if applicable):
   - Adjust the `sms_time` variable to match the expected time for SMS verification or any time-sensitive actions:
     ```python
     sms_time = 'HH:MM'
     ```

3. **Define Geographical Points**:
   - Modify the `points` list to include the geographical coordinates you wish to input:
     ```python
     points = [
         [
             (longitude_degree, longitude_minute, longitude_second, latitude_degree, latitude_minute, latitude_second),
             ...
         ],
         ...
     ]
     ```

4. **Run the Script**:
   - Ensure that WAMPServer is running if your script interacts with the database.
   - Execute the script using Python:
     ```python
     python your_script_name.py
     ```

5. **Monitor the Automation**:
   - The script will open a Chrome browser window and begin automating the web interactions.
   - Follow any on-screen prompts or instructions, especially if manual CAPTCHA or SMS verification is required.

## Notes

- **CAPTCHA and SMS Verification**:
  - The script includes a waiting mechanism for manual completion of CAPTCHA and SMS verification steps.
  - You will need to manually solve CAPTCHAs or enter verification codes when prompted.

- **Exception Handling**:
  - The script includes try-except blocks to handle potential exceptions.
  - If an error occurs, the script will print the error message and attempt to retry the operation.

- **Web Elements and XPaths**:
  - The script uses specific XPaths to locate web elements.
  - If the website's structure changes, you may need to update these XPaths accordingly.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

- Ensure you have permission to automate interactions with the target website.
- Be aware of the website's terms of service regarding automation and data entry.
- Use this script responsibly and ethically.

