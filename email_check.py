import sys
import pandas as pd
import pymailcheck as pymailcheck
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(filename)


#create pandas dataframe from csv file
email_list = pd.read_csv(filename, header=None)
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

t = fixed_listdf.loc[fixed_listdf[4] == True] ## change
f = fixed_listdf.loc[fixed_listdf[3] == False] ## output (no change)
t.to_csv(r'incorrect.csv',header=("First Name","Last Name","Suggested Email","Current Email"), index=False,columns=(0,1,2,3))
f.to_csv(r'correct.csv',header=("First Name","Last Name","Email"), index=False,columns=(0,1,2))
