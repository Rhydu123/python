import re
text = "Here are some dates: 01/25/2023, 12/31/2023, and 13/32/2023."
date_pattern = r'(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/\d{4}'
matched_dates = re.findall(date_pattern, text)

for date in matched_dates:
    print(date)
