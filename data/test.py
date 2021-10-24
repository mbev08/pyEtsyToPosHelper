import re
import os

"""
for process in new_list:
    if len(sorted_list) == 0:
        sorted_list.append(process)
    else:
        for index, sorted_process in enumerate(sorted_list):
            if process['memory'] >= sorted_process['memory']:
                sorted_list.insert(index, process)
"""
def chdir():
    print(os.getcwd())
    os.chdir('data')

def get_data():
    def get_raw_data():
        f = 'mem'
        with open(f, 'r') as fr:
            fc = fr.readlines()
        return fc

    def reformat_raw_data(raw_data):
        fd = {}
        for line in raw_data:
            line = line.split('|')
            fd[line[0]] = int(re.sub(r'[\r\n]', '', line[1]))

        return fd

    formatted_data = reformat_raw_data(get_raw_data())

    return formatted_data

def order_by_memory(data):
    ordered_list = {k: v for k, v in sorted(data.items(), key=lambda item: item[1], reverse=True)}
    return ordered_list

def get_total_memory(data):
    def get_total_kb():
        t = 0
        for process, memory in data.items():
            t += memory
        return float(t)

    def convert_kb_to_gb():
        return total_kb / conversion_unit

    conversion_unit = float(1000000)
    total_kb = get_total_kb()
    total_gb = convert_kb_to_gb()

    print(f"Total KB: {total_kb}, Total GB: {total_gb}")


def main():
    # chdir()
    data = get_data()
    data = order_by_memory(data)
    print(get_total_memory(data))



if __name__ == '__main__':
    main()