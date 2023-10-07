# instructions
OPS = {
        'halt': 0, 
        'add': 2, 
        'sub': 2, 
        'mul': 2, 
        'and': 2, 
        'or': 2, 
        'xor': 2, 
        'not': 1, 
        'shl': 1, 
        'shr': 1, 
        'copy': 2, 
        'mvi': 2, 
        'load': 2, 
        'store': 2, 
        'jump': 1,
        'jzro': 2
}

MACROS = ['label'] # starting it as an array for now, in case I add more later

def open_file(filename):
    file = open(filename, 'r')
    lines = []
    for line in file:
        newline = line.strip()
        lines.append(newline.lower())
    file.close()
    return lines

def remove_comments(filelines):
    lines = []
    for line in filelines:
        newline = line.split(';')[0]
        if newline != '':
            lines.append(newline)
    return lines

def dec_to_bin(num, prec):
    return str(bin(num)[2:].zfill(prec))

def parse_opcode(phrase):
    if phrase in OPS:
        dec_opcode = list(OPS.keys()).index(phrase)
        opcode = dec_to_bin(dec_opcode, 4)
        return opcode
    else:
        print('Error- not an operation: ', phrase)
        return None

def convert(filelines):
    converted_lines = []
    for line in filelines:
        splitline = line.split(' ')
        operation = splitline[0]
        if OPS[operation] == 2:
            dest = int(splitline[1].replace('r', ''))
            source = int(splitline[2].replace('r', ''))
            output = parse_opcode(operation) + dec_to_bin(dest, 6) + dec_to_bin(source, 6)
            converted_lines.append(output)
        elif OPS[operation] == 1:
            dest = int(splitline[1].replace('r', ''))
            output = parse_opcode(operation) + dec_to_bin(dest, 6) + '000000'
            converted_lines.append(output)
        else:
            output = parse_opcode(operation) + '000000000000'
            converted_lines.append(output)
    return converted_lines

def write_file(filename, linelist):
    file = open(filename, 'w')
    for line in linelist:
        file.write(line + '\n')
    file.close()


def main():
    file_input = input('Enter filename: ')
    new_file_name = file_input.replace('.asm', '.txt')
    file = open_file(file_input.strip())
    no_comments = remove_comments(file)
    converted = convert(no_comments)
    write_file(new_file_name, converted)

main()
