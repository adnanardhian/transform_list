# SUM SQUARED FUNCTION
def sum_squared(L1,L2):
    result = 0
    for i in range(0,len(L1)):
        result+=(L1[i]-L2[i])**2
    return result
    
# MAIN FUNCTION
def change_value(L1,max_diff):
    L_temp = list(L1) # Temporary List
    while True:
        L_temp[len(L_temp)-1] = L_temp[len(L_temp)-1]-1
        L_temp = [L_temp[len(L_temp)-1] if x>=L_temp[len(L_temp)-1] else x for x in L_temp]
        if(L_temp[len(L_temp)-1] - L_temp[0]==max_diff):
            return(sum_squared(L1,L_temp))
        
        L_temp[0] = L_temp[0]+1
        L_temp = [L_temp[0] if x<=L_temp[0] else x for x in L_temp]
        if(L_temp[len(L_temp)-1] - L_temp[0]==max_diff):
            return(sum_squared(L1,L_temp))

# READ TXT FILE
file_object = open("PATH_TO_FILE/input_file.txt", "r")
input_file = file_object.read()
input_file = input_file.split('\n')
max_diff = int(input_file[0].split(' ')[1])
input_file = input_file[1:len(input_file)]
input_file = list(map(int, input_file))

# OUTPUT
output = change_value(input_file,max_diff)
print(output)
