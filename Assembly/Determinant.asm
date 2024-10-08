.data
MatrixInt:     	.word 3, -8
				.word 5, 9       	# Matrix elements as integers
MatrixFloat:   	.float 3.0, -8.0
				.float 5.0, 9.0 	# Matrix elements as floats
Choice:        	.word 0             # 0 for integers, 1 for floats
resultMsg:     	.asciiz "The determinant is: "
newline:       	.asciiz "\n"

.text
.globl main
main:
    # Load choice (0 = integer, 1 = float)
    lw $t0, Choice

    # Load matrix elements depending on the chosen type
    beq $t0, $zero, integer_calculations
    b compute_float

integer_calculations:
    # Load integers
    lw $t1, MatrixInt
    lw $t2, MatrixInt + 4
    lw $t3, MatrixInt + 8
    lw $t4, MatrixInt + 12

    # Calculate the determinant as an integer
    mul $t5, $t1, $t4     # t5 = a * d
    mul $t6, $t2, $t3     # t6 = b * c
    sub $t7, $t5, $t6     # t7 = ad - bc (integer result)

    # Print integer result
    la $a0, resultMsg
    li $v0, 4
    syscall

    move $a0, $t7
    li $v0, 1
    syscall

    j exit

compute_float:
    # Load floats
    l.s $f0, MatrixFloat
    l.s $f1, MatrixFloat + 4
    l.s $f2, MatrixFloat + 8
    l.s $f3, MatrixFloat + 12

    # Calculate the determinant as a float
    mul.s $f4, $f0, $f3   # f4 = a * d
    mul.s $f5, $f1, $f2   # f5 = b * c
    sub.s $f6, $f4, $f5   # f6 = ad - bc (float result)

    # Print float result
    la $a0, resultMsg
    li $v0, 4
    syscall

    mov.s $f12, $f6
    li $v0, 2
    syscall

exit:
    # Exit the program
    li $v0, 10
    syscall
