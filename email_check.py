import sys
import pandas as pd
import numpy as np
from validate_email import validate_email

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
for email in email_list[2]:
    email_list[3] = validate_email(email) #check_mx=True

print(email_list)
