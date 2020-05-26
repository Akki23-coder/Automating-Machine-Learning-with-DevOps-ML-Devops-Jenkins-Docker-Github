data_file = open('/root/mlopstask1/data.txt','w')
input_file = open('/root/mlopstask1/input.txt','w')

data_file_data = str(old_accuracy) + '\n' + str(layer) + '\n' + str(line) + '\n' + str(entered_data) + '\n' + str(old_data) + '\n' + str(index_fc)

data_file.write(data_file_data)                           

data_file.close()

input_file_data = '\n'.join(inputs)

input_file.write(input_file_data)                      

input_file.close()
