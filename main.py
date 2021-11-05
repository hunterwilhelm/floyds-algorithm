FILE = "data.csv"
def parse_cell(s:str):
    if s == "":
        return float('inf')
    else:
        return int(float("0" + s.strip()))

def get_data_from_file(file):
    data = []
    with open(file, "r", encoding='utf-8-sig') as f:
        for line in f:
            data.append(list(map(parse_cell, line.strip().split(","))))
    return data

def write_data_to_file(file, data):
    with open(file, "w", encoding='utf-8-sig') as f:
        lines = list(map(lambda r: ",".join(map(str, r)), data))
        output = '\n'.join(lines)
        f.write(output)

if __name__ == "__main__":
    D = get_data_from_file(FILE)
    n = 48
    for k in range(n):
        for i in range(n):
            for j in range(n):
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])
    write_data_to_file("result.csv", D)