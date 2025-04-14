#!/usr/bin/env python
"""
Project: ABX-accent
Corpus: AESRC
2022
"""

import argparse
import pandas as pd
import sys

def average_task_within(task_within, task_across, output_file):
    """
    Calculate weighted average scores for both within and across tasks
    and write results to an output file.
    
    Args:
        task_within (str): Path to the within task CSV file
        task_across (str): Path to the across task CSV file
        output_file (str): Path to write the output results
    """
    # Process within task data
    df_within = pd.read_csv(task_within, delimiter=';', header=0)
    total_sum_within = 0
    total_n_within = 0
    
    for index, row in df_within.iterrows():
        total_sum_within += row['score'] * row['n']
        total_n_within += row['n']
    
    mean_within = total_sum_within / total_n_within
    print(f"mean within: {mean_within}")
    
    # Process across task data
    df_across = pd.read_csv(task_across, delimiter=';', header=0)
    total_sum_across = 0
    total_n_across = 0
    
    for index, row in df_across.iterrows():
        total_sum_across += row['score'] * row['n']
        total_n_across += row['n']
    
    print(f"sum across: {total_sum_across}")
    print(f"total n across: {total_n_across}")
    mean_across = total_sum_across / total_n_across
    print(f"mean across: {mean_across}")
    
    # Write results to output file
    with open(output_file, "w") as f:
        f.write("{\n")
        f.write(f"within: {mean_within}\n")
        f.write(f"across: {mean_across}\n")
        f.write("}")

def average_task_across(task_file, output_file):
    """
    Calculate weighted average score for a single task
    and write the result to an output file.
    
    Args:
        task_file (str): Path to the task CSV file
        output_file (str): Path to write the output results
    """
    df = pd.read_csv(task_file, delimiter=';', header=0)
    total_sum = 0
    total_n = 0
    
    for index, row in df.iterrows():
        total_sum += row['score'] * row['n']
        total_n += row['n']
    
    mean = total_sum / total_n
    print(f"mean: {mean}")
    
    # Write result to output file
    with open(output_file, "w") as f:
        f.write("within: {\n")
        f.write(f"{mean}\n")
        f.write("}")

def main():
    """Parse command line arguments and run the appropriate functions."""
    parser = argparse.ArgumentParser(description="Calculate average scores for ABX-accent tasks")
    parser.add_argument("task_within", help="Path to the within task file")
    parser.add_argument("task_across", help="Path to the across task file")
    parser.add_argument("within_average_score", help="Output file for within task average score")
    parser.add_argument("across_average_score", help="Output file for across task average score")
    
    args = parser.parse_args()
    
    # Run the averaging functions
    average_task_across(args.task_within, args.within_average_score)
    average_task_within(args.task_within, args.task_across, args.across_average_score)

if __name__ == "__main__":
    main()
