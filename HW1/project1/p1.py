
import matplotlib.pyplot as plt

# Prepocess the files
def file_handle():
    f=open("Hamlet.txt","r")
    contents =f.read()
    contents = contents.lower()
    contents = contents.replace(",", " ")
    contents = contents.replace(".", " ")
    contents = contents.replace("?", " ")
    contents = contents.replace("!", " ")
    contents = contents.split()
    return contents
    print(contents)

# Find the TOP n frequency of the words
def frequence(contents, n):
    frequence = []
    times = []
    for i in contents:
        if i not in frequence:
            frequence.append(i)
            times.append(contents.count(i))
            times.sort()
            times = times[::-1]
    
    # Find the Max frequency (n)       
    top_frequence = times[:n]
    top_frequence_words = []
    for j in top_frequence:
        for k in contents:
            if contents.count(k) == j and k not in top_frequence_words:
                top_frequence_dict = {j: k}
                top_frequence_str = str(top_frequence_dict)
                with open('p1_output.txt', 'a') as f:
                    f.write(top_frequence_str)
                    f.write("\n")
                print("'{}': {}".format(j, k))
                top_frequence_words.append(k)
                break
    
    return top_frequence_words, top_frequence

# Plot data
def plot(l1, l2):
    plt.figure(figsize=(9, 6))
    plt.bar(l1, l2)
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.show()

# Main function
if __name__ == "__main__":
    contents = file_handle()
    top_frequence_words, top_frequence = frequence(contents, 10)
    plot(top_frequence_words, top_frequence)
    
    