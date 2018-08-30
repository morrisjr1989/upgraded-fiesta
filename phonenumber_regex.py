import re
phonePattern = re.compile(r'(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')
PhoneNumber_list = recent_sales_data_df_grouped.PhoneNumber.tolist()
for number in PhoneNumber_list:
        try:
            print(phonePattern.search(number).groups())
        except AttributeError: pass