# coding = utf-8

plink_para_path = r"M:\20200801\DSS\mg1655_small_output\pLink2.plink"
merged_mgf = open(r"M:\20200801\DSS\ecoli_DSS_merge.mgf", 'w')
f = open(plink_para_path).readlines()
for line in f:
    if line.startswith("spec_path"):
        mgf_path = line.split("=")[1].strip().replace(".pf2", ".mgf")
        print(mgf_path)
        with open(mgf_path) as fls:
            fl = fls.readlines()
        for line_sub in fl:
            merged_mgf.write(line_sub)

merged_mgf.close()