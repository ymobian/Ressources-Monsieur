import pandas
iden=pandas.read_csv("ident_virgule.csv",encoding = "ISO-8859-1")
info=iden.loc[[0,1],['nom','date_naissance']]

