<pre>
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
    cities =['chicago', 'new york city', 'washington']
    city = input("Would you like to data for (chicago, new york city or washington)?\n").lower()
    while city not in cities:
                 city = input("Wronge answer, Enter name of city (chicago, new york city, washington)\n").lower()
    month, day = 'all', 'all'
    choices =['month', 'day', 'both', 'all']
    choice = input("Would you like to filter by (month, day, both or not all)?\n").lower()
    while choice not in choices:
                 choice = input("Wrong answer, Enter choice of filter (month, day, both or all)\n").lower()     
    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    if choice == 'month' or choice == 'both':
                 month = input("Wich month(January, February, March, April, May, or June)?\n").title()
                 while month not in months:
                        month = input("Wrong answer, Enter month(January, February, March, April, May, or June)?\n").title()
                 

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    if choice == 'day' or choice == 'both':
                 day = input("Wich day(Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday)?\n").title()
                 while day not in days:
                        day = input("Wrong answer, Enter day(Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday)?\n").title()

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
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day of week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    #     filter by month if applicable
    if month != 'all':
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month =months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day of week'] == day.title()]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]

    # TO DO: display the most common day of week
    most_common_day_of_week = df['day of week'].mode()[0]

    # TO DO: display the most common start hour
    common_start_hour = df['hour'].mode()[0]
    print('most common month: {}\nmost common day of week: {}\ncommon hour of day: {}'.format(most_common_month, most_common_day_of_week, common_start_hour))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_start_station = df['Start Station'].mode()[0]

    # TO DO: display most commonly used end station
    most_end_station = df['End Station'].mode()[0]

    # TO DO: display most frequent combination of start station and end station trip
    df['Trip'] = df['Start Station'] + ' to ' + df['End Station']
    most_station_trip = df['Trip'].mode()[0]
    print("most common start station: {}\nmost common end station: {}\nmost common trip from start to end: {}".format(most_start_station, most_end_station, most_station_trip))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    
    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()

    # TO DO: display mean travel time
    average_travel_time = df['Trip Duration'].mean()
    
    print("total travel time: {}\naverage travel time: {}".format(total_travel_time, average_travel_time))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    # TO DO: Display counts of user types
    count_user_type = df['User Type'].value_counts()
    print("counts of each user type are: \n{}".format(count_user_type))

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        count_of_gender = df['Gender'].value_counts()
        print("counts of each gender are: \n{}".format(count_of_gender))
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest = df['Birth Year'].min()
        print("oldest user is born of the year: {}".format(earliest))
        most_recent = df['Birth Year'].max()
        print("youngest user is born of the year: {}".format(most_recent))
        most_years_of_birth = df['Birth Year'].mode()[0]
        print("most users are born of the year: {}".format(most_years_of_birth))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    print('\nCalculating display raw data...\n')
    show = input("Would you like to Display data? Enter yes or no.\n").lower()
    while show != 'no':
        if show == 'yes':
            print(df.sample(5))
            show = input("Would you like to Display data? Enter yes or no.\n").lower()
        else:
            show = input("Wrong answer, Would you like to Display data? Enter yes or no.\n").lower()
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        while restart.lower() not in ['yes','no']:
            restart = input("\nWrong answer, Would you like to restart? Enter yes or no.\n")
        if restart.lower() == 'no':
                break
        

if __name__ == "__main__":
	main()
</pre>