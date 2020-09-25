#!/usr/bin/env/ python

genes_in_panel_app = []
with open('Familial hypercholesterolaemia.tsv') as f_h_panel:
    f_h_panel_list = []
    for i in f_h_panel:
        f_h_panel_list.append(i)
    for row in f_h_panel_list[1:]:
        genes_in_panel_app.append(row.split()[0])

genes_in_lab_panel = []
with open('gemini_panels_200522') as lab_panel:
    lab_panel_list = []
    for i in lab_panel:
      lab_panel_list.append(i)
    for row in lab_panel_list[1:]:
        genes_in_lab_panel.append(row.split()[-1])

genes_in_common = []
for i in genes_in_panel_app:
    if i in genes_in_lab_panel:
        genes_in_common.append(i)

print(genes_in_common)