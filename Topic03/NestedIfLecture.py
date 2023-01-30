action_dance = 'Start to dance!'
action_snowman = 'Build a snowman!'
action_bike = 'Ride your bike!'
action_bad_weather = 'Stay inside!'

WEATHER_SNOW = 'snowing'
WEATHER_RAIN = 'raining'
WEATHER_SUNNY = 'sunny'

current_weather = 'raining'
current_clothes = 'raincoat'

if(current_weather == WEATHER_RAIN):
    if(current_clothes == 'raincoat'):
        print(action_dance)
    else:
        print('Put on rain gear.')
elif (current_weather == WEATHER_SNOW):
    print(action_snowman)
elif (current_weather == WEATHER_SUNNY):
    print(action_bike)
else:
    print(action_bad_weather)

a_list = ['apple, banana, cherry']
if ('apple' in a_list):
    print('Apple is in the list!')
if ('banana' in a_list):
    print('found banana')
