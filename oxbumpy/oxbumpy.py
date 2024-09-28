import requests
import certifi

from hgutilities.utils import json
import pandas as pd

from display import Display


def load_data(year, event_type):
    url = f"https://bumps.live/data/{event_type.lower()}_{year}.json"
    response = requests.get(url, verify=certifi.where())
    response.raise_for_status()
    data = response.json
    return data

def read_json(file_name):
    with open(file_name, "r") as file:
        data = json.load(file)
    return data

def get_df(season_data):
    rows = []
    for college, college_data in season_data.items():
        for sex, sex_data in college_data.items():
            for boat_number, boat_data in enumerate(sex_data):
                add_boat_history(rows, college, sex, boat_number, boat_data)
    df = pd.DataFrame(rows)
    return df

def add_boat_history(rows, college, sex, boat_number, boat_data):
    position = boat_data["start"]
    add_row(rows, college, sex, boat_number, 0, position, True)
    for day, move_data in enumerate(boat_data["moves"]):
        position -= move_data["moves"]
        add_row(rows, college, sex, boat_number, day+1, position, move_data["status"])

def add_row(rows, college, sex, boat_number, day, position, status):
    rows.append({"College": college, "Sex": sex, "Boat": boat_number + 1,
                 "Day": day, "Position": position, "Status": status})
    

def display(df, divs):
    display_obj = Display(df, divs)
    return display_obj
