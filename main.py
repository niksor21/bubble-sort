arr = [-2, 45, 0, 11, -9]

print("Начальный массив: ")
print(arr)

i = len(arr)-1
while i > 0:
    j = 0
    while j < len(arr)-1:
        if arr[j] > arr[j+1]:
            tmp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = tmp
        j+=1

    print("Шаг " + str(len(arr)-i) + ": ")
    print(arr)

    i-=1

print("Конечный массив: ")
print(arr)
