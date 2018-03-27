import sys
import re
kelime=sys.argv[1]
verilen_kelime=[]
verilen_kelime2=[]
for i in kelime:
    verilen_kelime.append(i)
    verilen_kelime2.append(i)
tahmin_harfleri=re.split(',',sys.argv[2])
gizli_hal=["_"]*len(verilen_kelime)
Can=5
print("You have",Can,"guesses left")
print(gizli_hal)
print("--------------------------")
mod=True
kullanılan_harfler=[]
for i in tahmin_harfleri:
    if(Can>0):
        if mod==True:
            if i in verilen_kelime:
                print("Guessed word: "+i+" You are in IN mode")
                mod=True
                print("You have", Can, "guesses left")
                kullanılan_harfler.append(i)
                if verilen_kelime.count(i)>1:
                    for j in range(verilen_kelime.count(i)):
                        a=verilen_kelime.index(i)
                        gizli_hal[a]=i
                        verilen_kelime[a]=0
                else:
                    a=verilen_kelime.index(i)
                    gizli_hal[a]=i
                    verilen_kelime[a]=0
            elif(i in kullanılan_harfler):
                Can-=1
                print("Guessed word: "+i+" is used in IN mode.The game turned into OUT mode")
                print("You have", Can, "guesses left")
                mod=False
            else:
                Can-=1
                print("Guessed word:" + i + " The game turned into OUT mode")
                mod=False
                print("You have", Can, "guesses left")
            print(gizli_hal)
            print("--------------------------")
        else:
            if i in verilen_kelime2:
                Can -= 1
                print("Guessed word: "+i+" You are in Out mode")
                mod=False
                print("You have", Can, "guesses left")
            else:
                print("Guessed word:" + i + " The game turned into IN mode")
                mod=True
                print("You have", Can, "guesses left")
            print(gizli_hal)
            print("--------------------------")
    else:
        print("You have no right ")
        print("You lost the game")
if(verilen_kelime2==gizli_hal):
    print("You won the game")
else:
    print("You finished all letters")
    print("You lost the game")

