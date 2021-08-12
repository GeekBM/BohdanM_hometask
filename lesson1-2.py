time = int(input('Enter time in seconds'))
days = time // (3600 * 24)
hours = (time - days * 3600 * 24) // 3600
minutes = (time - (days * 3600 * 24 + hours * 3600)) // 60
seconds = time - (days * 3600 * 24 + hours * 3600 + minutes * 60)
print(f'Time in format dd:hh:mm:ss {days:02} : {hours:02} : {minutes:02} : {seconds:02}')
