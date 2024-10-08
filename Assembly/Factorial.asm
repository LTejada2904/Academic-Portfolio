.data
    prompt: .asciiz "Enter a positive integer: "
    resultMsg: .asciiz "The factorial of the number is: "

.text
.globl main

main:
    # Prompt user for input
    li $v0, 4
    la $a0, prompt
    syscall
    
    # Read user input (integer)
    li $v0, 5
    syscall
    
    # Move input to $t1
    move $t1, $v0
    
    # Check for non-positive input
    blez $t1, error
    
    # Initialize factorial result with 1
    li $t0, 1

loop:
    # Multiply $t0 by $t1
    mul $t0, $t0, $t1
    
    # Decrement $t1
    addi $t1, $t1, -1
    
    # Continue loop while $t1 > 0
    bgtz $t1, loop
    
    # Print result message
    li $v0, 4
    la $a0, resultMsg
    syscall
    
    # Print factorial result
    move $a0, $t0
    li $v0, 1
    syscall
    
    # Exit program
    li $v0, 10
    syscall

error:
    li $v0, 10
    syscall
