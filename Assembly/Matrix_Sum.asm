.data
MatrixA:        .word 3, -8 
				.word 5, 9      	# Elements of Matrix A
MatrixB:        .word -9, 11
				.word 1, -5    		# Elements of Matrix B
ResultMatrix:   .space 16           # Space for result matrix
Operation:      .word 0             # Operation code: 0 for addition, 1 for subtraction
Newline:        .asciiz "\n"
Space:          .asciiz " "

.text
.globl main
main:
    # Load operation code
    lw $t0, Operation

    # Load matrix elements into registers
    lw $t1, MatrixA
    lw $t2, MatrixA+4
    lw $t3, MatrixA+8
    lw $t4, MatrixA+12

    lw $t5, MatrixB
    lw $t6, MatrixB+4
    lw $t7, MatrixB+8
    lw $t8, MatrixB+12

    # Decision making for addition or subtraction
    beq $t0, $zero, add_matrices
    j subtract_matrices

add_matrices:
    add $s0, $t1, $t5
    add $s1, $t2, $t6
    add $s2, $t3, $t7
    add $s3, $t4, $t8
    j store_result

subtract_matrices:
    sub $s0, $t1, $t5
    sub $s1, $t2, $t6
    sub $s2, $t3, $t7
    sub $s3, $t4, $t8

store_result:
    # Store result back into memory
    sw $s0, ResultMatrix
    sw $s1, ResultMatrix+4
    sw $s2, ResultMatrix+8
    sw $s3, ResultMatrix+12

    # Print results in matrix form
    li $v0, 1               # Prepare to print integer
    lw $a0, ResultMatrix    # Load the first result
    syscall
    li $v0, 4
    la $a0, Space
    syscall
    li $v0, 1
    lw $a0, ResultMatrix+4  # Load the second result
    syscall
    li $v0, 4
    la $a0, Newline
    syscall

    li $v0, 1
    lw $a0, ResultMatrix+8  # Load the third result
    syscall
    li $v0, 4
    la $a0, Space
    syscall
    li $v0, 1
    lw $a0, ResultMatrix+12 # Load the fourth result
    syscall

    # Exit the program
    li $v0, 10              # Load syscall for exit
    syscall
