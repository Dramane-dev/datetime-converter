import pandas as pd
from removeUselessColumns import remove_useless_columns

sheets = pd.ExcelFile("Patients.xlsx").sheet_names

for i in range(len(sheets)):
    sheet = sheets[i]
    if (sheet.lower().startswith("inclusion")):
        dt = pd.read_excel("./Patients.xlsx", sheet_name=sheet)

        dt = remove_useless_columns(dt)

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

        dt.to_excel("dates_converted_" + sheet + ".xlsx", sheet_name="Dates")