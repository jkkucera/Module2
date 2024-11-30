meters = float(input('Enter meters: '))
unit = input('Select convertion unit (miles/yards/inches): ').strip().lower()

units = {
    'miles': meters * 0.000621371,
    'yards': meters * 1.09361,
    'inches': meters * 39.3701
}

if unit in units:
    print(f'{meters} meters is',units[unit], unit)
else:
    print('Invalid units')