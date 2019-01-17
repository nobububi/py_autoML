def analysis_for_importance(dataX,datay,RandomForestRegressor,pd,main_feature_num):
    rf = RandomForestRegressor()
    rf.fit(dataX, datay)
    data_importances=pd.DataFrame(rf.feature_importances_,
                               index=dataX.columns,
                              columns=['importances'])
    data_importances.sort_values(by='importances',ascending=False,inplace=True)
    data_importances=data_importances.iloc[:main_feature_num,:]
    print(data_importances.head(10))
    main_data=dataX.loc[:,data_importances.index]
    return main_data
