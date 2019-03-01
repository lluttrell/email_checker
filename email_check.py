import sys
import pandas as pd
import pymailcheck as pymailcheck

# open file from command line arguments
try:
    csvfile = open(sys.argv[1], newline='')
except IndexError as error:
    print(error)
    print("Email checker requires an input file")
    sys.exit()
except FileNotFoundError as error:
    print(error)
    print("File not found")
    sys.exit()

#create pandas dataframe from csv file
email_list = pd.read_csv(csvfile, header=None)
fixed_list = list()
fname = 0
lname = 1
email = 2
changed = 3
accepted_declines = {'declined','delcined','decline','declind','declin'}

for index,row in email_list.iterrows():
    suggestion = pymailcheck.suggest(row[email])

    ## if we want to replace all the emails
    ## with the fixed versions without checking
    if row[email].lower() in accepted_declines:
        continue
    elif (suggestion):
        fixed_email = suggestion['full']
        fixed_full = row[fname],row[lname],fixed_email,row[email],True
        row[email] = fixed_email
        fixed_list.append(fixed_full)
    else:
        fixed_full = row[fname],row[lname],row[email],False
        fixed_list.append(fixed_full)

fixed_listdf = pd.DataFrame(fixed_list)

t = fixed_listdf.loc[fixed_listdf[4] == True]
f = fixed_listdf.loc[fixed_listdf[3] == False]
t.to_csv(r'change.csv',header=False, index=False,columns=(0,1,2,3))
f.to_csv(r'output.csv',header=False, index=False,columns=(0,1,2))
