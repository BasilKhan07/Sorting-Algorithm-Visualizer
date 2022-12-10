from tkinter import *
from tkinter import simpledialog
from tkinter import ttk, messagebox 
from ttkbootstrap import *
import numpy as np 
import time 
import random
from color import getColor


fptr = open("ArrayNumbers.txt", "w" )
for i in range(100):
    line = str(random.randint(10, 390))
    fptr.write(line)
    fptr.write(" ")
fptr.write('\n')
fptr.close()

fptr = open("ArrayNumbers.txt", "r" )
array = []
array = list(map(int, fptr.read().split()))
fptr.close()
speed = 100
N = len(array)


def insertionSort():
    for j in range(1, N): 
            key = array[j] 
            i = j-1
            ShowBars(N, array, ['yellow' if a == i or a == i +
                               1 else 'green' if a <= j 
                               else'cyan' for a in range(N)]) 
            time.sleep(1/speed) 
            while i >= 0 and array[i] > key: 
                array[i+1] = array[i] 
                ShowBars(N, array, ['pink' if a == i else 'green' if a <= j  else'cyan' for a in range(N)]) 
                time.sleep(1/speed) 
                i -= 1
            array[i+1] = key

def bubbleSort():
    for i in range(N):
            time.sleep(1/speed) 
            for j in range(0, N-i-1):
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
                    ShowBars(N, array, ['pink' if a == i else 'green' if a <= j  else'cyan' for a in range(N)])

def mergeSort(left, right):
    if left < right:
        mid = (left+right)//2
        mergeSort(left, mid)
        mergeSort(mid+1, right)
        j = mid+1
        if array[mid] <= array[mid+1]:
            return
        while left <= mid and j <= right:
            ShowBars(N, array, ['red' if x == left or x == j else 'pink' for x in range(N)])
            time.sleep(1/speed)
            if array[left] <= array[j]:
                left += 1
            else:
                ShowBars(N, array, ['cyan' if x == left or x == j else 'pink' for x in range(N)])
                time.sleep(1/speed)
                temp = array[j]
                i = j
                while i != left:
                    array[i] = array[i-1]
                    ShowBars(N, array, ['cyan' if x == i or x == j else 'pink' for x in range(N)])
                    time.sleep(1/speed)
                    i -= 1       
                array[left] = temp
                ShowBars(N, array, ['green' if x == left or x == j else 'pink' for x in range(N)])
                time.sleep(1/speed)
                left += 1
                mid += 1
                j += 1

def heapify(n, index):
    ShowBars(n, array, ['cyan' if x==index else 'pink' for x in range(n)])
    time.sleep(1/speed) 
    largest = index
    left = 2*index+1
    right = 2*index+2
    if left < n and array[index] < array[left]:
        largest = left
    if right < n and array[largest] < array[right]:
        largest = right
    if largest != index:
        array[index], array[largest] = array[largest], array[index]
        heapify(n, largest)

