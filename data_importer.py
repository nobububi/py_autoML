def data_import(filenames,pd):
    data1=pd.read_csv(filenames[0])
    data2=pd.read_csv(filenames[1])
    return [data1,data2]