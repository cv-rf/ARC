; Main Program
        INP num1        ; Get a number from the user
        LOAD num1       ; Load it into ACC

        CALL double_it  ; Jump to our function

        HALT            ; Stop the CPU when we return

; Variables
num1:   DAT 0

; Functions
double_it:
        ADD num1        ; Add the originial number to itself (doubling it)
        OUT 00          ; OUT prints a memory address. Let's print our new ACC
        PUSH            ; Pushing our doubled ACC to the stack
        POP             ; And popping it right back
        STORE num1      ; Store the doubled value
        OUT num1        ; Print the doubled value
        RET             ; Return to wherever we were called from