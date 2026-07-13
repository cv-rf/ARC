# assembler.py

import os

OPCODES = {
    "LOAD": 1,
    "ADD": 2,
    "STORE": 3,
    "SUB": 4,
    "JZ": 5,
    "JUMP": 6
}

def assemble(asm_filepath, arc_filepath):
    machine_code = []

    with open(asm_filepath, 'r') as file:
        for line in file:
            line = line.split(';')[0].strip()
            if not line:
                continue

            parts = line.split()
            command = parts[0].upper()

            if command == "HALT":
                machine_code.append("900")

            elif command == "DAT":
                value = int(parts[1])
                machine_code.append(f"{value:03}")

            elif command in OPCODES:
                opcode = OPCODES[command]
                operand = int(parts[1])
                machine_code.append(f"{opcode}{operand:02}")

            else:
                print(f"ERROR: Unknown command '{command}' in {asm_filepath}")
                return
    with open(arc_filepath, 'w') as file:
        for code in machine_code:
            file.write(code + '\n')

    print(f"Successfully assembled: {os.path.basename(asm_filepath)} -> {os.path.basename(arc_filepath)}")

def main():
    asm_dir = "asm"
    programs_dir = "programs"

    if not os.path.exists(asm_dir):
        os.makedirs(asm_dir)
        print(f"Created '{asm_dir}' directory. Please add your .asm source files here.")
        return
    
    if not os.path.exists(programs_dir):
        os.makedirs(programs_dir)

    files_compiled = 0
    for filename in os.listdir(asm_dir):
        if filename.endswith(".asm"):
            asm_path = os.path.join(asm_dir, filename)
            arc_path = os.path.join(programs_dir, filename.replace(".asm", ".arc"))

            assemble(asm_path, arc_path)
            files_compiled += 1

    if files_compiled == 0:
        print(f"No .asm files found in '{asm_dir}'.")

if __name__ == "__main__":
    main()