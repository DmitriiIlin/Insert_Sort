def Conditions(array,step,start):
    # Ф-ция проверки входных данных 
    if type(array) is list and step<len(array) and step>0 and start>=0 and start<len(array) and step+start<len(array):
        return True
    else:
        return False


def InsertionSortStep(array,step=1,start=0):
    # Сортировка вставкой в массиве array, с шагом step, номер элемента i
    test=Conditions(array,step,start)
    if test==True:  
        for j in range(start+step,len(array),step):
            key=array[j]
            i=j-step
            if i<len(array) and i>=0:
                while array[i]>key and i>=0:
                    array[i+step]=array[i]

                    i-=step 
                else: 
                    array[i+step]=key
            else:
                break
        return array
    else:
        return False


"""
a=[1,6,5,4,3,2,7]
print(a)
print(InsertionSortStep(a,3,1))
"""