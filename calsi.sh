#!/bin/bash
#
read -p "Enter the number1: " num1
read -p "Enter the number2: " num2

read -p "Enter the opration:  " op

if [ $op = "Add" ]
then 
	echo "Addition is:" $(( $num1 + $num2 )) 
elif [ $op = "Subtract" ]
then 
	echo "Subtration is: " $(( $num1 - $num2 ))

elif [ $op = "Multiply" ]
then
	echo "Multiply is: " $(( $num1 * $num2 ))

elif [ $op = "Divide" ]
then
	echo "Division is: " $(( $num1 / $num2 ))
fi
