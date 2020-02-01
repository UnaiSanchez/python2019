def main():
    with open("data_nums_1000000.txt","r") as file:
        numbers = list(map(int,file.read().splitlines()))
   #print(type(numbers))
   #print(len(numbers))
   #print(type(numbers[0]))
    print(linear_search(numbers,666666))
def linear_search(data,needle):
    for index, num in enumerate(data):
        if n == needle:
            return
def binary_search(data,needle):
    sorted_data = sorted(data)
    left_index=0
    right_index = len(sorted_data)
    while Ture:
        middle_index = int((left_index+right_index)/2)
        num = sorted_data[middle_index]
        if num > needle:
            right_index= middle_index
        elif:
            left_index = middle_index
        else:
            return middle_index
main()