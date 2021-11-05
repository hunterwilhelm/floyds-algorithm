SOURCE = "data.csv"
RESULT = "data_result.csv"


def parse_cell(s: str):
    try:
        if s == "":
            return float('inf')
        else:
            return int(float(s.strip()))
    except ValueError:
        return None


def get_data_from_file(file):
    data = []
    with open(file, "r", encoding='utf-8-sig') as f:
        header = f.readline()
        for line in f:
            row = map(parse_cell, line.strip().split(","))
            row = filter(lambda x: x is not None, row)
            row = list(row)
            if len(row) > 0:
                data.append(row)
    return (header, data)


def write_data_to_file(file, header, data):
    with open(file, "w", encoding='utf-8-sig') as f:
        f.write(header)
        header_items = header.split(',')
        lines = list(map(lambda r: ",".join(map(str, r)), data))
        output = '\n'.join([",".join(items)
                           for items in zip(header_items, lines)])
        f.write(output)


def do_floyds(source_data, n):
    D = source_data[:]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])
    return D


def main():
    (header, D) = get_data_from_file(SOURCE)
    result_data = do_floyds(D, 48)
    write_data_to_file(RESULT, header, result_data)


if __name__ == "__main__":
    main()
