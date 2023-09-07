#!/bin/bash

# Loop over input files

# rm Times/ASP_Floyd_Least_time.txt
# rm Times/ASP_Floyd_Normal_time.txt
# rm Times/ASP_Grouping_time.txt
# rm Times/SMT_Floyd_Warshall_time.txt
rm -r Times 
rm -r Outputs

mkdir Times 
mkdir Outputs

for ((i=0; i<40; i++))
do
    input_file="Inputs/inputs${i}.txt"
    output_file="Outputs/outputs${i}.txt"


    # Run the Python script with the input and output file arguments
    timeout 10 cat  "$input_file"  | python3 Tester.py SMT_Grouping  > "$output_file, SMT_Grouping"
    timeout 10 cat  "$input_file"  | python3 Tester.py SMT_Floyd_Warshall  > "$output_file, SMT_Floyd_Warshall"
    timeout 10 cat  "$input_file"  | python3 Tester.py ASP_Grouping   > "$output_file,  ASP_Grouping "
    timeout 10 cat  "$input_file"  | python3 Tester.py ASP_Floyd_Normal  > "$output_file, ASP_Floyd_Normal"
    timeout 10 cat  "$input_file"  | python3 Tester.py ASP_Floyd_Least  > "$output_file, ASP_Floyd_Least"

done