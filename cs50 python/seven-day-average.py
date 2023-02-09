import csv
import requests


def main():
    # Read NYTimes Covid Database
    download = requests.get(
        "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv"
    )
    decoded_content = download.content.decode("utf-8")
    file = decoded_content.splitlines()
    reader = csv.DictReader(file)

    # Construct 14 day lists of new cases for each states
    new_cases = calculate(reader)

    # Create a list to store selected states
    states = []
    print("Choose one or more states to view average COVID cases.")
    print("Press enter when done.\n")

    while True:
        state = input("State: ")
        if state in new_cases:
            states.append(state)
        if len(state) == 0:
            break

    print(f"\nSeven-Day Averages")

    # Print out 7-day averages for this week vs last week
    comparative_averages(new_cases, states)


# Create a dictionary to store 14 most recent days of new cases by state
def calculate(reader):
    new_cases = {}
    previous_cases = {}
    for row in reader:
        state = row["state"]
        state_cases = new_cases.get(state, [])
        prev = previous_cases.get(state, 0)
        new = int(row["cases"])
        state_cases.append(new - prev)
        if len(state_cases) > 14:
            state_cases.pop(0)
        new_cases[state] = state_cases
        previous_cases[state] = new

    return new_cases

# Calculate and print out seven day average for given state
def comparative_averages(new_cases, states):
    for state in states:
        state_cases = new_cases[state]
        try:
            cAvg = sum(state_cases[-7:]) / 7
            pAvg = sum(state_cases[:7]) / 7
            percent = (cAvg - pAvg) / pAvg * 100
            if percent >= 0:
                change = "n increase"
            else:
                change = " decrease"
            print(f'{state} had a 7-day average of {int(cAvg)} and a{change} of {int(percent)}%.')
        except ZeroDivisionError:
            print("Tried dividing by zero")

main()
