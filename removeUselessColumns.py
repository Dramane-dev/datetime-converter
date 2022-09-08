def remove_useless_columns(dt):
    newDataFrame = dt
    for i in range(len(dt.columns)):
        if (not(dt.columns[i].lower().startswith("date d'inclusion") | 
            dt.columns[i].lower().startswith("date de naissance") | 
            dt.columns[i].lower().startswith("date de facturation"))
        ):
            newDataFrame = dt.drop(columns=dt.columns[i])
    return newDataFrame