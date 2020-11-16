#!/usr/bin/python3
# coding : utf-8


def ses_diviseurs(n):
 
  i=2
  diviseurs = ” “
  while (i < n):
    if (n % i == 0):
      # Une chaîne se manipule comme une liste.
      if (len(diviseurs) == 0):
        diviseurs = diviseurs + str(i)
      else:
        diviseurs = diviseurs +“, ”+str(i)
      i = i + 1
  return diviseurs


n = int(input(“Entrez un nombre dont on cherche les diviseurs :  ”))
if (ses_diviseurs(n) == ““): 
    print (“Ce nombre n’a pas de diviseurs entiers différents de 1 et de lui-même.”)
else:
    if (ses_diviseurs(n).count(“,”) == 0):
        print (“Son diviseur est  : ”, ses_diviseurs(n))
    else:
        print (“Ses diviseurs sont  : “, ses_diviseurs(n))
