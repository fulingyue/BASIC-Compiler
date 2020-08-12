import pickle
import base64

file_template_list = ['testcases/array_test/array_{}.txt', 'testcases/basic_test/basic_{}.txt', 'testcases/control_test/control_{}.txt', 'testcases/op_test/op_{}.txt', 'testcases/sema/sema_{}.txt']

array_size = 5
basic_size = 10
control_size = 5
op_size = 10
sema_size = 20

file_list = []
for i in range(array_size):
    file_list.append(file_template_list[0].format(i + 1))

for i in range(basic_size):
    file_list.append(file_template_list[1].format(i + 1))

for i in range(control_size):
    file_list.append(file_template_list[2].format(i + 1))

for i in range(op_size):
    file_list.append(file_template_list[3].format(i + 1))

for i in range(sema_size):
    file_list.append(file_template_list[4].format(i + 1))

test_case = []
for f in file_list:
    all_lines = open(f, 'r').readlines()
    file_name = all_lines[0].split(' ')[2]
    input_data = all_lines[1].split(':')[1].strip()
    exit_code = all_lines[2].split(':')[1].strip()
    all_lines[2] = '3 REM asfeskejfewf'
    test_case.append((file_name.strip('\n'), ''.join(input_data).strip('\n'), -1 if 'FAIL' in exit_code else int(exit_code), '{}\n'.format(''.join(all_lines))))
    print('Finish: ', f)

s = pickle.dumps(test_case)
print(base64.b64encode(s).decode())