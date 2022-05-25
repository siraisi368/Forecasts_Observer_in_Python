import requests;
import json;

uri = "http://weather.tsukumijima.net/api/forecast/city/120020";
response = requests.get(uri);

js_l = json.loads(response.text);

print("\r\n" , js_l['forecasts'][0]['dateLabel'] , "(",js_l['forecasts'][0]['date'] , ")の千葉県の天気は" , js_l['forecasts'][0]['telop'],"です"); #場所+天気
print("最高気温:",js_l['forecasts'][0]['temperature']['max']['celsius'],"度") #最高気温 

print("\r\n", js_l['forecasts'][1]['dateLabel'] ,"(",js_l['forecasts'][1]['date'],")の千葉県の天気は",js_l['forecasts'][1]['telop'],"です"); #明日の天気
print("最高気温:",js_l['forecasts'][1]['temperature']['max']['celsius'],"度") #最高気温
print("最低気温:",js_l['forecasts'][1]['temperature']['min']['celsius'],"度") #最低気温

print("\r\n", js_l['forecasts'][2]['dateLabel'] ,"(",js_l['forecasts'][2]['date'],")の千葉県の天気は",js_l['forecasts'][1]['telop'],"です"); #明後日の天気
print("最高気温:",js_l['forecasts'][2]['temperature']['max']['celsius'],"度") #最高気温
print("最低気温:",js_l['forecasts'][2]['temperature']['min']['celsius'],"度") #最低気温
