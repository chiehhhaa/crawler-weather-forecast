import requests

forecast_url = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWA-48CDBF71-C99E-42CC-9DED-5FA6ED0FB08C&format=JSON"

data = requests.get(forecast_url) # 使用 requests 中的 get 方法來拿到 forecast_url 中的內容
data_json = data.json() # 並將拿到的內容轉換成 json
locations = data_json['records']['location'] # 從 data_json 提取出鍵為 `records` 的值，並進一步從這個值中提取鍵為 `location` 的值

for location in locations: # locations 為 list，使用迴圈逐一處理每個地點的資料
    location_name = location['locationName']
    weather_description = ""
    max_temp = ""
    min_temp = ""
    pop = ""

    for element in location['weatherElement']: # location 中的 `weatherElement` 也是 list，使用迴圈逐一處理每個天氣元素
        if element['elementName'] == "Wx":
            weather_description = element['time'][0]['parameter']['parameterName']
        # 檢查當前天氣元素的類型是否為 "Wx"（天氣描述）如果是，則從該天氣元素的第一個時間段中提取天氣描述文字
        elif element['elementName'] == "MaxT": # 最高溫度
            max_temp = element['time'][0]['parameter']['parameterName']
        elif element['elementName'] == "MinT": # 最低溫度
            min_temp = element['time'][0]['parameter']['parameterName']
        elif element['elementName'] == "PoP": # 降雨機率
            pop = element['time'][0]['parameter']['parameterName']

    print(f"{location_name} 未來 8 小時 {weather_description}，最高溫 {max_temp} 度，最低溫 {min_temp} 度，降雨機率 {pop} %")

