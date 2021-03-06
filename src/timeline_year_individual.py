#!/usr/bin/python
import sys
import util
import templates
from database_countries import code_to_country
from database_students import year_grouped as s_db_y
from database_timeline import year_indexed as t_db_y
from database_timeline import previous_year
from database_timeline import next_year

def run(year):
    print "Creating timeline/" + year + "/individual"
    html = templates.get("timeline/year/individual")
    html = templates.initial_replace(html, 1)
    yeardata = t_db_y[year]
    html = html.replace("__YEAR__", year)
    html = html.replace("__NUMBER__", yeardata["number"])
    html = html.replace("__ORDINAL__", util.ordinal(yeardata["number"]))
    
    if year in previous_year:
        html = html.replace("__PREVIOUS_YEAR__", previous_year[year])
        html = html.replace("__PREVIOUS_YEAR_STYLE__", "")
    else:
        html = html.replace("__PREVIOUS_YEAR_STYLE__", "display: none;")
        
    if year in next_year:
        html = html.replace("__NEXT_YEAR__", next_year[year])
        html = html.replace("__NEXT_YEAR_STYLE__", "")
    else:
        html = html.replace("__NEXT_YEAR_STYLE__", "display: none;")
    
    tablehtml = ""
    if year in s_db_y:
        for row in s_db_y[year]:
            rowhtml = templates.get("timeline/year/individual_row")
            rowhtml = rowhtml.replace("__NAME__", row["name"])
            rowhtml = rowhtml.replace("__CODE__", row["code"])
            rowhtml = rowhtml.replace("__COUNTRY__", code_to_country[row["code"]])
            rowhtml = rowhtml.replace("__RANK__", row["rank"])
            if row["medal"] == "1":
                rowhtml = rowhtml.replace("__MEDAL__", templates.get("timeline/year/individual_gold"))
            elif row["medal"] == "2":
                rowhtml = rowhtml.replace("__MEDAL__", templates.get("timeline/year/individual_silver"))
            elif row["medal"] == "3":
                rowhtml = rowhtml.replace("__MEDAL__", templates.get("timeline/year/individual_bronze"))
            elif row["medal"] == "4":
                rowhtml = rowhtml.replace("__MEDAL__", templates.get("timeline/year/individual_honourable"))
            else:
                rowhtml = rowhtml.replace("__MEDAL__", "")
            tablehtml += rowhtml
    html = html.replace("__TABLE__", tablehtml)
    
    html = templates.final_replace(html, "../..")
    util.writefile("../timeline/" + year + "/individual.html", html)
    
if __name__ == "__main__":
    run(sys.argv[1])