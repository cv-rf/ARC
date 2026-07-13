# main.py

import os

from memory import Memory
from cpu import CPU

def load_program(filepath, memory):
    with open(filepath, 'r') as file:
        address = 0
        for line in file:
            instruction = line.strip()
            if instruction.isdigit():
                memory.write(address, int(instruction))
                address += 1

def main():
    ram = Memory(size=100)
    processor = CPU(memory=ram)

    programs_dir = "programs"

    if not os.path.exists(programs_dir):
        print(f"Directory '{programs_dir}' not found. Creating it...")
        os.makedirs(programs_dir)
        print("Please add .arc program files to the directory and run again.")
        return
    
    files = [
        f for f in os.listdir(programs_dir) 
        if os.path.isfile(os.path.join(programs_dir, f)) and f.endswith('.arc')
    ]

    if not files:
        print(f"No .arc programs found in '{programs_dir}'.")
        return
    
    print("Available ARC programs:")
    for idx, filename in enumerate(files):
        print(f"{[idx + 1]} {filename}")

    try:
        choice = int(input("\nSelect a program to run (Enter Number): "))

        if 1 <= choice <= len(files):
            selected_file = files[choice - 1]
            filepath = os.path.join(programs_dir, selected_file)

            load_program(filepath, ram)

            processor.run()

        else:
            print("Invalid selection. Exiting...")

    except ValueError:
        print("Please enter a valid numeric choice. Exiting...")

if __name__ == "__main__":
    main()