###!/usr/bin/python
###menulis data ke dalam berkas
##berkas = open("L200180139.txt", "w")
##berkas.write("Nim L200180139.""\n")
##berkas.write("29-04-2000.""\n")
##berkas.write("Muhammad Saiful Mujab.")
##berkas.close()


###!/usr/bin/python
###menulis data ke dalam berkas
##berkas = open("L200180139", "w")
##berkas.write("Nim L200180139.")
##berkas.write("29-04-2000.")
##berkas.write("Muhammad Saiful Mujab.")
##berkas.write(" kota Rembang")
##berkas.close()
##
##berkas = open("L200180139", "r")
##print (berkas.readlines())
##berkas.close()


import shelve

F = shelve.open("dataku.data")
F["nama"] = ['Muhammad Saiful Mujab']
F["NIM"] = ['NIM L200180139']
F["Kota"] = ['Rembang']
F["tanggal_lahir"] = ['29-04-2000']
F.close()

F = shelve.open("dataku.data")
F.close()


##import shelve
##
##F = shelve.open("dataku.data")
##F["nama"] = ['Muhammad Saiful Mujab']
##F["NIM"] = ['NIM L200180139']
##F["Kota"] = ['Rembang']
##F["tanggal_lahir"] = ['29-04-2000']
##F.close()
##
##F = shelve.open("dataku.data")
##print F["nama"]
##print F["NIM"]
##print F["Kota"]
##print F["tanggal_lahir"]
##F.close()
