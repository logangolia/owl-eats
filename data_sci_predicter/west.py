import random

import matplotlib.pyplot as plt
import numpy as np


def west_data():
    '''
    Generates 125 data points to simulate servery activity in a given weekday lunch period (
    :return: 125 tuples of the form (# of ppl swiping into the college servery building, # of ppl swiping into
    the servery, current wait time)
    '''

    # represent data as (# in, # out, wait time)
    # 1) generate points before servery opens
    # 2) 11:30 - 12:00
    # 3) 12:00 - 12:30
    # 4) 12:30 - 1:00
    # 5) 1:00 - 1:30

    lst_data = []
    length_line = 0
    # number of swipes into the servery in one minute assuming there always exists a line (for the entire minute)
    service_time = 5
    max_out = 60 / service_time
    #1


    for x in range(5):
        num_in = random.randint(1, 5)
        num_out = 0
        wait_time = length_line * service_time / 60
        data_point = (num_in, num_out, round(wait_time, 2))
        lst_data.append(data_point)
        length_line += num_in - num_out

    #2
    for x in range(30):
        num_in = random.randint(5, 15)
        if length_line + num_in >= max_out:
            num_out = max_out
            wait_time = length_line * service_time /60
            data_point = (num_in, num_out, round(wait_time, 2))
            length_line += num_in - num_out
        else:
            num_out = length_line + num_in
            wait_time = length_line * service_time / 60
            data_point = (num_in, num_out, round(wait_time, 2))
            length_line = 0
        lst_data.append(data_point)

    #3
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

    #4
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

    #5
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
    return lst_data

    #x = 0
    #for elem in lst_data:
     #   x += 1
     #   print(elem, x)


def future_prediction():
    '''
    Creates a bar graph of wait times vs time that predicts wait times at a given time based on previous wait times
    at this time in the past.
    :return: plot: a bar graph of wait times vs time
    '''
    lst_previous_data = []

    for x in range(5):
        lst_previous_data.append((west_data()))

    prediction_data = []
    for i in range(len(west_data())):
        total = 0
        for j in range(5):
            total += lst_previous_data[j][i][2]
        avg = total/5
        prediction_data.append(avg)

    y_values = []
    # make y values of bar graph
    for i in range(0, len(prediction_data), 5):
        total = 0
        for j in range(5):
            total += prediction_data[i+j]
        total /= 5
        y_values.append(total)

    # make x values of bar graph
    x_values = []
   # x_values = ['11:30', '11:35', ]
    # 11 o clock
    for minute in range(25, 60, 5):
        x_val = '11:' + str(minute)
        x_values.append(str(x_val))
    # 12 o clock
    for minute in range(0, 60, 5):
        if minute == 0:
            minute = str(minute) + '0'
        elif minute == 5:
            minute = '0'+ str(minute)
        x_val = '12:' + str(minute)
        x_values.append(str(x_val))
    # 1 o clock
    for minute in range(0, 30, 5):
        if minute == 0:
            minute = str(minute) + '0'
        elif minute == 5:
            minute = '0' + str(minute)
        x_val = '1:' + str(minute)
        x_values.append(str(x_val))

    fig = plt.figure(figsize=(10, 5))

    # creating the bar plot
    plt.bar(x_values, y_values, color='maroon',
            width=0.4)

    plt.xlabel("Time of day")
    plt.ylabel("Wait time (min.)")
    plt.title("Predicted wait time vs time of day")
    plt.show()

future_prediction()








