def elemental_info(data):
    print('データを表示\n')
    print(data.head())
    print('\n\nデータの基礎情報表示\n')
    print(data.describe())
    print('\n\nデータの量表示\n')
    print(data.shape)

def null_handling(data,null_line):
    nrow,ncol=data.shape
    data.isnull().sum().sort_values(ascending=False).head(10)
    newdata=data.loc[:,data.isnull().sum()<nrow*0.8]
    print('欠損許容ラインを下回るデータを削除、データ量  {}'.format(newdata.shape))
    print('{}　列削除しました'.format(data.shape[1]-newdata.shape[1]))
    return newdata

def print_type_of_data(data,pd):
    dtypes=pd.DataFrame(data.dtypes,columns=['type_of_data'])
    dtypes['count']=1
    print(dtypes.groupby(by='type_of_data').count())

def object_number_of_unique(data):
    object_data=data.loc[:,data.dtypes=='object' ]
    object_data_manykind=object_data.loc[:,object_data.nunique()>data.shape[0]/100]
    object_data_fewkind=object_data.loc[:,object_data.nunique()<=data.shape[0]/100]
    newdata=data.drop(object_data_manykind.columns,axis=1)
    newdata.drop(object_data_fewkind.columns,axis=1,inplace=True)
    print('{}　列削除しました'.format(data.shape[1]-newdata.shape[1]))
    return newdata
    

def mini_handling(data):
    data.dropna(inplace=True)
    return data

def make_data_for_analysis(data,y):
    dataX=data.loc[:,data.columns!=y]
    datay=data[y].astype(float)
    return [dataX,datay]