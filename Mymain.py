from pprint import pprint
import csv
import re

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

phone_patern = r"(\+7|8)\s*\(*(\d{3})\)*(\s|-)*(\d{3})-*(\d{2})-*(\d{2})" \
               r"(\s*)\(*(доб.)*\s*(\d+)*\)*"
name_patern = r"^(\w+)(\s*)(,?)(\w+)(\s*)(,?)(\w*)(,?)(,?)(,?)"
phone_replace = r"+7(\2)\4-\5-\6\7\8\9"
mame_replace = r"\1\3\10\4\6\9\7\8"

modify_n = []
for i_n in contacts_list:
    ful_fio = ','.join(i_n)
    res_mod = re.sub(name_patern, mame_replace, ful_fio)
    modify_n.append(res_mod.split(','))
# print(modify_n)
modify_p = []
for j_p in modify_n:
    ful_p = ','.join(j_p)
    res_mod = re.sub(phone_patern, phone_replace, ful_p)
    modify_p.append(res_mod.split(','))
# print(modify_p)
fin_res = []
for pfin in modify_p:
    for item in modify_p:
        if pfin[0] == item[0]:
            for k in range(1, len(modify_p[0])):
                if item[k] == '':
                    item[k] = pfin[k]
            if len(pfin) > len(modify_p[0]):
                pfin.pop()
            if pfin not in fin_res:
                fin_res.append(pfin)
# pprint(fin_res)
with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(fin_res)
