import time as time
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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ['new york city', 'washington', 'chicago']

    city = str ( input ('\nWould you like to see date for New York, Chicago or Washington?\t').lower())
    while city not in cities:
        city = str ( input ('\nEnter please the city: New York City, Chicago, Washington\t').lower())


    # get user input for month (all, january, february, ... , june)
    monts_and_all = ['january', 'february', 'march', 'april', 'may', 'june', 'all']

    month = str ( input ('\nPlease enter a month: january, february, march, april, may, june or "all" for all\t').lower())

    while month not in monts_and_all:
        month = str ( input ('\nPlease enter a month: january, february, march, april, may, june or "all" for all\t').lower())

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day_and_all = ['sunday', 'monday', 'thuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']

    day = str ( input('\nPlease enter a day: sunday, monday, thuesday, wednesday, thursday, friday, saturday or "all" for all\t').lower())

    while day not in day_and_all:
        day = str ( input('\nPlease enter a day: sunday, monday, thuesday, wednesday, tursday, friday, saturday or "all" for all\t').lower())


    print('-'*40)
    print('Filtered parameters:', city, month, day)
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

    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour


    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print ('\nMost common month:\t', df['month'].mode()[0])

    # display the most common day of week
    print ('\nMost common day of week:\t', df['day_of_week'].mode()[0])

    # display the most common start hour
    print ('\nMost common hour:\t', df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('\nMost commonly used start station:\t', df['Start Station'].mode()[0])

    # display most commonly used end station
    print('\nMost commonly used end station:\t', df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip
    print('\nMost frequent combination of start station and end station trip:\t', (df['Start Station'] + df['End Station']).mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('\nTotal travel time:\t', (total_travel_time // 60 // 60), 'Hours', \
    (total_travel_time // 60 % 60), 'Minutes', \
    total_travel_time // 60 //60 % 60, 'seconds')

    # display mean travel time
    travel_time = df['Trip Duration'].mean()
    print('\nMean travel time:\t',(total_travel_time // 60 % 60), 'Minutes', \
    total_travel_time // 60 //60 % 60, 'seconds')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('\nCounts of user types:\n', df['User Type'].value_counts())

    # Display counts of gender
    if 'Gender' in df.columns:
        print('\nCounts of gender:\n', df['Gender'].value_counts())
    else:
        print('for Washington there are no statistics "Gender"')

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('\nEarlier year of birth\t', df['Birth Year'].min())
        print('\nMost recent year of birth\t', df['Birth Year'].max())
        print('\nCommon year of birth\t', df['Birth Year'].mean())
        print("\nThis took %s seconds." % (time.time() - start_time))
    else:
        print('for Washington there are no statistics "Year Birth"')
        print('-'*40)



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)



        time_stats(df)
        line5 = input('\nWould you like to see Station Statistics? Enter yes or no.\n')
        while line5.lower() != 'yes':
            line5 = input('\nWould you like to see Station Statistics? Enter yes or no.\n')

        station_stats(df)
        line5 = input('\nWould you like to see Trip duration Statistics? Enter yes or no.\n')
        while line5.lower() != 'yes':
            line5 = input('\nWould you like to see Trip duration Statistics? Enter yes or no.\n')

        trip_duration_stats(df)
        line5 = input('\nWould you like to see User Statistics? Enter yes or no.\n')
        while line5.lower() != 'yes':
            line5 = input('\nWould you like to see User Statistics? Enter yes or no.\n')
        user_stats(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":

	main()
