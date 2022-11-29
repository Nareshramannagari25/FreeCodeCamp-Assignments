import numpy as NP

def calculate(list):
    if len(list) !=9:
        raise ValueError("List must contain nine numbers.")
    Reshape = NP.reshape(list,(3,3))
    Dict =  {                            # Mapping the the keys with the list of arrays
                "mean"                 : [ Reshape.mean(axis=0) ,Reshape.mean(axis=1),NP.ravel(Reshape.mean())],
                "variance"             : [ Reshape.var(axis=0)  ,Reshape.var(axis=1) ,NP.ravel(Reshape.var())],
                "standard deviation"   : [ Reshape.std(axis=0)  ,Reshape.std(axis=1) ,NP.ravel(Reshape.std())],
                "max"                  : [ Reshape.max(axis=0)  ,Reshape.max(axis=1) ,NP.ravel(Reshape.max())],
                "min"                  : [ Reshape.min(axis=0)  ,Reshape.min(axis=1) ,NP.ravel(Reshape.min())],
                "sum"                  : [ Reshape.sum(axis=0)  ,Reshape.sum(axis=1) ,NP.ravel(Reshape.sum())]
                }

    Dict_2 = {}
        #looping through the keys and values of dictionary
    for k,values in Dict.items():
        List = []
        #looping through list of arrays(i.e values)
        for each_array in values:
            if each_array.size == 1:
                Type_conv = each_array.tolist()
                List.extend(Type_conv)
            else:
                Type_conv = each_array.tolist()
                List.append(Type_conv)
        
          # Adding the key-value pair to the Dictionary
        Dict_2[k] = List
    print(Dict_2)
calculate([0,1,2,3,4,5,6,7,8])