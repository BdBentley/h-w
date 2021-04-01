#   --SNOWFALL PROGRAM--
#   This program will ask for a users input and keep track of snow for three months. The total snowfall will
#   display at the end of the third month. The weatherman also want's to find out if the record has been broken and
#   test to see if the total snowfall was greater than 24 inches. If snowfall is greater than 24 inches, message will
#   display the number of inches that broke the record OR if the record was not broken then display a message that
#   says the snowfall was average for the season.
#   Program should also validate that the information input for each month is not less than zero. If zero is entered,
#    the program should prompt the user to try again.
#
#   - Bentley 11/1/2020

# Assign variables.

snowfall = 0
total_Snowfall = 0
recordSnowfall = 24
highestSnowfall = 0
brokenRecordCheck = 0

# Gather data for each month.

months = 3
monthCount = 1

# Make sure that the months are less than three by setting a while loop with a counter.

while monthCount <= months:

    # Have the user enter their info and all that jazz, no exception cases yet.

    print("Please enter the amount of snowfall for the month of " + str(monthCount) + ": ")
    snowfall = float(input('>>'))

    # Set up the variable to receive the highest snowfall number

    if snowfall > highestSnowfall:
        highestSnowfall = snowfall

    # Check for the highest snowfall.

    while snowfall < 0:
        print("Snowfall for the month cannot equal less than zero.")
        print("Please enter the amount of snowfall for the month of " + str(monthCount) + ": ")
        snowfall = float(input('>>'))

        # Add up the snowfall total.
    total_Snowfall = total_Snowfall + snowfall
    monthCount = monthCount + 1

    if snowfall > recordSnowfall:
        brokenRecordCheck = brokenRecordCheck + 1

# Set variables up for the average and the broken record to neaten things up with a rounding.
averageSnowfall = total_Snowfall/months
brokenRecord = highestSnowfall - recordSnowfall

# Print Statements. I used the .rjust here to adjust the output and keep things neat. The characters will fill empty
# space and give us a good looking output for the most part.I also used a function that rounds the number to one
# decimal. This helps prevent us having cluttered output. https://www.geeksforgeeks.org/python-output-formatting/
print("Snowfall amount in inches".rjust(77, '-'))
print("The total amount of snow is:", str(round(total_Snowfall, 1)).rjust(27, ' '))
print("The average amount of snow is:", str(round(averageSnowfall, 1)).rjust(25, ' '))
print("The highest amount of snow is:", str(round(highestSnowfall, 1)).rjust(25, ' '))
if brokenRecordCheck > 0:
    print("Record snowfall has broken the 24\" mark by " + str(round(brokenRecord, 1)) + " inches!")
else:
    print("The snow this season did not break the 24\" amount!.")




