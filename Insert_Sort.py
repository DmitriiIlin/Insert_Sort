def Conditions(array,step,start):
    # Ф-ция проверки входных данных 
    if type(array) is list and step<len(array) and step>0 and start>=0 and start<len(array) and step+start<len(array):
        return True
    else:
        return False

def KnuthSequence(array_size):
    #Ф-ция вычесляет интервальную последовательность целых чисел
    Numbers=[]
    Knuth_Numbers=[]
    number=1
    if array_size>0:
        Numbers.append(number)
        while array_size>=number:
            number=3*number+1
            if number>=array_size:
                break
            else:
                Numbers.append(number)
        Numbers_size=len(Numbers)
        while Numbers_size>0:
            Knuth_Numbers.append(Numbers[Numbers_size-1])
            Numbers_size-=1
        return Knuth_Numbers
    elif array_size==0:
        return [1]
    else:
        return []


def ShellSort(array):
    #Сортировка массива методом Шелла
    if len(array)>1:
        Knuth_numbers=KnuthSequence(len(array))
        for i in range(0,len(Knuth_numbers)):
            array=InsertionSortStep(array,Knuth_numbers[i],i)
        return array
    else:
        return array


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
a=[1,6,5,4,3,2,7,67,44,23,567,12,45,67]
print(ShellSort(a))

print(KnuthSequence(5))
"""