def heapSort():
    for i in range(N//2, -1, -1):
        heapify(N, i)
    for i in range(N-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(i, 0)
        ShowBars(N, array, ['green' if x > i else 'cyan' if x==i else 'pink' for x in range(N)])
        time.sleep(1/speed) 

def partition(head, tail):
    index = head
    pivot = array[tail] 
    ShowBars(N, array, getColor(N, head, tail, index, index))
    time.sleep(1/speed)
    for j in range(head, tail):
        if array[j] < pivot:
            ShowBars(N, array, getColor(N, head, tail, index, j, True))
            time.sleep(1/speed)
            array[index], array[j] = array[j], array[index]
            index += 1
        ShowBars(N, array, getColor(N, head, tail, index, j))
        time.sleep(1/speed)
    ShowBars(N, array, getColor(N, head, tail, index, tail, True))
    time.sleep(1/speed)
    array[index], array[tail] = array[tail], array[index]
    return index

def quickSort(head, tail):
    if head < tail:
        partition1 = partition(head, tail)
        quickSort(head, partition1-1)
        quickSort(partition1+1, tail)   

def countingSortForRadix(exp):
    output = [0] * (N)
    count = [0] * (10)
    for i in range(0, N):
        index = (array[i]/exp)
        count[int((index)%10)] += 1
    for i in range(1,10):
        count[i] += count[i-1]
    i = N-1
    while i>=0:
        index = (array[i]/exp)
        output[ count[ int((index)%10) ] - 1] = array[i]
        count[int((index)%10)] -= 1
        i -= 1
        ShowBars(N, array, ['green' if index > i else 'cyan' if index==i else 'pink' for index in range(N)])
    i = 0
    for i in range(0,len(array)):
        array[i] = output[i]
        ShowBars(N, array, ['green' if x == i else ['cyan'] for x in range(N)])
        time.sleep(1/speed)

def radixSort():
    maximum = max(array)
    exponent = 1
    while maximum/exponent > 0:
        countingSortForRadix(exponent)
        exponent *= 10

def bucketSort():
    largest = max(array)
    size = largest/N
    buckets = [[] for i in range(N)]  
    for i in range(N):
        index = int(array[i]/size)
        if index != N:
            buckets[index].append(array[i])
            ShowBars(N, array, ['green' if index > i else 'cyan' if index==i else 'pink' for index in range(N)])
            time.sleep(1/speed)
        else:
            buckets[N - 1].append(array[i])
            ShowBars(N, array, ['green' if index > i else 'cyan' if index==i else 'pink' for index in range(N)])
            time.sleep(1/speed)
    for i in range(N):
        buckets[i] = sorted(buckets[i])
        ShowBars(N, array, ['cyan' if x==i else 'pink' for x in range(N)])
        time.sleep(1/speed)
        result = []
    for i in range(N):
        result = result + buckets[i]
        time.sleep(1/speed)
    return result

def countingSort():
    maximum = 0
    for i in range(N):
        ShowBars(N, array, ['green' if x == i else ['cyan'] for x in range(N)])
        time.sleep(1/speed)
        if array[i] > maximum:
            maximum = array[i]
    buckets = [0 for i in range(maximum + 1)]
    for i in array:
        buckets[i] += 1
    i = 0
    for j in range(maximum + 1):
        for _ in range(buckets[j]):
            array[i] = j
            i += 1
            ShowBars(N, array, ['green' if index > i else 'cyan' if index==i else 'pink' for index in range(N)])
            time.sleep(1/speed)

def insertionSortForAlgo7_4_5(l, n):
    for i in range(l + 1, n + 1):
        val = array[i]
        j = i
        ShowBars(N, array, ['yellow' if a == i or a == i +
                               1 else 'green' if a <= j 
                               else'cyan' for a in range(N)])
        time.sleep(1/speed) 
        while j>l and array[j-1]>val:
            array[j]= array[j-1]
            ShowBars(N, array, ['pink' if a == i else 'green' if a <= j  else'cyan' for a in range(N)]) 
            time.sleep(1/speed) 
            j-= 1
        array[j]= val

def partioningForAlgo7_4_5(low, high):
    p = array[high]
    i = j = low
    ShowBars(N, array, getColor(N, low, high, i, j))
    time.sleep(1/speed)
    for i in range(low, high):
        if array[i]<p:
            ShowBars(N, array, getColor(N, low, high, j, i, True))
            time.sleep(1/speed)
            array[i], array[j]= array[j], array[i]
            j+= 1
        ShowBars(N, array, getColor(N, low, high, j, i))
        time.sleep(1/speed)
    ShowBars(N, array, getColor(N, low, high, i, high, True))
    time.sleep(1/speed)
    array[j], array[high]= array[high], array[j]
    return j

def _Algo7_4_5(low, high):
    while low < high:
        if high-1 + 1<10:
            insertionSortForAlgo7_4_5(low, high)
            break
        else:
            partitioning = partioningForAlgo7_4_5(low, high)
            if partitioning - 1 < high - partitioning:
                _Algo7_4_5(low, partitioning-1)
                low = partitioning + 1
            else:
                _Algo7_4_5(partitioning + 1, high)
                high = partitioning - 1

def _Algo8_2_4():
    maximum = max(array)
    output = [0] * N
    count = [0] * (maximum+1)
    a = simpledialog.askinteger("Input", "Enter value of a", parent=root, minvalue=1, maxvalue=max(array))
    b = simpledialog.askinteger("Input", "Enter value of b", parent=root, minvalue=1, maxvalue=max(array))
    begin = time.time()
    for i in range(0, N):
        count[array[i]] += 1
    for i in range(1, maximum+1):
        count[i] += count[i - 1]
    c=count[b]-count[a-1]
    i = N - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1
        ShowBars(N, array, ['green' if index > i else 'cyan' if index==i else 'pink' for index in range(N)])
        time.sleep(1/speed)
    for i in range(0, N):
        array[i] = output[i]
        ShowBars(N, array, ['green' if x == i else ['cyan'] for x in range(N)])
        time.sleep(1/speed)
    end = time.time()
    return c, end - begin

def ShowBars(n, array, color): 
    __canvas.delete('all') 
    width = 1560/(3*n-1) 
    gap = width/2
    for i in range(n): 
        __canvas.create_rectangle(7+i*width+i*gap, 0, 7 + (i+1)*width+i*gap, array[i], fill=color[i]) 
    root.update_idletasks() 

def shuffle(): 
    np.random.shuffle(array) 
    ShowBars(N, array, colors) 

def start():
    if algorithms['insertion'] == True:
        begin = time.time()
        insertionSort()
        end = time.time()
        ShowBars(N, array, ['yellow' for _ in range(N)])
        messagebox.showinfo("Time Taken: ", str(round(end - begin, 8)) + " seconds")
    elif algorithms['bubble'] == True:
        begin = time.time()
        bubbleSort()
        end = time.time()
        ShowBars(N, array, ['yellow' for _ in range(N)]) 
        messagebox.showinfo("Time Taken: ", str(round(end - begin, 5)) + "seconds")
    elif algorithms['merge'] == True:
        begin = time.time()
        mergeSort(0, N - 1)
        end = time.time()
        ShowBars(N, array, ['yellow' for _ in range(N)]) 
        messagebox.showinfo("Time Taken: ", str(round(end - begin, 8)) + "seconds")
    elif algorithms['heap'] == True:
        begin = time.time()
        heapSort()
        end = time.time()
        ShowBars(N, array, ['yellow' for _ in range(N)]) 
        messagebox.showinfo("Time Taken: ", str(round(end - begin, 8)) + "seconds")
    elif algorithms['quick'] == True:
        begin = time.time()    
        quickSort(0, N-1)
        end = time.time()
        ShowBars(N, array, ['yellow' for _ in range(N)]) 
        messagebox.showinfo("Time Taken: ", str(round(end - begin, 8)) + "seconds")
    elif algorithms['radix'] == True:
        begin = time.time()   
        radixSort()
        end = time.time()
        ShowBars(N, array, ['yellow' for _ in range(N)]) 
        messagebox.showinfo("Time Taken: ", str(round(end - begin, 8)) + "seconds")
    elif algorithms['bucket'] == True:
        begin = time.time() 
        ShowBars(N, bucketSort(), ['yellow' for x in range(N)])
        end = time.time()
        messagebox.showinfo("Time Taken: ", str(round(end - begin, 8)) + "seconds")
    elif algorithms['counting'] == True:
        begin = time.time() 
        countingSort()
        end = time.time()
        ShowBars(N, array, ['yellow' for x in range(N)])
        messagebox.showinfo("Time Taken: ", str(round(end - begin, 8)) + "seconds")
    elif algorithms['Algo7_4_5'] == True:
        begin = time.time() 
        _Algo7_4_5(0, N-1)
        end = time.time()
        ShowBars(N, array, ['yellow' for x in range(N)])
        messagebox.showinfo("Time Taken: ", str(round(end - begin, 8)) + "seconds")
    elif algorithms['Algo8_2_4'] == True:
        begin = time.time() 
        answer, timeTaken= _Algo8_2_4()
        ShowBars(N, array, ['yellow' for x in range(N)])
        messagebox.showinfo("Time Taken ", str(round(timeTaken, 8)) + " seconds ")
        messagebox.showinfo("Result ", "Value of c : " + str(answer))
    else: 
        messagebox.showerror("Algorithm Visualizer", "You need to select a sorting algorithm")

def bubble(): 
    if algorithms['bubble'] is False: 
        algorithms['bubble'] = True
        bubbleButton.config(style='success.TButton') 
        algorithms['insertion'] = False
        insertionButton.config(style='danger.TButton')
        algorithms['merge'] = False
        mergeButton.config(style='danger.TButton')
        algorithms['heap'] = False
        heapButton.config(style='danger.TButton')
        algorithms['quick'] = False
        quickButton.config(style='danger.TButton')
        algorithms['radix'] = False
        radixButton.config(style='danger.TButton')
        algorithms['bucket'] = False
        bucketButton.config(style='danger.TButton')
        algorithms['counting'] = False
        countingButton.config(style='danger.TButton')
        algorithms['Algo7_4_5'] = False
        button7_4_5.config(style='danger.TButton')
        algorithms['Algo8_2_4'] = False
        button8_2_4.config(style='danger.TButton') 
    else: 
        algorithms['bubble'] = False
        bubbleButton.config(style='danger.TButton') 

def insertion(): 
    if algorithms['insertion'] is False: 
        algorithms['insertion'] = True
        insertionButton.config(style='success.TButton') 
        algorithms['bubble'] = False
        bubbleButton.config(style='danger.TButton')
        algorithms['merge'] = False
        mergeButton.config(style='danger.TButton')
        algorithms['heap'] = False
        heapButton.config(style='danger.TButton')
        algorithms['quick'] = False
        quickButton.config(style='danger.TButton')
        algorithms['radix'] = False
        radixButton.config(style='danger.TButton')
        algorithms['bucket'] = False
        bucketButton.config(style='danger.TButton')
        algorithms['counting'] = False
        countingButton.config(style='danger.TButton')
        algorithms['Algo7_4_5'] = False
        button7_4_5.config(style='danger.TButton')
        algorithms['Algo8_2_4'] = False
        button8_2_4.config(style='danger.TButton')
    else: 
        algorithms['insertion'] = False
        insertionButton.config(style='danger.TButton')

def merge(): 
    if algorithms['merge'] is False: 
        algorithms['merge'] = True
        mergeButton.config(style='success.TButton') 
        algorithms['bubble'] = False
        bubbleButton.config(style='danger.TButton')
        algorithms['insertion'] = False
        insertionButton.config(style='danger.TButton')
        algorithms['heap'] = False
        heapButton.config(style='danger.TButton')
        algorithms['quick'] = False
        quickButton.config(style='danger.TButton')
        algorithms['radix'] = False
        radixButton.config(style='danger.TButton')
        algorithms['bucket'] = False
        bucketButton.config(style='danger.TButton')
        algorithms['counting'] = False
        countingButton.config(style='danger.TButton')
        algorithms['Algo7_4_5'] = False
        button7_4_5.config(style='danger.TButton')
        algorithms['Algo8_2_4'] = False
        button8_2_4.config(style='danger.TButton')
    else: 
        algorithms['merge'] = False
        mergeButton.config(style='danger.TButton')  

def heap(): 
    if algorithms['heap'] is False: 
        algorithms['heap'] = True
        heapButton.config(style='success.TButton') 
        algorithms['bubble'] = False
        bubbleButton.config(style='danger.TButton')
        algorithms['merge'] = False
        mergeButton.config(style='danger.TButton')
        algorithms['insertion'] = False
        insertionButton.config(style='danger.TButton')
        algorithms['quick'] = False
        quickButton.config(style='danger.TButton')
        algorithms['radix'] = False
        radixButton.config(style='danger.TButton')
        algorithms['bucket'] = False
        bucketButton.config(style='danger.TButton')
        algorithms['counting'] = False
        countingButton.config(style='danger.TButton')
        algorithms['Algo7_4_5'] = False
        button7_4_5.config(style='danger.TButton')
        algorithms['Algo8_2_4'] = False
        button8_2_4.config(style='danger.TButton')
    else: 
        algorithms['heap'] = False
        heapButton.config(style='danger.TButton')

def quick(): 
    if algorithms['quick'] is False: 
        algorithms['quick'] = True
        quickButton.config(style='success.TButton') 
        algorithms['bubble'] = False
        bubbleButton.config(style='danger.TButton')
        algorithms['merge'] = False
        mergeButton.config(style='danger.TButton')
        algorithms['heap'] = False
        heapButton.config(style='danger.TButton')
        algorithms['insertion'] = False
        insertionButton.config(style='danger.TButton')
        algorithms['radix'] = False
        radixButton.config(style='danger.TButton')
        algorithms['bucket'] = False
        bucketButton.config(style='danger.TButton')
        algorithms['counting'] = False
        countingButton.config(style='danger.TButton')
        algorithms['Algo7_4_5'] = False
        button7_4_5.config(style='danger.TButton')
        algorithms['Algo8_2_4'] = False
        button8_2_4.config(style='danger.TButton')
    else: 
        algorithms['quick'] = False
        quickButton.config(style='danger.TButton')

def radix(): 
    if algorithms['radix'] is False: 
        algorithms['radix'] = True
        radixButton.config(style='success.TButton') 
        algorithms['bubble'] = False
        bubbleButton.config(style='danger.TButton')
        algorithms['merge'] = False
        mergeButton.config(style='danger.TButton')
        algorithms['heap'] = False
        heapButton.config(style='danger.TButton')
        algorithms['quick'] = False
        quickButton.config(style='danger.TButton')
        algorithms['insertion'] = False
        insertionButton.config(style='danger.TButton')
        algorithms['bucket'] = False
        bucketButton.config(style='danger.TButton')
        algorithms['counting'] = False
        countingButton.config(style='danger.TButton')
        algorithms['Algo7_4_5'] = False
        button7_4_5.config(style='danger.TButton')
        algorithms['Algo8_2_4'] = False
        button8_2_4.config(style='danger.TButton')
    else: 
        algorithms['radix'] = False
        radixButton.config(style='danger.TButton')

def bucket(): 
    if algorithms['bucket'] is False: 
        algorithms['bucket'] = True
        bucketButton.config(style='success.TButton') 
        algorithms['bubble'] = False
        bubbleButton.config(style='danger.TButton')
        algorithms['merge'] = False
        mergeButton.config(style='danger.TButton')
        algorithms['heap'] = False
        heapButton.config(style='danger.TButton')
        algorithms['quick'] = False
        quickButton.config(style='danger.TButton')
        algorithms['radix'] = False
        radixButton.config(style='danger.TButton')
        algorithms['insertion'] = False
        insertionButton.config(style='danger.TButton')
        algorithms['counting'] = False
        countingButton.config(style='danger.TButton')
        algorithms['Algo7_4_5'] = False
        button7_4_5.config(style='danger.TButton')
        algorithms['Algo8_2_4'] = False
        button8_2_4.config(style='danger.TButton')
    else: 
        algorithms['bucket'] = False
        bucketButton.config(style='danger.TButton')

def counting(): 
    if algorithms['counting'] is False: 
        algorithms['counting'] = True
        countingButton.config(style='success.TButton') 
        algorithms['bubble'] = False
        bubbleButton.config(style='danger.TButton')
        algorithms['merge'] = False
        mergeButton.config(style='danger.TButton')
        algorithms['heap'] = False
        heapButton.config(style='danger.TButton')
        algorithms['quick'] = False
        quickButton.config(style='danger.TButton')
        algorithms['radix'] = False
        radixButton.config(style='danger.TButton')
        algorithms['bucket'] = False
        bucketButton.config(style='danger.TButton')
        algorithms['insertion'] = False
        insertionButton.config(style='danger.TButton')
        algorithms['Algo7_4_5'] = False
        button7_4_5.config(style='danger.TButton')
        algorithms['Algo8_2_4'] = False
        button8_2_4.config(style='danger.TButton')
    else: 
        algorithms['countiing'] = False
        countingButton.config(style='danger.TButton')

def Algo7_4_5(): 
    if algorithms['Algo7_4_5'] is False: 
        algorithms['Algo7_4_5'] = True
        button7_4_5.config(style='success.TButton') 
        algorithms['bubble'] = False
        bubbleButton.config(style='danger.TButton')
        algorithms['merge'] = False
        mergeButton.config(style='danger.TButton')
        algorithms['heap'] = False
        heapButton.config(style='danger.TButton')
        algorithms['quick'] = False
        quickButton.config(style='danger.TButton')
        algorithms['radix'] = False
        radixButton.config(style='danger.TButton')
        algorithms['bucket'] = False
        bucketButton.config(style='danger.TButton')
        algorithms['insertion'] = False
        insertionButton.config(style='danger.TButton')
        algorithms['counting'] = False
        countingButton.config(style='danger.TButton')
        algorithms['Algo8_2_4'] = False
        button8_2_4.config(style='danger.TButton')
    else: 
        algorithms['Algo7_4_5'] = False
        button7_4_5.config(style='danger.TButton')

def Algo8_2_4(): 
    if algorithms['Algo8_2_4'] is False: 
        algorithms['Algo8_2_4'] = True
        button8_2_4.config(style='success.TButton') 
        algorithms['bubble'] = False
        bubbleButton.config(style='danger.TButton')
        algorithms['merge'] = False
        mergeButton.config(style='danger.TButton')
        algorithms['heap'] = False
        heapButton.config(style='danger.TButton')
        algorithms['quick'] = False
        quickButton.config(style='danger.TButton')
        algorithms['radix'] = False
        radixButton.config(style='danger.TButton')
        algorithms['bucket'] = False
        bucketButton.config(style='danger.TButton')
        algorithms['insertion'] = False
        insertionButton.config(style='danger.TButton')
        algorithms['counting'] = False
        countingButton.config(style='danger.TButton')
        algorithms['Algo7_4_5'] = False
        button7_4_5.config(style='danger.TButton')
    else: 
        algorithms['Algo8_2_4'] = False
        button8_2_4.config(style='danger.TButton')


if __name__ == '__main__': 
    root = Style(theme='superhero').master 
    algorithms = {'insertion': False, 'bubble': False, 'merge': False, 'heap': False, 'quick': False, 'radix': False, 'bucket':False, 'counting': False, 'Algo7_4_5':False, 'Algo8_2_4':False} 
    root.title('Sorting Algorithms') 
    root.resizable(True, True) 
    Label(root, text='Select which Sorting to apply on Array').grid(row=0,column=0, columnspan=8) 
    insertionButton = ttk.Button(root, text='Insertion sort', width=14, padding=1, command=insertion) 
    insertionButton.grid(row=1, column=0, padx= 1,  pady=8) 
    bubbleButton = ttk.Button(root, text='Bubble sort', width=14, padding=1, command=bubble) 
    bubbleButton.grid(row=1, column=1, padx= 1, pady=8)
    mergeButton = ttk.Button(root, text='Merge sort', width=14, padding=1, command=merge) 
    mergeButton.grid(row=1, column=2, padx= 1,pady=8) 
    heapButton = ttk.Button(root, text='Heap sort', width=14, padding=1, command=heap) 
    heapButton.grid(row=1, column=3, padx= 1,pady=8)
    quickButton = ttk.Button(root, text='Quick sort', width=14, padding=1, command=quick) 
    quickButton.grid(row=1, column=4, padx= 1,pady=8)  
    radixButton = ttk.Button(root, text='Radix sort', width=14, padding=1, command=radix) 
    radixButton.grid(row=1, column=5,padx= 1, pady=8)
    bucketButton = ttk.Button(root, text='Bucket sort', width=14, padding=1, command=bucket) 
    bucketButton.grid(row=1, column=6, padx= 1,pady=8)
    countingButton = ttk.Button(root, text='Counting sort', width=14, padding=1, command=counting) 
    countingButton.grid(row=1, column=7,padx= 1, pady=8)
    button7_4_5 = ttk.Button(root, text='Algo7_4_5', width=14, padding=1, command=Algo7_4_5) 
    button7_4_5.grid(row=2, column=0, padx= 1,pady=8)
    button8_2_4 = ttk.Button(root, text='Algo8_2_4', width=14, padding=1, command=Algo8_2_4) 
    button8_2_4.grid(row=2, column=1, padx= 1,pady=8)
    startButton = ttk.Button(root, text='Start', width=14, padding=5, command=start)  
    startButton.grid(row=3, column=3, padx= 10,pady=8)
    shuffleButton = ttk.Button(root, text='Shuffle Array', width=14, padding=5, command=shuffle) 
    shuffleButton.grid(row=3, column=4,padx= 10, pady=8)
    colors = ['white' for _ in range(N)] 
    __canvas = Canvas(root, width=1000, height=500) 
    __canvas.grid(row=4, column=0, columnspan=8) 
    shuffle() 
    ShowBars(N, array, colors)
    root.mainloop() 