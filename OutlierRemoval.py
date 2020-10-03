#Importing Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys




def main():
    import sys
    total = len(sys.argv)
    if (total!=2):
        print("ERROR! WRONG NUMBER OF PARAMETERS")
        print("USAGES: $python <programName> <dataset>")
        print('EXAMPLE: $python programName.py data.csv')
        sys.exit(1)
  #  dataset=pd.read_csv(sys.argv[1]).values
    rr=outlier_removal(sys.argv[1])
    print("Number of rows removed are: ",rr)

if __name__=="__main__":
     main()
