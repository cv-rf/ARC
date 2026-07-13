; A countdown loop program using labels and variables
start:    LOAD counter  ; Load the counter
          JZ end        ; If it hits 0, jump to the end
          SUB step      ; Subtract our step value
          STORE counter ; Save it back to memory
          JUMP start    ; Jump back to the top of the loop

end:      HALT

; Variables Data Section
counter:  DAT 3
step:     DAT 1