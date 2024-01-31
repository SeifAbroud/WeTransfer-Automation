# Wetransfere-automation
If you find yourself repeatedly going through the steps of sending files via WeTransfer and wish to save time, this script can automate the process for you. By automating the steps of opening the website, uploading the file, and copying the link, you can save approximately 20 seconds per transfer. Additionally, you can multitask while the script runs.
### About the code : 
this code lets u automate opening the website and uploading the file to directly get the link copied to clipboard and printed . 
There are Two versions for this code : 
  - wetransfere-autoamtion1 : Takes the file path as input and prints the link directly. In this version, you can observe the automation process as it unfolds, with the Chrome browser visible during automation.
  - wetransfere-autoamtion1.1 : The same functionality as the previous version, but runs in headless mode. All automation occurs in the background, and the link is copied to the clipboard directly.
  - Wtscript.bat : This file allows you to execute the code directly from the command prompt, saving you more time.
## Setup :
### **for This code you need** : 
1.  Python installed in your pc (version 3.9) : [Python](https://www.python.org/downloads/release/python-3918/)
2.  Install the Selenium library using the command : `pip install selenium`
3.  Chrome browser and Google Webdriver (version 115 or newer) : [chromewebdriver](https://googlechromelabs.github.io/chrome-for-testing/)
### **Configuration** :
- Change the path for the Chrome driver in the code. For example, if the driver is located in C:\Windows\System32, update the path accordingly.
- To use the script.bat file, edit it to include the path for the code. Place the script.bat file in the C:\Windows\System32 folder for convenient execution from the command prompt.
### Execution :
**Manual Excution** : 
  - Run the Python file manually.
**Using Script File** :
  - After placing the script file in \system32, open the command prompt and type `wtscript` to execute the code.


