months = ['Janary', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
endings = ['st', 'nd', 'rd'] + 17 * ['th'] + \
          ['st', 'nd', 'rd'] + 7 *['th'] + ['st']

year = input('Year:')
month = input('Month(1-12):')
day = input('Day(1-31):')

month_name = months[int(month) - 1]
ordinal = day + endings[int(day) -1]

print (month_name + ' ' + ordinal + ',' + year)
