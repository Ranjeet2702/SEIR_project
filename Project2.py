from sys import*
import requests
from bs4 import BeautifulSoup

# define function to store word with frequency in a dictionary
def frequency_words(s):
    Words = s.lower().split()
    clean_Words =[]
    for word in Words:
        if word.isalnum():
            clean_Words.append(word)
    freq = {}
    for word in clean_Words:
        if word in freq:
            freq[word]+=1
        else:
            freq[word]=1
    return freq

#Get the first URL from command line arguments
#send an HTTP GET request to fetch its webpage content
response1 = requests.get(argv[1])
response2 = requests.get(argv[2])

# parse the html content of the webpage using BeautifulSoup
html_content1 = BeautifulSoup(response1.text,"html.parser")
html_content2 = BeautifulSoup(response2.text,"html.parser")


# get word with their frequency in a dictionary
words_url1 = frequency_words(html_content1.get_text())
words_url2 = frequency_words(html_content2.get_text())
# print("word freq url1 : ", words_url1)
# print("word freq url2 : " ,words_url2)



#define a function to calculate word with their hashvaule and store in a dictionary 
def hash_for_word(my_dict):
    my_newdict ={}
    p = 53
    m = 2**64
    for word ,weight in my_dict.items():
        i=0
        hashvalue =0
        for ch in word:
            hashvalue = (hashvalue + ord(ch) * (p**i)) % m
            i+=1
        my_newdict[word] = (weight,hashvalue)
            
    return my_newdict   


#get word with their hashvalue
hash_word1 = hash_for_word(words_url1)
hashword2 = hash_for_word(words_url2)
# print("word hash url1:",hash_word1)
# print("word hash url2:",hashword2)


#apply simhash
def cal_simhash(hashvalue_dict):
    v = [0]*64
    for word ,(weight,hashvalue)  in hashvalue_dict.items():

        for i in range(64):
            if hashvalue & (1<<i) != 0:
                v[i] += weight
            else:
                v[i]-=weight

    new_bits =""
    for i in range(64):
        if v[i]>=0:
            new_bits+="1"
        else:
            new_bits+="0"
    return new_bits[::-1]


#compute simhash for document
simhash_webpage1 = cal_simhash(hash_word1)
simhash_webpage2 = cal_simhash(hashword2)
print("simahash_of_url1:",simhash_webpage1)
print("simahs_of_url2:" ,simhash_webpage2)



#define a function to count common bits between two simhash value of given document
def count_commonbits(simhash_url1,simhash_url2):
    if(len(simhash_url1) != len(simhash_url2)):
        print("error")
    else:
        n = len(simhash_url1)
        left =0
        count =0
        while(left < n):
            if simhash_webpage1[left] == simhash_webpage2[left]:
                count+=1
            left+=1
        
        return count
print("common bits between two webpages :", count_commonbits(simhash_webpage1,simhash_webpage2))




    












