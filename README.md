## To refresh a webpage automatically

In order to run the script: 

1. Clone the Repository
2. Change the present working directory to the directory where the files of this repositories are located.
3. Run the following command: "pip install -r requirements.txt"
4. Before running the script make sure that you download the chromedriver and the version of that must match the version of your Google Chrome Application installed on your PC or laptop.
5. To know the version of installed Google Chrome 
   Open Google Chrome -> Click three dots icon on the right most side on top --> Point the cursor on Help --> Click on About Google Chrome.
   You will find the current Google Chrome Version version something like "86.0.4820.183"
6. Now install the compatible chromedriver from the following website "https://chromedriver.chromium.org/" 
7. Note on checking compatibility, to check if the chromedriver is compatible with the installed Google Chrome make sure that the first digits before the decimal match in both the chromedriver you are going to install and the Google Chrome that you have already installed.
   For example: Google Chrome version - 86.0.4820.183 AND chromedriver version - 86.0.4240.22 are compatible because "86" is common in both.
                Contrastingly, Google Chrome version - 86.0.4820.183 AND chromedriver version - 87.0.4240.22 are not compatible because "86" does not equal to "87".
8. Voila! Champ you did all the hard stuff and now its your time to enjoy the fruits of your hardwork. Run the python script in refresh.py just like you run any other python command ie. python refresh.py
