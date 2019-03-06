with open("data.csv.txt",'r') as file:
    file_data=file.read()
print('Processing done.')


#print(file_data)

file_data_lines = file_data.split('\n')
#print(file_data_lines)

# Splitting induvidual lines.

# The original string representation.
#print(file_data_lines[1])
# The String split into different columns.
file_data_lines[1].split(',')

# Create the final cleaned list.
cleaned_file = []
# Loop to iterate and process each line.
for line in file_data_lines:
    processed_line = line.split(',')
    cleaned_file.append(processed_line)

# Display the cleaned list.
#print(cleaned_file)

# Converting the data into a dictionary.
# Creating the dicitonary with columns.
cols = cleaned_file[0]
loan_data_dict = dict.fromkeys(cols)

# Initialize the dictionary with empty lists.
for column in cols:
    loan_data_dict[column] = []

# Display the dictionary.
#print(loan_data_dict)

# Append the values to the respective columns.
for row in range(1, len(cleaned_file)):
    loan_data_dict['Loan_ID'].append(cleaned_file[row][0])
    loan_data_dict['Gender'].append(cleaned_file[row][1])
    loan_data_dict['Married'].append(cleaned_file[row][2])
    loan_data_dict['Education'].append(cleaned_file[row][3])
    loan_data_dict['ApplicantIncome'].append(cleaned_file[row][4])
    loan_data_dict['LoanAmount'].append(cleaned_file[row][5])
    loan_data_dict['Property_Area'].append(cleaned_file[row][6])

#print(loan_data_dict['Education'])

# Changing Graduate to 1 ; Non-graduate to 0

educationlist = loan_data_dict['Education']
#print(educationlist)

i=0

for i in range(0,len(educationlist)):
    if educationlist[i]=='Graduate':
        educationlist[i]=1
    else:
        educationlist[i]=0

#print(educationlist)

#Calculating mean values. Finding max and min values

loanamountlist = loan_data_dict['LoanAmount']
print(loanamountlist)

#sample = ['1','2','3','4']
#print(max(sample))

loanamountlist.sort()
print(loanamountlist)
print('Max value: ',max(loanamountlist))
print('Min value: ',min(loanamountlist))

sumlist=0

for i in range(0,len(loanamountlist)):
    sumlist=sumlist+int(loanamountlist[i])

actual_mean=float(sumlist/len(loanamountlist))
print('Mean: ',actual_mean)
    










