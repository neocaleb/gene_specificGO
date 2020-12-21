import sys

species=sys.argv[1]

ifile = open("GO_entrez_"+species+"20180214.txt")
lines = ifile.readlines();ifile.close()
GOid=[];GOterm=[];entrez=[]
for i in range(len(lines)):
    line = lines[i][:-1].split('\t')
    GOid.append(line[0])
    GOterm.append(line[1])
    entrez.append(line[2][:-1].split(';'))

ifile = open("GO_parents_children.txt")
lines = ifile.readlines();ifile.close()
GO_children=[]
for i in range(len(GOid)):
    GO_children.append([])
for i in range(len(lines)):
    line = lines[i][:-1].split('\t')
    if line[0] in GOid:
        GO_children[GOid.index(line[0])]=list(line[3][:-1].split(';'))

specificGOindex=GOid.index(sys.argv[2])
specificGOentrez=list(entrez[specificGOindex])
for i in range(len(GO_children[specificGOindex])):
    if GO_children[specificGOindex][i] in GOid:
        for j in entrez[GOid.index(GO_children[specificGOindex][i])]:
            if j not in specificGOentrez:
                specificGOentrez.append(j)


ofile = open("GO_entrez_"+species+"_"+GOterm[specificGOindex].replace(" ","_")+"_list.txt","w")
for i in specificGOentrez:
    ofile.write(i+'\n')
ofile.close()

ifile = open(species+"_gene_id_symbol_refseq.txt")
lines = ifile.readlines();ifile.close()
entrez_ref=[];symbol_ref=[]
for i in range(len(lines)):
    line = lines[i][:-1].split("\t")
    entrez_ref.append(line[0])
    symbol_ref.append(line[1])

ofile = open("GO_symbol_"+species+"_"+GOterm[specificGOindex].replace(" ","_")+"_list.txt","w")
for i in specificGOentrez:
    if i in entrez_ref:
        ofile.write(symbol_ref[entrez_ref.index(i)]+'\n')
ofile.close()
