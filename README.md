### Date created
04/Feb/2021
### Project Title
Explore US Bikeshare Data

### Description
In this project, Python is used to explore data related to bike share systems for three major cities in the United States — Chicago, New York City, and Washington for 2017.
- The source code takes in raw input from the user to create an interactive experience.
- According to the input the code will import the data and will provide information by computing descriptive statistics.
- If user input were wrong program will return a list of all optional input for each question.

### Files used

bikeshare.py
chicago.csv
new_york_city.csv
washington.csv

### Credits

* Richard Kalehoff (Udacity mentor)

    - https://github.com/richardkalehoff

* Dhaval Patel (software engineer)

    - https://www.youtube.com/playlist?list=PLeo1K3hjS3usJuxZZUBdjAcilgfQHkRzW

* Juno Lee (Udacity Mentor)

    - https://github.com/junolee

* Yash Motwani (data enthusiast)

    - https://github.com/YashMotwani

## Softwares needed:
    * Python 3, NumPy, and Pandas installed using Anaconda.
    * A text editor, like Sublime or Atom..
    * A terminal application (Terminal on Mac and Linux or Cygwin on Windows).

## Code explained in Detail:
### How the program works:
This code creates an interactive experience by taking raw input from users to answer questions about the dataset that will change the results! There are five questions in total (can decrease to four depending on the user's answers):

* Which city do you want to explore?
* Do you want to specify a month from the first six month of 2017? if so input the month name, else input "all"
    * (If month was specified) Do you want to specify a day of the week? if so please input the day name, else input "all"

Answering those questions will decide which city and time data to be analyzed.

After viewing the desired data, users will can choose to see some raw data:
* Do you want to see some raw data? if so please input "yes", else input anything.

And finally program can restart again by answering the next question:
* Would you like to restart? if so please input "yes", else input anything.

### The Datasets:
Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:

- Start Time (e.g., 2017-01-01 00:07:57)
- End Time (e.g., 2017-01-01 00:20:53)
- Trip Duration (in seconds - e.g., 776)
- Start Station (e.g., Broadway & Barry Ave)
- End Station (e.g., Sedgwick St & North Ave)
- User Type (Subscriber or Customer)

The Chicago and New York City files also have the following two columns:

- Gender
- Birth Year
