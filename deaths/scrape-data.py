from wikitables import import_tables
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
tables = import_tables('List_of_people_who_died_climbing_Mount_Everest','en')
t=tables[0].json()
with open('everest-deaths.txt', 'w') as outfile:
    json.dump(t, outfile)
