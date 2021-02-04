# **Explore US Bikeshare Data project**

### 04/Feb/2021


## **Description**
In this project, _Python_ is used to explore data related to _bike share systems_ for three major cities in the United States: _Chicago, New York City, and Washington_ for 2017.
- The source code takes in _raw_ input from the user to create an _interactive experience_.
- According to the input the code will import the data and will provide information by computing descriptive statistics.
- If user input were wrong program will return a list of all optional input for each question.

## **Files used**

- bikeshare.py
- chicago.csv
- new_york_city.csv
- washington.csv

## **Credits**

* Richard Kalehoff (Udacity mentor)

    - https://github.com/richardkalehoff

* Dhaval Patel (Software Engineer)

    - https://www.youtube.com/playlist?list=PLeo1K3hjS3usJuxZZUBdjAcilgfQHkRzW

* Juno Lee (Udacity Mentor)

    - https://github.com/junolee

* Yash Motwani (Data Enthusiast)

    - https://github.com/YashMotwani

## **Softwares needed:**
* _Python 3, NumPy_, and _Pandas_ installed using _Anaconda_.
* A text editor, like _Sublime_ or _Atom_.
* A terminal application (_Terminal_ on Mac and Linux or _Cygwin_ on Windows).

## **Code explained in Detail:**
### **How the program works:**
This code creates an interactive experience by _taking raw input_ from users to answer questions about the dataset that will _change the results!_ There are _five_ questions in total (can decrease to four depending on the user's answers):

* _Which city do you want to explore?_
* _Do you want to specify a month from the first six month of 2017? if so input the month name, else input "all"_
    * (If month was specified) _Do you want to specify a day of the week? if so please input the day name, else input "all"_

Answering those questions will decide which city and time data to be analyzed.

After viewing the desired data, users will can choose to see some raw data:
* _Do you want to see some raw data? if so please input "yes", else input anything._

And finally program can restart again by answering the next question:
* _Would you like to restart? if so please input "yes", else input anything._

## **The Datasets:**
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
