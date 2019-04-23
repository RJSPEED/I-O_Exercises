"""APPROACH:
1. Read CSV file into memory
2. Filter data to Tm = DET
3. Perform required calcs and store values into dict
4. Output via new CSV
"""
import csv

with open('NHL_2018.csv', 'r') as file_object:
    key_list = ["Name", "Games Played", "Points", "Blocks", "Hits"]
    dict_rows = []
        
    for line in file_object:
        x = line.split(",")
        #Filter for team = Detroit.
        if x[3] == "DET":
            """Format name colunn to remove all chars from \ onwards."""
            name_backslash_str_pos = (x[1].find("\\"))
            
            """Calc TOI time give in mins:secs as a % of 60 mins."""
            time_colon_pos = (x[22].find(":"))
            seconds_played = (int(x[22][:time_colon_pos])*60)+(int(x[22][time_colon_pos+1:]))
            game_percentage = round(seconds_played / 36,2)
            
            """Calc theoretical stats assuming everyone plated a full season
               ie. 82 games"""
            pts = int(x[8])*82
            blks = int(x[23])*82
            hits = int(x[24])*82
            
            """Extrapolate above stats based on % of game played, eg. if played 10% 
               of game * 10 ie. (100/10), if 25% then * 4 ie. (100/25)."""
            pts = int(pts * (100/game_percentage))
            blks = int(blks * (100/game_percentage))
            hits = int(hits * (100/game_percentage))

            """Append all the above into dictionary."""
            dict_rows.append({"Name": x[1][:name_backslash_str_pos], "Games Played": int(x[5]),
                              "Points": pts, "Blocks": blks, "Hits": hits})

"""Output to csv file."""
with open('nhl18.csv', 'w') as file_object:
    writer = csv.DictWriter(file_object, key_list, quoting=csv.QUOTE_NONNUMERIC)
    writer.writeheader()
    for row in dict_rows:
        writer.writerow(row)
    
