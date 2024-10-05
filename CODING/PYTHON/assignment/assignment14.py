def question1():
    with open('sowpods.txt', 'r') as file:
        data=file.read()
    words = data.split()
    words_with_uu = [i for i in words if 'UU' in i]
    if not words_with_uu:
        print("there are not words with uu consecutively")
    print(words_with_uu)
    
def question2():
    def consecutive(word):
        for i in range(len(word)-1):
            if word[i]==word[i+1]:
                return True
        return False
    consecutive_letters = set()
    with open('sonnet_words.txt', 'r') as f:
        content=f.read()
    data=content.split()
    for i in data:
        if consecutive(i):
            for j in range(len(i)-1):
                if i[j]==i[j+1]:
                        consecutive_letters.add(i[j])
    import string
    all_alphabets = set(string.ascii_uppercase)
    non_consecutive_letters = all_alphabets - consecutive_letters
    print("Alphabets that never appear consecutively in any word:")
    print(' '.join(sorted(non_consecutive_letters)))
    
def question3():
    with open('sonnet_words.txt', 'r') as f:
        content=f.read()
    data=content.lower()
    data=content.split()
    final=[]
    for i in data:
        if 'a' in i and 'e' in i and 'i' in i and 'o' in i and 'u' in i:
            final.append(i)
    if not final:
        print("there are no words with all the vowels in it!")
    else:
        print("the words with all vowels are: ")
        print(final)
def palindrome(word):
        rev=''
        for i in word:
            rev=i+rev
        if rev==word:
            return True
        else:
            return False
def question4():
    with open('sonnet_words.txt', 'r') as f:
        content=f.read()
    words=content.split()
    final=[]
    for word in words:
        if palindrome(word):
            final.append(word)
    if not final:
        print("there are no palindrome words in this file")
    else:
        print("the words that are palindrome are: ")
        print(final)
def question5():
    with open('sowpods.txt', 'r') as f:
        content=f.read()
    words=content.split()
    length=0
    final=[]
    for word in words:
        if palindrome(word):
            if length<len(word):
                length=len(word)
                final.append(word)
    print("the longest palindrome word is :")
    print(final[-1])
    
def question6():
    with open('sowpods.txt', 'r') as f:
        sowpods_words=f.read()
    with open('sonnet_words.txt', 'r') as f:
        sonnet_words=f.read()
    sowpods=sowpods_words.split()
    sonnet=sonnet_words.split()
    word=[snw for snw in sonnet if snw not in sowpods]
    print(word)
def main():
    print("ASSIGNMENT 14")
    print("1.qustion 1\n2.question 2\n3.question 3\n4.question 4\n5.Question 5\n6.question 6\n")
    n=int(input("enter a question number to run:"))
    if n==1:
        print("Find all the words which contains ‘uu in the file (sowpods.txt)\n")
        question1()
    elif n==2:
        print("Print all alphabets that never appears in sequence (back-to-back) in the words in the files. \n")
        question2()
    elif n==3:
        print("Print words in the file contains all the vowels.\n")
        question3()
    elif n==4:
        print("Print all palindrome words in the file\n")
        question4()
    elif n==5:
        print("Print the longest palindrome in sowpods.txt \n")
        question5()
    elif n==6:
        print("print the words that are in sonnet_words.txt but not in sowpods.txt \n")
        question6()
    else:
        print("enter a valid option\n")  
while True:
    main()
    c=input("Do you want to Continue[y/n]: ")
    if c=='y' or c=='Y':
        continue
    else:
         break