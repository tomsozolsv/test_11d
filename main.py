mala=float(input("Ievadi malas garumu! "))
maladiv=mala+5


if mala<5:
  pirmlauk=mala*mala
  otrlauk=maladiv*maladiv
  procenti=((otrlauk-pirmlauk)/((otrlauk+pirmlauk)/2))
  print(pirmlauk)
  print(otrlauk)
print(procenti)
