import sys
f = open(sys.argv[1],'r')
arr = f.readlines()
f.close()
print(arr)
new_arr = []
new_arr.append(arr[0])
new_arr.append(arr[1])
new_arr.append('\n')
for i, vol in enumerate(arr):
    print(i,vol)
    if vol=='\n' and i!=len(arr)-1:
        new_arr.append(arr[i+1])
        new_arr.append(arr[i+2])
        new_arr.append('\n')
for i, vol in enumerate(new_arr):
    print(i,vol)

f = open(sys.argv[1]+'(simp)', "w")
f.writelines(new_arr)