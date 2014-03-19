import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

import csv


if __name__ == "__main__":
  with open('fre-monthly-011941-022014.csv', 'rb') as csvdata:
    datareader = csv.reader(csvdata, delimiter=',')
    data = []
    for row in datareader:
      try:   
        #0:  "Date/Heure"
        #1:*  "Annee"
        #2:*  "Mois"
        #3:*  "Temp max.moy.(C)"
        #4:  "Temp max. moy. Indicateur"
        #5:*  "Temp min.moy.(C)"
        #6:  "Temp min. moy. Indicateur"
        #7:*  "Temp moy.(C)"
        #8:  "Temp moy. Indicateur"
        #9:  "Temp max.ext.(C)"
        #10: "Temp max. ext. Indicateur"
        #11: "Temp min.ext.(C)"
        #12: "Temp min. ext. Indicateur"
        #13:* "Pluie tot. (mm)"
        #14: "Pluie tot. Indicateur"
        #15:* "Neige tot. (cm)"
        #16: "Neige tot. Indicateur"
        #17:* "Precip. tot. (mm)"
        #18: "Precip. tot. Indicateur"
        #19: "Neige au sol, dernier jour (cm)"
        #20: "Neige au sol, dernier jour Indicateur"
        #21: "Dir. raf. max. (10's deg)"
        #22: "Dir. raf. max. Indicateur"
        #23: "Vit. raf. max. (km/h)"
        #24: "Vit. raf. max. Indicateur" 
        print int(row[1]), int(row[2]), float(row[3].replace(',','.')), float(row[5].replace(',','.')), float(row[7].replace(',','.')), float(row[13].replace(',','.')), float(row[15].replace(',','.')), float(row[17].replace(',','.'))
        data.add([int(row[1]), int(row[2]), float(row[3].replace(',','.')), float(row[5].replace(',','.')), float(row[7].replace(',','.')), float(row[13].replace(',','.')), float(row[15].replace(',','.')), float(row[17].replace(',','.'))])
      except:
        pass
