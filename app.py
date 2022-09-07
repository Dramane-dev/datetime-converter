import pandas as pd

# dt = pd.read_excel("./input/dates.xlsx", sheet_name="Dates")
# print(dt["Date1"])
# print(pd.to_datetime("25/07/2022", format="%d/%m/%Y", errors="ignore").strftime("%d/%m/%Y"))
# dt["Date2"] = pd.to_datetime(dt["Date2"], format="%d/%m/%Y", errors="ignore")
# # dt["Date2"] = dt["Date2"].dt.strftime("%d/%m/%Y")
# dt["Date2"] = dt["Date2"].dt.date
# dt.to_excel("dates_converted.xlsx", sheet_name="Dates")

dt = pd.read_excel("./input/Patients.xlsx", sheet_name="Inclusions 1")
# print(dt["Date d'inclusion"])
# print(pd.to_datetime("25/07/2022", format="%d/%m/%Y", errors="ignore").strftime("%d/%m/%Y"))
# try:
#     dt["Date d'inclusion"] = pd.to_datetime(dt["Date d'inclusion"], format="%d/%m/%Y", errors="raise")
#     dt["Date d'inclusion"] = dt["Date d'inclusion"].dt.date
# except:
#     dt["Date d'inclusion"] = pd.to_datetime(dt["Date d'inclusion"], format="%Y/%m/%d", errors="raise")
#     dt["Date d'inclusion"] = dt["Date d'inclusion"].dt.date
    
dt["Date d'inclusion"] = pd.to_datetime(dt["Date d'inclusion"], format="%d/%m/%Y", errors="coerce")
dt["Date d'inclusion"] = dt["Date d'inclusion"].dt.date
dt["Date de naissance"] = pd.to_datetime(dt["Date de naissance"], format="%d/%m/%Y", errors="coerce")
dt["Date de naissance"] = dt["Date de naissance"].dt.date
dt["Date de facturation THEORIQUE ST 1"] = pd.to_datetime(dt["Date de facturation THEORIQUE ST 1"], format="%d/%m/%Y", errors="coerce")
dt["Date de facturation THEORIQUE ST 1"] = dt["Date de facturation THEORIQUE ST 1"].dt.date
dt["Date de facturation ST 2 (calculée sur l'envoi de la série)"] = pd.to_datetime(dt["Date de facturation ST 2 (calculée sur l'envoi de la série)"], format="%d/%m/%Y", errors="coerce")
dt["Date de facturation ST 2 (calculée sur l'envoi de la série)"] = dt["Date de facturation ST 2 (calculée sur l'envoi de la série)"].dt.date
dt["Date de facturation ST3 (calculée sur l'envoi de la série)"] = pd.to_datetime(dt["Date de facturation ST3 (calculée sur l'envoi de la série)"], format="%d/%m/%Y", errors="coerce")
dt["Date de facturation ST3 (calculée sur l'envoi de la série)"] = dt["Date de facturation ST3 (calculée sur l'envoi de la série)"].dt.date
dt["Date de facturation AT (calculée sur l'envoi de la série)"] = pd.to_datetime(dt["Date de facturation AT (calculée sur l'envoi de la série)"], format="%d/%m/%Y", errors="coerce")
dt["Date de facturation AT (calculée sur l'envoi de la série)"] = dt["Date de facturation AT (calculée sur l'envoi de la série)"].dt.date
# dt["Date2"] = dt["Date2"].dt.strftime("%d/%m/%Y")
# dt["Date2"] = dt["Date2"].dt.date
dt.to_excel("dates_converted.xlsx", sheet_name="Dates")