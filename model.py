import pickle
import pandas as pd
from pathlib import Path

root = Path(".")
my_path = root / "model" / "finalized_model.sav"
model = pickle.load(open(my_path, 'rb'))
airport_ids  = pd.read_csv('CleanData/airport_id.csv',header=None)

def ontime (departure_date_time, origin, destination):
    from datetime import datetime
    try:
        departure_date_time_parsed = datetime.strptime(departure_date_time, "%d/%m/%Y")
    except ValueError as e:
        return 'Error parsing date/time - {}'.format(e)

    month = departure_date_time_parsed.month
    day = departure_date_time_parsed.day
    day_of_week = departure_date_time_parsed.isoweekday()
    hour = departure_date_time_parsed.hour
    
#     user_input = ('17/1/2020', 'SFO', 'IAD')
    origin = origin.upper()
    destination = destination.upper()
    
    aids = airport_ids[0].tolist()
    d = {'month': [month],'day': [day],'DAY_OF_WEEK': [day_of_week],'DEP_TIME': [hour]}
    for atype in ["ORIGIN","DEST"]:
        for aid in aids:
            d[atype + "_" + aid] = [0]
    d["ORIGIN" + "_" + origin] = [1]
    d["DEST" + "_" + destination] = [1]
    return(model.predict_proba(pd.DataFrame(d))[0][0])
