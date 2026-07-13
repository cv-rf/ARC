# ARC CPU Simulator

This repository contains a simple, lightweight Python simulation of an accumulator-based Central Processing Unit (CPU) and system memory (RAM).

## Features

- Accumulator-based architecture.
- 100-cell simulated RAM memory.
- Standard fetch-decode-execute instruction cycle.
- Detailed logs for execution steps.

## Instruction Set

The CPU decodes instructions using a three-digit integer format, where the hundreds digit represents the opcode and the tens/units digits specify the memory address (operand).

| Opcode | Instruction | Description |
|---|---|---|
| `1XX` | `LOAD` | Loads the value from memory address `XX` into the accumulator. |
| `2XX` | `ADD` | Adds the value at memory address `XX` to the current accumulator value. |
| `3XX` | `STORE` | Stores the current accumulator value into memory address `XX`. |
| `9XX` | `HALT` | Terminates program execution. |

## File Structure

- [cpu.py](cpu.py): Implements the CPU class containing registers, fetch, and execution logic.
- [memory.py](memory.py): Implements the Memory class simulating system RAM.
- [main.py](main.py): Entry point demonstrating how to configure memory, load a program, and run the simulator.

## Running the Simulator

To run the simulator and execute the sample program, use the following command:

```bash
python main.py
```
