# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to
# achieve the program requirements.

from data_manager import DataManager

sheet_data = DataManager().get_sheet_data()
print(sheet_data)
