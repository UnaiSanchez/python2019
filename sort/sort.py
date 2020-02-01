from random import randint
num = 20
data = []
for l in range(num):
    data.append(randint(0,100))
    #data=[0,4,2]
def bubble():
    #print(data)
    operation= 0
    swamp = 0
    for i in range(len(data)):
        prev_swaps = swamp
        for k in range(len(data)-1-i):
            operation +=1
            first=data[k]
            second=data[k+1]
            #print('comparar {} con {}'.format(first,second)) asdfghjklñ
            if first > second:
                #print('intercambiar el {} con el {}'.format(first,second))
                swamp += 1
                data[k]=second
                data[k+1]=first
            #print(data)
        if prev_swaps == swamp:
            break
    print("operations:",operation)
    print("swamps:",swamp)
if __name__ == "__main__": 
    print("Sorting...") 
    bubble()
