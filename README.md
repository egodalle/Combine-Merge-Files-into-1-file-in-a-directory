# Combine-Merge-Files-into-1-file-in-a-directory
This script will combine multiple files into 1 file in a directory.
If all the files has headers/column names, it will only copy the column names of the first file, the succeeding files, the copying will start at line 2, ignoring the headers.
It will check the number of delimiters per line. If the delimiter is not equal to the desired delimiter it will be written to an exception file to make sure that the output file will only contain the correct number of delimiter
