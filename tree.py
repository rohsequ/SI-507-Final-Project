import json
from tqdm import tqdm
from front_page_ip.models import Country, State, City

# remove_keys = ['currency_name', 'currency_symbol', 'tld', 'native', 'region', 'subregion', 'timezones', 'translations', 'emoji', 'emojiU']
# f = open(r"static\data\countries+states+cities.json","rb")
# data = json.load(f)
# for cn_entry in data:
#     for keys in remove_keys:
#         del cn_entry[keys]
# with open(r"static\data\truncated_countries_states_cities.json", 'w') as fout:
#     json.dump(data , fout)


f = open(r"static\data\truncated_countries_states_cities.json","rb")
data = json.load(f)

for cn_entry in data:
    if cn_entry['name'] == "United States":
        country_obj = Country.objects.create(name=cn_entry['name'], 
                latitude=cn_entry['latitude'], longitude=cn_entry['longitude'])
        country_obj.save()
        for state in tqdm(cn_entry['states']):
            if state['cities'] and "Puerto Rico" not in state['name'] and "District" not in state['name']:
                state_obj = State.objects.create(name=state['name'], 
                    latitude=state['latitude'], longitude=state['longitude'], country=country_obj)
                state_obj.save()
                for city in state['cities']:
                    if "County" in city['name']:
                        pass
                    else:
                        city_obj = City.objects.create(name=city['name'], 
                            latitude=city['latitude'], longitude=city['longitude'], 
                            country=country_obj, state=state_obj)
                        city_obj.save()
                
# count = 0
# for cn_entry in data:
#     if cn_entry['name'] == "United States":
#         for state in (cn_entry['states']):
#             if state['cities'] and "Puerto Rico" not in state['name'] and "District" not in state['name']:
#                 print(state['name'])
#                 count+=1
#                 for city in state['cities']:
#                     if "County" in city['name']:
#                         pass
#                     else:
#                         pass
#                         # print(f"--------->{city['name']}")
# print(f"States Count: {count}")
# import pdb;pdb.set_trace()
