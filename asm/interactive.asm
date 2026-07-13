; An interactive addition calculator
        INP num1      ; Ask the user for the first number
        INP num2      ; Ask the user for the second number
        
        LOAD num1     ; Load the first number into the accumulator
        ADD num2      ; Add the second number
        STORE result  ; Store the answer
        
        OUT result    ; Print the answer to the screen
        HALT          ; Shut down

; --- Variables ---
num1:   DAT 0
num2:   DAT 0
result: DAT 0