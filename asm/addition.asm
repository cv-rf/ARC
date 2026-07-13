; A simple addition program
LOAD 04     ; Load the first number into ACC
ADD 05      ; Add the second number into ACC
STORE 06    ; Store the result in address 06
HALT        ; Stop execution
DAT 5       ; Address 04: the first number
DAT 10      ; Address 05: the second number
DAT 0       ; Address 06: space for the result