import glob

def merge_file_func(input_files,
                    merge_file,
                    exception_file):

    first_file = 'TRUE'
    delimiter_count = dict()
    
    with open(exception_file, 'w') as exceptfile:
        with open(merge_file, 'w') as outfile:
            for fname in input_files:
                print ('Processing ',fname)
                with open(fname) as infile:
                    if first_file == 'TRUE':
                        for line in infile:
                            count_delimiter = line.count(",")
                            if count_delimiter == 7:
                                outfile.write(line)
                            else:
                                exceptfile.write(line)
                                
                            if count_delimiter in delimiter_count:
                                delimiter_count[count_delimiter] += 1
                            else:
                                delimiter_count[count_delimiter] = 1
                        print(delimiter_count)
                        first_file = 'FALSE'
                    else:
                        noheader = infile.readlines()[1:]
                        for line in noheader:
                            count_delimiter = line.count(",")
                            if count_delimiter == 7:
                                outfile.write(line)
                            else:
                                exceptfile.write(line)
                                
                            if count_delimiter in delimiter_count:
                                delimiter_count[count_delimiter] += 1
                            else:
                                delimiter_count[count_delimiter] = 1
                        print(delimiter_count)

input_files = glob.glob("C:/Python/Merge/Updated*.csv")
merge_file = "C:/Python/Merge/Merged.csv"
exception_file = "C:/Python/Merge/Exception.csv"

merge_file_func(input_files,
                merge_file,
                exception_file)