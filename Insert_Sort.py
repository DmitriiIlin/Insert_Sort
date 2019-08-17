def Conditions(array,step,start):
    # Ф-ция проверки входных данных 
    if type(array) is list and step<len(array) and step>0 and start>=0 and start<len(array) and step+start<len(array):
        return True
    else:
        return False


def InsertionSortStep(array,step=1,start=1):
    # Сортировка вставкой в массиве array, с шагом step, номер элемента i
    test=Conditions(array,step,start)
    if test==True:
        current=array[start]  
        j=start+step
        Flag=False
        while array[j]<current:
            Flag=True
            Target=array[j]
            if j+step<len(array):
                if array[j+step]<current:
                    j+=step
                else:
                    break
            else:
                break
        if Flag==True:
            array[j]=current
            array[start]=Target
        return array
    else:
        return False


"""
a=[8,6,5,4,3,2,1]
print(a)
print(InsertionSortStep(a,5,1))
"""