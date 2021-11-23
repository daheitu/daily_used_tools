
import os
import shutil  

wk_dir = r"M:"


def delete_ms1_files(wk_dir):
    for root, dirs, fls in os.walk(wk_dir):
        for fl in fls:
            if fl.endswith(".ms1") or fl.endswith(".ms2") or fl.endswith(".pf1") or fl.endswith(".pf1idx") or fl.endswith("rawInfo"):
                os.remove(os.path.join(root, fl))


def delete_plink2_tmp(wk_dir):
    for root, dirs, fls in os.walk(wk_dir):
        if root.endswith("\\tmps"):
            print(root)
            shutil.rmtree(root)


delete_plink2_tmp(wk_dir)
delete_ms1_files(wk_dir)