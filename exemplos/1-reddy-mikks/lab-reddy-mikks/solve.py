import sys
import model

def extract_values(line, data):
    key = line.split(': ')[0]
    content = line.split(': ')[-1]
    data[key] = (int(content.split(', ')[0]), int(content.split(', ')[1]))
    
def read(file_name):
    data = {}
    file = open(file_name, 'r')
    for line in file.readlines():
        line = line.strip()
        if line != '' and line[0] != '#':
            extract_values(line, data)
    file.close()
    return data

def main(file_name):
    data = read(file_name)
    result = model.solve(data)

    if len(result) > 1:
        print('x1 =', result[0])
        print('x2 =', result[1])
        print('z =', result[2])
    else:
        print('Termination condition:', result[0])

if __name__ == "__main__":
    file_name = sys.argv[1]
    main(file_name)