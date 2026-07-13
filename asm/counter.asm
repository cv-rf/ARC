; A countdown loop program
LOAD 06     ; Start of loop: Load the counter
JZ 05       ; If ACC is 0, jump to HALT (address 05)
SUB 07      ; Subtract 1
STORE 06    ; Save the updated counter
JUMP 00     ; Jump back to the start of the loop
HALT        ; Stop execution
DAT 3       ; Address 06: The counter value
DAT 1       ; Address 07: The decrement value 