# import module
import requests
from bs4 import BeautifulSoup


# input by geek
from_Station_code = "ndls" 
from_Station_name = "new delhi"

To_station_code = "adi"
To_station_name = "ahmdabad"
# url
r = requests.get("https://www.railyatri.in/booking/trains-between-stations?from_code="+from_Station_code+"&from_name="+from_Station_name+"+JN+&journey_date=+Wed&src=tbs&to_code=" + \
	To_station_code+"&to_name="+To_station_name + \
	"+JN+&user_id=-1603228437&user_token=355740&utm_source=dwebsearch_tbs_search_trains")
# r=requests.get('https://www.ixigo.com/search/result/train/NDLS/ADI/02012023//1/0/0/0/ALL')
print(r.status_code)
soup=BeautifulSoup(r.content,"html.parser")
# print(soup)
data_str = ""

for item in soup.find_all("div", class_="namePart"):
    data_str = data_str + item.get_text()

result = data_str.split("\n")
print(result)

print("")
  
# Display the result
for item in result:
    if item != "":
        print(item)

# print('result :',result[1])
# train_no=result[1][0:5]
# print('train_no:',train_no)

# https://www.railyatri.in/seat-availability/
# {train_no}-asr-lku?journey_date=31-12-2022&quota=GN&
# train_full_name={result[1]}&
# train_boarding_from=ASR%20|%20AMRITSAR%20JN&train_boarding_to=LKU%20|%20LAL%20KUAN&journey_class
# =SL&utm_source=tbs_seo_result_dweb_header_sa