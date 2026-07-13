# ARC CPU Simulator

This repository contains a simple, lightweight Python simulation of an accumulator-based Central Processing Unit (CPU) and system memory (RAM), along with a custom assembly compiler (assembler).

## Features

- Accumulator-based CPU architecture with fetch-decode-execute instruction cycle.
- 100-cell simulated RAM memory space.
- A built-in assembler to compile assembly files (`.asm`) into machine code (`.arc`).
- Detailed execution logging showing step-by-step CPU operations.

## File Structure

```text
ARC/
├── asm/                    # Assembly source files (.asm)
│   ├── addition.asm        # Demo addition program
│   └── counter.asm         # Demo countdown loop program
├── programs/               # Compiled machine-code files (.arc)
│   ├── addition.arc
│   └── counter.arc
├── assembler.py            # Compiles .asm files to .arc files
├── cpu.py                  # Implements the CPU execution cycle and registers
├── main.py                 # Main entry point to load and run programs
├── memory.py               # Implements system RAM (100 memory cells)
├── LICENSE                 # GNU General Public License v3.0
└── README.md               # Project documentation
```

### Module Descriptions

- [cpu.py](cpu.py): Defines the `CPU` class responsible for registers (`pc`, `acc`), fetching instructions from memory, and decoding/executing them.
- [memory.py](memory.py): Defines the `Memory` class simulating RAM. It supports reading, writing, and loading machine-code arrays.
- [assembler.py](assembler.py): Translates human-readable assembly instructions and labels into 3-digit decimal machine-code instructions.
- [main.py](main.py): Lists compiled programs in `programs/` directory, prompts the user for selection, loads it into memory, and initiates the CPU run loop.

## Instruction Set

The CPU executes instructions using a three-digit decimal format: `OAA`. The hundreds digit (`O`) represents the **Opcode**, while the tens and units digits (`AA`) specify the **Memory Address** (operand).

### CPU Opcodes

| Opcode | Mnemonic | Machine Format | Description |
|---|---|---|---|
| `1` | `LOAD` | `1AA` | Loads the value stored at memory address `AA` into the Accumulator. |
| `2` | `ADD` | `2AA` | Adds the value at memory address `AA` to the current Accumulator. |
| `3` | `STORE` | `3AA` | Stores the current Accumulator value into memory address `AA`. |
| `4` | `SUB` | `4AA` | Subtracts the value at memory address `AA` from the Accumulator. |
| `5` | `JZ` | `5AA` | Jumps to instruction address `AA` if the Accumulator is equal to `0`. |
| `6` | `JUMP` | `6AA` | Jumps unconditionally to instruction address `AA`. |
| `9` | `HALT` | `900` | Shuts down the CPU. |

### Assembler Directives

- `DAT X`: Reserves a memory cell and initializes it with the constant value `X`.
- `Label:`: Declares a label referencing the current address for jumps and variable access.
- `;`: Denotes the start of a comment (everything after it on the line is ignored).

## Running the Simulator

### 1. Compile Assembly Source
If you make changes to `.asm` files in the `asm/` directory or add new ones, compile them using the assembler:

```bash
python assembler.py
```

*Expected output:*
```text
Successfully assembled: addition.asm -> addition.arc
Successfully assembled: counter.asm -> counter.arc
```

### 2. Run the CPU Simulator
Run the simulator to select and execute compiled machine-code programs:

```bash
python main.py
```

Upon running, choose a program from the menu. The simulator will log the instruction fetching, decoding, and execution steps, and output the final accumulator state.
```text
Available ARC programs:
[1] addition.arc
[2] counter.arc

Select a program to run (Enter Number): 1
FETCH: PC=[0] -> Instruction 104
EXEC:   LOAD value 5 from address 4 into ACC
FETCH: PC=[1] -> Instruction 205
EXEC:   ADD value 10 from address 5 to ACC (ACC is now 15)
FETCH: PC=[2] -> Instruction 306
EXEC:   STORE ACC (15) into address 6
FETCH: PC=[3] -> Instruction 900
EXEC:    HALT. Shutting down CPU.
Final Accumulator State: 15
```
