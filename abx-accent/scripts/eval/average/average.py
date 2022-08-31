'''
Project: ABX-accent
Corpus: AESRC
2022
'''
#!/usr/bin/env python
import pandas as pd 
def moyenne_task_within(task_within, task_across, outputfile):
    data = [line.strip().split(" ") for line in  open(task_within, 'r', encoding="utf8")]

    total_sum = 0
    n_lines = 0
    
    df = pd.read_csv(task_within, delimiter=';', header=0)
    total_sum_within = 0
    total_n_within = 0
    for index, row in df.iterrows():
        total_sum_within += row['score'] * row['n']
        total_n_within += row['n']
    print("sum_within: ",total_sum_within)
    print("total n within :",total_n_within)


    mean_within = total_sum_within / total_n_within
    print("mean: ",mean_within)
    

    #across
    df = pd.read_csv(task_across, delimiter=';', header=0)
    total_sum_across = 0
    total_n_across = 0
    for index, row in df.iterrows():
        total_sum_across += row['score'] * row['n']
        total_n_across += row['n']
    print("sum_across: ",total_sum_across)
    print("total n across :",total_n_across)

    #mean = total_sum / len(df.index)
    mean_across = total_sum_across / total_n_across
    print("mean_across: ",mean_across)

    f = open(outputfile,"w")
    f.write("{")
    f.write("\nwithin: ")
    f.write(str(mean_within))
    f.write(" \n")
    f.write("across: ")
    f.write(str(mean_across))
    f.write(" \n}")
    
    f.close()
def moyenne_task_across(task_file, outputfile):
    data = [line.strip().split(" ") for line in  open(task_file, 'r', encoding="utf8")]

    total_sum = 0
    n_lines = 0
    
    df = pd.read_csv(task_file, delimiter=';', header=0)
    total_sum = 0
    total_n = 0
    for index, row in df.iterrows():
        total_sum += row['score'] * row['n']
        total_n += row['n']
    print("sum: ",total_sum)
    print("total n :",total_n)

    #mean = total_sum / len(df.index)
    mean = total_sum / total_n
    print("mean: ",mean)
    
    f = open(outputfile,"w")
    f.write("within : { \n")
    f.write(str(mean))
    f.write(" \n}")
    f.close()
    

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("task_within", help="within task file")
    parser.add_argument('output_file')
    parser.parse_args()
    args, leftovers = parser.parse_known_args()
    moyenne_task_across(args.task_within, args.output_file)


