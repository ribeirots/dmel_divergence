# Uses the raw output from MS and count frequencies for downstream analyses.

import re 

output = open("freq_simple_ms.txt", "w")
sample_pop = 50



def pop_summary(simulations,Ne):

    pop = [Ne]

    pop_lines = []
    j = 0

    for samples in pop:
        sample_lines = []

        for i in range(0, samples):
            sample_lines.append(simulations[j][:-1])
            j += 1
        pop_lines.append(sample_lines) # Each vector is a vector with all lines for a pop

    count = []
    

    for samples in pop_lines:
        z = [len(samples)] # number of rows from each pop
        for i in range(0, len(samples[0])): # number of columns
            z.append(0) # z starts with 0s for all sites, len(z) = number of sites in a given simulation
        for line in samples:
            line2 = line
            line2 = [line[i:i+1] for i in range(0, len(line), 1)] #spliting str into characters to then convert to int
            line2 = list(map(int, line2))

            for j in range(0, len(samples[0])):
                z[j+1] += line2[j]
        count.append(z)


    invert_count = []

    for k in range(0, len(count[0])):
	print(len(count[0]))
	print(count[0])
        invert_line = []
        for line in count:
            invert_line.append(line[k])
        invert_line = list(map(str, invert_line))
        invert_line = "\t".join(invert_line) + "\n"
        invert_count.append(invert_line)
        
    return invert_count



with open("simple_ms.txt", "r") as file:
    next(file)
    next(file)
    lines = []
    sim_index = 0
    for line in file:
        if len(line) == 1: #line = \n
            line = line
	    lines = []
        elif line[0] == '/':
            line = line
        elif line[0] == 's':
            line = line
        elif line[0] == 'p':
            line = line
        elif line[0] == '0' or line[0] == '1':
            lines.append(line)
	if len(lines) == sample_pop:
            ps = pop_summary(lines, sample_pop)
            for site in ps:
                output.write(site)
            output.write("\n")
            lines = []
            sim_index += 1
print('Total simulations: '+str(sim_index))
output.close()

