import random
import sys
import matplotlib.pyplot as plt


def live_data():
    """
    Generates 125 data points to simulate servery activity in a specific weekday lunch period (e.g. Thursday lunch)
    return: 125 tuples of the form (num_in, num_out, wait_time)
    num_in - # of ppl swiping into the college servery building during this minute
    num_out - # of ppl swiping into the servery during this minute
    wait_time - current wait time (in min.) at this minute
    """

    lst_data = []
    length_line = 0
    # estimated average time (in sec.) it takes to enter the servery once at the front of the line (aka swipe time)
    service_time = 5
    # number of swipes into the servery in one minute assuming there always exists a line (for the entire minute)
    # if there exists a line, this is a constant rate since the rate of people entering the servery will be the same
    # whether the line is 10 people long or 50 people long.
    max_out = 60 / service_time

    # 1) generate data points between 11:25 - 11:30 (before the servery opens)
    # since the servery is closed, people cannot enter the servery so num_out = 0 and num_in, length_line, wait_time
    # keeps increasing
    for x in range(5):
        num_in = random.randint(1, 5)
        num_out = 0
        wait_time = length_line * service_time / 60
        data_point = (num_in, num_out, round(wait_time, 2))
        lst_data.append(data_point)
        length_line += num_in - num_out

    # 2) generate data points between 11:30 - 12:00
    # now that the servery is open, the logic is a bit different
    # if there exists a line given this new num_in, we can assume that num_out = max_out
    # if there is no line given this new num_in, we make the relatively safe assumption that everyone who enters the
    # servery building this minute can also enter the servery this same minute
    # and length_line should be updated to 0 for the next minute
    for x in range(30):
        num_in = random.randint(5, 15)
        if length_line + num_in >= max_out:
            num_out = max_out
            wait_time = length_line * service_time / 60
            data_point = (num_in, num_out, round(wait_time, 2))
            length_line += num_in - num_out
        else:
            num_out = length_line + num_in
            wait_time = length_line * service_time / 60
            data_point = (num_in, num_out, round(wait_time, 2))
            length_line = 0
        lst_data.append(data_point)

    # 3) generate data points between 12:00 - 12:30 (popular lunchtime so num_in values are greater)
    for x in range(30):
        num_in = random.randint(10, 25)
        if length_line + num_in >= max_out:
            num_out = max_out
            wait_time = length_line * service_time / 60
            data_point = (num_in, num_out, round(wait_time, 2))
            length_line += num_in - num_out
        else:
            num_out = length_line + num_in
            wait_time = length_line * service_time / 60
            data_point = (num_in, num_out, round(wait_time, 2))
            length_line = 0
        lst_data.append(data_point)

    # 4) generate data points between 12:30 - 1:00
    for x in range(30):
        num_in = random.randint(5, 12)
        if length_line + num_in >= max_out:
            num_out = max_out
            wait_time = length_line * service_time / 60
            data_point = (num_in, num_out, round(wait_time, 2))
            length_line += num_in - num_out
        else:
            num_out = length_line + num_in
            wait_time = length_line * service_time / 60
            data_point = (num_in, num_out, round(wait_time, 2))
            length_line = 0
        lst_data.append(data_point)

    # 5) generate data points between 1:00 - 1:30
    for x in range(30):
        num_in = random.randint(5, 10)
        if length_line + num_in >= max_out:
            num_out = max_out
            wait_time = length_line * service_time / 60
            data_point = (num_in, num_out, round(wait_time, 2))
            length_line += num_in - num_out
        else:
            num_out = length_line + num_in
            wait_time = length_line * service_time / 60
            data_point = (num_in, num_out, round(wait_time, 2))
            length_line = 0
        lst_data.append(data_point)

    # create a string of live wait times at each minute to generate a .txt file of the wait times, with each wait time
    # on a new line. This file will be sent to Android Studio in order to display the live wait times in the app.
    # wait_time_str = ''
    # for elem in lst_data:
    #     wait_time_str += str((round(elem[2], 1)))
    #     wait_time_str += '\n'
    # can return wait_time_str if we want to create the .txt file of the wait times
    return lst_data

# creates the .txt file of wait times at each minute (if we return wait_time_str instead of lst_data)
# to be sent to Android Studio
# sys.stdout = open('wait_times.txt', 'w')
# print(live_data())
# sys.stdout.close()

# uncomment to generate live data of servery activity
# print(live_data())


def future_prediction():
    """
    Creates a bar graph of wait times vs time of day that displays predictions of wait times at a given time
    based on previous wait times at this time in the past.
    """

    lst_previous_data = []
    # generate data points for the past 5 lunches on a particular weekday (e.g. past 5 Thursday lunches)
    for x in range(5):
        lst_previous_data.append((live_data()))

    # calculates average wait times at each minute from the previous 5 Thursday lunches in order to predict the wait
    # times for today's lunch (the current Thursday lunch)
    prediction_data = []
    for i in range(len(live_data())):
        total = 0
        for j in range(5):
            total += lst_previous_data[j][i][2]
        avg = total/5
        prediction_data.append(avg)

    # append 5 0's to the end of the list to make the list a multiple of 10, so we can group it into chunks of 10 later.
    # this is okay since these data points represent the wait times from 1:30 - 1:35, but these must be 0 since the
    # servery is closed at these times.
    for x in range(5):
        prediction_data.append(0)

    # the width of each time interval for the x-values in the bar graph.
    interval = 10

    # make y values of bar graph
    # groups every 10 elements together and calculates the average wait time of all 10 of them to represent the
    # predicted wait time for this entire time interval
    y_values = []
    for i in range(0, len(prediction_data), interval):
        total = 0
        for j in range(interval):
            total += prediction_data[i+j]
        total /= interval
        y_values.append(total)

    # make a list to represent the x values of the bar graph which are the different times in which the servery is open
    # separated by 10-min time intervals (this interval time can be changed, but it was selected to best represent
    # the data on a mobile device while still retaining useful predicted wait time information for the user.
    x_values = []
    # create strings for 11 o'clock times
    for minute in range(30, 60, interval):
        x_val = '11:' + str(minute)
        x_values.append(str(x_val))
    # create strings for 12 o'clock times
    for minute in range(0, 60, interval):
        if minute == 0:
            minute = str(minute) + '0'
        # in case we want to use 5-minute time intervals
        elif minute == 5:
            minute = '0'+ str(minute)
        x_val = '12:' + str(minute)
        x_values.append(str(x_val))
    # create strings for 1 o'clock times
    for minute in range(0, 31, interval):
        if minute == 0:
            minute = str(minute) + '0'
        elif minute == 5:
            minute = '0' + str(minute)
        x_val = '1:' + str(minute)
        x_values.append(str(x_val))

    # create the bar plot
    fig = plt.figure(figsize=(10, 5))
    plt.bar(x_values, y_values, color='deepskyblue',
            width=0.4)
    plt.xlabel("Time of day")
    plt.ylabel("Wait time (min.)")
    plt.title("Predicted Wait Times")
    plt.show()

# uncomment to generate a bar graph of the predictions of future wait times
# future_prediction()











