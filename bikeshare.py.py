# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 07:27:45 2023

@author: bayan
"""

import time
import pandas as pd
import numpy as np



CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

CITIES = ['chicago', 'new york', 'washington']

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']

DAYS = ['sunday', 'monday', 'tuesday', 'wednesday', \
        'thursday', 'friday', 'saturday' ]

def get_filters():
    """Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Would you like to see data for Chicago, New York City, or Washington?\n").lower()
        if city not in CITY_DATA:
            print("Invalid input. Please enter a valid city name.")
        else:
            break

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("Which month? January, February, March, April, May, June, or all?\n").lower()
        if month not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            print("Invalid input. Please enter a valid month name or 'all' for all months.")
        else:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Which day of the week? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or all?\n").lower()
        if day not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
            print("Invalid input. Please enter a valid day name or 'all' for all days.")
        else:
            break

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
    filename = CITY_DATA[city]
    df = pd.read_csv(CITY_DATA[city])

    # convert start time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # create new columns for month and day of week
    df['Month'] = df['Start Time'].dt.month_name()
    df['Day of Week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        df = df[df['Month'] == month.title()]
 # filter by day of week if applicable
    if day != 'all':
        df = df[df['Day of Week'] == day.title()]       

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['Start Time'].dt.month.mode()[0]
    print("The most common month is: ", common_month)

    # display the most common day of week
    common_day_of_week = df['Start Time'].dt.day_name().mode()[0]
    print("The most common day of week is: ", common_day_of_week)

    # display the most common start hour
    common_hour = df['Start Time'].dt.hour.mode()[0]
    print("The most common start hour is: ", common_hour)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station is: ", common_start_station)

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station is: ", common_end_station)

    # display most frequent combination of start station and end station trip
    df['trip'] = df['Start Station'] + ' - ' + df['End Station']
    common_trip = df['trip'].mode()[0]
    print("The most frequent combination of start station and end station trip is: ", common_trip)



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time is: ", total_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The mean travel time is: ", mean_travel_time)



def user_stats(df):
    """Displays statistics on bikeshare users."""
    
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Counts of user types:\n", user_types)

    # Display counts of gender (if applicable)
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print("Counts of gender:\n", gender)
    else:
        print("No gender data available for this city.")

    # Display earliest, most recent, and most common year of birth (if applicable)
    if 'Birth Year' in df:
        earliest_birth_year = int(df['Birth Year'].min())
        most_recent_birth_year = int(df['Birth Year'].max())
        most_common_birth_year = int(df['Birth Year'].mode()[0])
        print("Earliest birth year: ", earliest_birth_year)
        print("Most recent birth year: ", most_recent_birth_year)
        print("Most common birth year: ", most_common_birth_year)
    else:
        print("No birth year data available for this city.")



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
      
        # Code to display data
        start_index = 0
        increment = 5   
        while True:
            displayData = input('Would you like to see some raw data? ')
            if displayData.lower() == 'yes':
                # CODE TO DISPLAY RAW DATA
                print(df.iloc[start_index:start_index+increment])
                start_index += increment
            else:
                break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break







if __name__ == "__main__":
	main()