from datetime import datetime
date_str = "2025-01-17"
# result = datetime.strptime(date_str, date_str_format)

# print(type(result))
date_str_format = "Hora: %H:%M  Data: ( %d/%m/%Y )"
date_in_str = datetime.now().strftime(date_str_format)

print(date_in_str)
# date_now = datetime.strptime(, date_str_format)

# print(date_now)

dt = datetime.now().timestamp()
print(dt)

convertion = datetime.fromtimestamp(dt)
print(convertion)