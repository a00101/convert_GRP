import os, sys

Input = (sys.argv[1])

U133A=open("GPL571-15670.txt")
U133ALines = U133A.readlines()


fw = open(Input+".grp","w")

for j in open(Input).readlines():
        spG=j.strip().split("\t")
        Tag=spG[0].upper()
        for i in U133ALines[18:]:
                sp= i.strip().split("\t")
                if len(sp) > 10:
                        prob= sp[0] ; gene = sp[10].upper()
                        if Tag == gene:
                                out = prob+"\n"
                                fw.write(out)
fw.close()


#ID     GB_ACC  SPOT_ID Species Scientific Name Annotation Date Sequence Type   Sequence Source Target Description      Representative Public ID     Gene Title Gene Symbol     ENTREZ_GENE_ID  RefSeq Transcript ID    Gene Ontology Biological Process        Gene Ontology Cellular Component     Gene Ontology Molecular Functio

#['201366_at', 'NM_004034', '', 'Homo sapiens', 'Jun 9, 2011', 'Exemplar sequence', 'GenBank', 'gb:NM_004034.1 /DB_XREF=gi:4809278 /GEN=ANXA7 /FEA=FLmRNA /CNT=239 /TID=Hs.78637.0 /TIER=FL+Stack /STK=60 /UG=Hs.78637 /LL=310 /DEF=Homo sapiens annexin A7 (ANXA7), transcript variant 2, mRNA. /PROD=annexin VII isoform 2 /FL=gb:NM_004034.1', 'NM_004034', 'annexin A7', 'ANXA7', '310', 'NM_001156 /// NM_004034', '0006874 // cellular calcium ion homeostasis // inferred from electronic annotation /// 0007599 // hemostasis // inferred from electronic annotation /// 0008283 // cell proliferation // inferred from electronic annotation /// 0008360 // regulation of cell shape // inferred from electronic annotation /// 0009651 // response to salt stress // inferred from electronic annotation /// 0009992 // cellular water homeostasis // inferred from electronic annotation', '0005625 // soluble fraction // inferred from electronic annotation /// 0005626 // insoluble fraction // inferred from electronic annotation /// 0005634 // nucleus // inferred from electronic annotation /// 0005635 // nuclear envelope // inferred from electronic annotation /// 0005829 // cytosol // inferred from electronic annotation /// 0005886 // plasma membrane // inferred from electronic annotation /// 0031982 // vesicle // inferred from electronic annotation', '0005509 // calcium ion binding // inferred from electronic annotation /// 0005515 // protein binding // inferred from physical interaction /// 0005515 // protein binding // inferred from electronic annotation /// 0005544 // calcium-dependent phospholipid binding // inferred from electronic annotation /// 0048306 // calcium-dependent protein binding // inferred from physical interaction']
