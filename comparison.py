#!/usr/bin/env/ python

first_word_list = []
with open('Familial hypercholesterolaemia.tsv') as f_h_panel:
    f_h_panel_list = []
    for i in f_h_panel:
        f_h_panel_list.append(i)
    print(f_h_panel_list)
    for row in f_h_panel_list:
        first_word_list.append(row.split()[0])
    print(len(f_h_panel_list))


print(first_word_list)
print