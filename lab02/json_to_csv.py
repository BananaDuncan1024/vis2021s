import csv
import json
import sys
import pandas as pd

f = open("weather.json", 'r',encoding="utf-8")
#print(f.read())
weather_json = json.loads(f.read())
#print(weather_json)
weatherdata = []
#print(weather_json['cwbopendata']['location'])

def covet_to_csv():
    #value = json_object
    #with open("weather.csv", 'w') as f: 
    #wr = csv.DictWriter(f, fieldnames = info[0].keys()) 
    df = pd.json_normalize(weatherdata)
    #wr.writeheader() 
    df.to_csv("weather.csv",encoding="utf-8")
    #wr.writerows(info) 


def data_clear():
    
    weather_city = None
    weather_town = None
    weather_rain = None

    for model in weather_json['cwbopendata']['location']:
        for dataRain in model['weatherElement']:
            if dataRain['elementName'] == "HOUR_24":
                weather_rain = dataRain['elementValue']['value']
                #print(weather_rain)
        for dataCity in model['parameter']:
            if dataCity['parameterName'] == "CITY":
                weather_city = dataCity['parameterValue']
                #print(weather_city)
            elif dataCity['parameterName'] == "TOWN":
                weather_town = dataCity['parameterValue']
                #print(weather_town)
        weathermodel = {
            "City":weather_city,
            "Town":weather_town,
            "Rain_24":weather_rain
        }
        weatherdata.append(weathermodel)

    #print(weatherdata)
    covet_to_csv()



def write_csv(title, rows, csv_file_name):
    with open(csv_file_name, 'w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=title)
        writer.writeheader()
        writer.writerows(rows)


def json_to_csv(object_list):
    global json_ob, c_line
    json_ob = {}
    c_line = 0
    # for ov in object_list :
    # for ov in object_list:
        # loop_data(ov)
        # c_line += 1
    with open("json檔案路徑.json", "r") as f:
        for ov in f :
            ov = json.loads(ov.strip())
            loop_data(ov)
            c_line += 1
    title, rows = get_title_rows(json_ob)
    write_csv(title, rows, 'csv檔案儲存路徑.csv')

#json_to_csv(o)

if __name__ == '__main__':

    data_clear()
