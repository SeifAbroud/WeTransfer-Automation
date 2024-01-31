# Wetransfere-automation
if u are tired of sending files through wetransfere and repeating steps (opening website > selecting send file option > selecting get link option > browsing the file explorer for file > waiting for upload > finally click on copy link )
this code may save you some time ( approximatly 20 sec , + u can do something else as it runs ). 
### About the code : 
this code lets u automate opening the website and uploading the file to directly get the link copied to clipboard and printed . 
There are Two versions for this code : 
  - wetransfere-autoamtion1 : takes the path file as an input , and it will priant link directly . in this version you will see the process as it folds , you can see the chrome browser as it beign auotmated . 
  - wetransfere-autoamtion1.1 : the same code but its headless , meaning all the autoamtion is happening in the background and you will get the link copied to clipboard directly .
  - Wtscript.bat : this file lets u excute the code right from the cmd , it will save you more of time .
## Setup :
### **for This code you need** : 
1.  Python installed in your pc (python 3.9) : [Python](https://www.python.org/downloads/release/python-3918/)
2.  also need Selenium library u can download it after installing python with : `pip install selenium`
3.  you need to have chrome browser aswell as google Webdriver (version 115 or newer ) : [chromewebdriver](https://googlechromelabs.github.io/chrome-for-testing/)
### **How to use** :
- you need to change the path for the chrome **driver** in the code . ( in this case , the driver is in C:\Windows\System32)
- To use the script.bat file , first you need to edit it and put the path for the Code , then put the script.bat file in the C:\Windows\System32 folder so you can excute it directly from the cmd .
  ### Excute :
  **How to run the code** : 
you can manually run the python file . Or
you can use the script file , after placing it in \systeme32 , you can open the CMD and type `wtscript` to Excute the code . 


