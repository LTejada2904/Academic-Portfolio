.data
prompt: .asciiz "Enter the value for i: "
resultMsg: .asciiz "The result of the summation is: "

.text
.globl main

main:
    # Print prompt message
    li $v0, 4
    la $a0, prompt
    syscall

    # Read integer from user
    li $v0, 5
    syscall

    # Store user input into $s0
    move $s0, $v0

    # Initialize sum to 0.0 in floating-point register $f12
    li $t0, 0
    mtc1 $t0, $f12
    cvt.s.w $f12, $f12

    # Initialize counter i (in $s1) to 1
    li $s1, 1

loop:
    # Convert loop counter to float and store in $f2
    mtc1 $s1, $f2
    cvt.s.w $f2, $f2

    # Calculate reciprocal 1/i and store in $f1
    li $t0, 1
    mtc1 $t0, $f0
    cvt.s.w $f0, $f0
    div.s $f1, $f0, $f2

    # Add reciprocal to sum
    add.s $f12, $f12, $f1

    # Increment loop counter
    addi $s1, $s1, 1

    # Loop until counter is greater than user input
    bgt $s1, $s0, endLoop
    j loop

endLoop:
    # Print result message
    li $v0, 4
    la $a0, resultMsg
    syscall

    # Print sum
    mov.s $f0, $f12
    li $v0, 2
    syscall

    # Exit program
    li $v0, 10
    syscall
