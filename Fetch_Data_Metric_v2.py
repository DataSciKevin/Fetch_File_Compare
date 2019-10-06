##########################
#Name - Kevin Ducat
#Date - 10/03/2019
#
#Version -
#Change the compare logic for the dictionaries
#Change the program to allow the passing of values 
#
#Fetch Data Challenge
#
#Program reads in 2 files and calculates a metric to determine how equal the two data files are.
#A value of 1 is fully matching, and value of 0 has no matches at all
#
#Assumptions -
#Puncutation will not be used in the compare.
#Case will not be used in the compare.
#
#Metric - 
#Matching Value = Number of Values Matched / Max Number of Values in either Dictionary
#Value of 1 is fully matching
#Value of 0 has no matching values
#
#Inputs -
#File Names
#
#Outputs -
#Matching Value Metric
##########################
from collections import Counter
import sys
    
#Read the data file
def read_file(in_name):
    with open(in_name,'r') as f:
        out_data = f.read()
    f.closed
    return out_data

#Remove punctuation and replace with a space
#Also makes all values lower case
def remove_punct(in_data):
    out_data = in_data.replace(','," ").replace('-'," ").replace('"'," ").replace('('," ").replace(')'," ").replace(':'," ").replace('.'," ").replace('!'," ") 
    out_data = out_data.lower()
    return out_data

#Counts the number of words in the list
def count_words(in_list):
    out_dict = {}                                 #Initialize Dictionary
    for word in in_list:                          #count number of times each word is in list.
        out_dict[word] = out_dict.get(word, 0) + 1
    return out_dict

#sorts the list from most common word occurance to least common word occurance
def sort_list(in_list):
    return Counter(in_list).most_common()

#Calculates the matching Value
#If All values match, it is a 1, and if none match, it is a 0
#Matching Value = Number of Values Matched / Max Number of Values in either Dictionary
#Rounds the metrix to 2 decimal places
def calculate_match_value(in_dict1, in_dict2):

    count_of_dict_match = 0.0                                # Initialize the count to zero
    for i in in_dict1:                                       # Loop through both Dicts and count the values that equal
        for j in in_dict2:
	    if i == j:
	        count_of_dict_match =  count_of_dict_match + 1 

    count_of_dict1 = len(in_dict1.values())                   # Get the length of the first dict
    count_of_dict2 = len(in_dict2.values())                   # Get the length of the second dict

    count_of_dict = count_of_dict2                          # Initialize the Value to 0    
    if count_of_dict2 < count_of_dict1:                     # Find the greater value 
        count_of_dict = count_of_dict1
	
    return_count = 0.0					    # Initialize the return counter
    return_count =  round((count_of_dict_match / count_of_dict), 2)  # Calculate the Metric and round to 2 decimals places
    return return_count

##
## Main Function to call other functions
##
def process_and_format_file(in_data1, in_data2):
    temp_data1 = read_file(in_data1)
    temp_data2 = read_file(in_data2)
                                                    # Removes Punctuation from the data.
    temp_data1 = remove_punct(temp_data1)
    temp_data2 = remove_punct(temp_data2)
                                                    # Splits the data of the file into individual elements
    out_data1 = temp_data1.split()                   
    out_data2 = temp_data2.split()                   
                                                    # Sorts the Lists for further analysis
    out_data1 = sort_list(out_data1)
    out_data2 = sort_list(out_data2)
                                                    # Count the iteration of the words in each list
    dict_1 = count_words(out_data1)
    dict_2 = count_words(out_data2)  
                                                        # Calculate the Match Value
    match_value = calculate_match_value(dict_1,dict_2)
                                                    #Count the number of distinct words in each list 
    return match_value

##################################################
#Call the main function with the file name
##################################################

File_Name_a = sys.argv[1];				# Read in first parameter value
File_Name_b = sys.argv[2];				# Read in second parameter value

Metric_Value = process_and_format_file(File_Name_a,File_Name_b);

print("Compare - File1 "), 
print(File_Name_a),
print("to File2 "), 
print(File_Name_b);
print(Metric_Value);