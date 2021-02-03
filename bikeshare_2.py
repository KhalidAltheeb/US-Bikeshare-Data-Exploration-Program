import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Which city do you want to explore? ")
        city = city.lower()
        if city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print('invalid input. Please input one of these cities: (chicago, new york city, or washington)')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Do you want to specify a month from the first six month of 2017? if so input the month name, else input "all": ')
        month = month.lower()
        if month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            break
        else:
            print('invald input. Please input one of these choices:(january, february, march, april, may, june, or all')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Do you want to specify a day of the week? if so please input the day name, else input "all": ')
        day = day.lower()
        if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
            break
        else:
            print('invald input. Please input one of these:(monday, tuesday, wednesday, thursday, friday, saturday, sunday, or all')
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('The most common month is: ', df['month'].mode()[0], '\n')

    # TO DO: display the most common day of week
    print('The most commen day of the week is: ', df['day_of_week'].mode()[0], '\n')

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print('The most common start hour is: ', df['hour'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Most commonly used start station is: ', df['Start Station'].mode()[0], '\n')

    # TO DO: display most commonly used end station
    print('Most commonly used end station is: ', df['End Station'].mode()[0], '\n')

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + ' ' + df['End Station']
    print('Most frequent combination of start station and end station trip is: ', df['combination'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total travel time is: ', df['Trip Duration'].sum(), '\n')

    # TO DO: display mean travel time
    print('Mean travel time is: ', df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df.groupby(['User Type'])['User Type'].count()
    print(user_type, '\n')
    if city != 'washington':
        # TO DO: Display counts of gender
        gen = df.groupby(['Gender'])['Gender'].count()
        print(gen)
        # TO DO: Display earliest, most recent, and most common year of birth
        earliest = sorted(df.groupby(['Birth Year'])['Birth Year'])[0][0]
        most_recent = sorted(df.groupby(['Birth Year'])['Birth Year'], reverse=True)[0][0]
        most_common_year = df['Birth Year'].mode()[0]
        print('The earliest year of birth is: ', earliest)
        print('The most recent year of birth is: ', most_recent)
        print('The most common year of birth is: ', most_common_year)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    x = 1
    while True:
        raw = input('Do you want to see some raw data? if so please input "yes", else input anything.\n')
        if raw.lower() == 'yes':
            print(df[x:x+5])
        else:
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? if so please input "yes", else input anything.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
