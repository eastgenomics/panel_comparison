#!/usr/bin/env/ python
import os
import csv
lab_panel_dict = {}
panel_app_dict = {}
comparison_dict ={}
comparison_list = []
directory = '/home/katherine/projects/panel_comparison/panels_unzip'

for filename in os.listdir(directory):
    filepath = os.path.join(directory, filename)
    panel_app_panel = open(filepath)
    panel_app_reader = csv.reader(panel_app_panel, delimiter='\t')
    for line in panel_app_reader:
        if line[0] not in panel_app_dict:
            panel_app_dict[line[0]] = [line[-1]]
        else:
            panel_app_dict[line[0]].append(line[-1])
      

#print(panel_app_dict['Autism'])

with open('gemini_panels_200522') as lab_panel:
    lab_panel_reader = csv.reader(lab_panel, delimiter='\t')
    for line in lab_panel_reader:
        if line[0] not in lab_panel_dict:
            lab_panel_dict[line[0]] = [line[-1]]
        else:
            lab_panel_dict[line[0]].append(line[-1])

#print(lab_panel_dict['Thrombotic'])

for k in lab_panel_dict.keys() & panel_app_dict.keys():
    comparison_dict[k] = [lab_panel_dict[k], panel_app_dict[k]]
    comparison_list
#print(comparison_dict)

def panel_match(lab_panel):
    top_score = 0
    best_match = ''
    matching_panels = []
    for gene in lab_panel:
        for panel_name, gene_list in panel_app_dict.items():
            for k in set(lab_panel) & set(gene_list):
                if panel_name not in matching_panels:
                    matching_panels.append(panel_name)
    return matching_panels

print(lab_panel_dict['Familial hypercholesterolaemia'])
answer = panel_match(lab_panel_dict['Familial hypercholesterolaemia'])
print(answer)