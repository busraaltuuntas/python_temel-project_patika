def flatten(x):
    for i in x:
        if isinstance(i,list):
            flatten(i)
        else:
            new_list.append(i)

x=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
new_list =[]
flatten(x)
print(new_list)


