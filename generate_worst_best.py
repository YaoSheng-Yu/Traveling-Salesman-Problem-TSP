import sys

def main(argv):
# input output file names
    # the command is strictly: "python3 generate_testcases.py [scenario] [graph_of_size_n] -o [output_filename]"
    # scenario 1 = best case, scenario 2 = worst case
    worst_case, best_case = False, False
    scenario = int(argv[0])
    n = int(argv[1])
    outputfile = argv[3]
    
    '''
    print ('size n is ', n)
    print ('Output file is ', outputfile)
    print(scenario)
    '''


    # generate ratio close to 1: ratio = TSP tour / MST
    if scenario == 1:
        with open(outputfile, 'a') as f:
            f.write(str(n) + "\n" + str(n) + "\n")
            for i in range(n-1):
                f.write(str(i) + " " + str(i+1) + " " + "1\n")
            f.write(str(n-1) + " 0 1\n")
    
    # generate ratio close to 2: ratio = TSP tour / MST
    elif scenario == 2:
        with open(outputfile, 'a') as f:
            f.write(str(n) + "\n" + str(n) + "\n")
            for i in range(n-1):
                f.write(str(i) + " " + str(i+1) + " " + "1\n")
            f.write(str(n-1) + " 0 " + str(n-2) + "\n")



if __name__ == "__main__":
    main(sys.argv[1:])