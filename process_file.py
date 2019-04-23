"""APPROACH = 
1. Open file
2. Search for relevant rows
3. Count them, sum the floats
4. Output the avg
"""

filename = input('What file do you want to open? ')
try:
    with open(filename, 'r') as file_object:
        row_count = 0
        flt_sum = 0
        for line in file_object:
            if 'X-DSPAM-Confidence:' in line:
                row_count += 1
                flt_sum += float(line.split()[-1])
        #print(flt_sum)
        print("Avg float value = ", round(flt_sum / row_count,2))
except FileNotFoundError:
        print('File does not exist!')