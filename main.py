# main.py

from memory import Memory
from cpu import CPU

def main():
    ram = Memory(size=100)
    processor = CPU(memory=ram)

    ram.write(98, 15)
    ram.write(99, 30)

    my_program = [
        198,    # LOAD 98
        299,    # ADD 99
        390,    # STORE 90
        900     # HALT
    ]

    ram.load_program(my_program)
    processor.run()

    print(f"\nResult stored in RAM address 90: {ram.read(90)}")

if __name__ == "__main__":
    main()