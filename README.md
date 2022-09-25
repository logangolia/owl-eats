# HackRice12 Project: OwlEats - A Rice Servery App

## Contributors: Micheal Yu, Logan Golia, Bryant Huang, Kevin Ni

### Description:
This Android app predicts current and future servery line wait time at Rice University.

### Implementation: 
Python simulation: 
In practice, we would want to estimate wait times based on empirically collected data of servery activity. While this data is most likely already being collected by Rice University, by means of recording swipes into servery buildings and swipes into the servery, even if it is not, this data is very easily collectable. However, since we currently do not have access to this data, we first wrote a Python script to synthetically generate realistic servery activity data. Then, we designed an algorithm to calculate the estimated live wait time for each given minute, given the number of people swiping into the servery building, which we assume is the number of people entering the queue, the number of people swiping into the servery, which is the number of people leaving the queue, and an assumed average service time of 5 seconds which represents the time it takes for someone to swipe into the servery and grab a plate; this service time can be statistically calculated once more data is collected. Finally, we were able to predict future wait times within each time interval by taking into account previous wait times on this day and within this time interval in the past. We display these future wait times as a bar graph with our x-axis being the time of day and our y-axis being the estimated wait time. The Python script also compiles live wait time in minutes at every minute into a txt file, which is then sent to the Android Studio app interface. The Python script sends a new txt file each minute, and its contents include all the wait times since the start of the meal period. 

Android Studio:
As mentioned earlier, the Android Studio interface receives the txt files of past wait times to calculate the current wait time, and a bar graph of predicted wait times for the current dining period. The graph of future prediction is displayed on top of each specific servery page. We employ a multi-threading technique to update current wait time after every minute using information from the txt file. We take in system clock time and use the data from past times in the day’s current dining period to compute current wait time, each of which is displayed to the side of each servery's button. 
