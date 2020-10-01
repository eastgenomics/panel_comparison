#!/usr/bin/env/ python
import os
import csv
lab_panel_dict = {}
panel_app_dict = {}
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

with open('gemini_panels_200522') as lab_panel:
    lab_panel_reader = csv.reader(lab_panel, delimiter='\t')
    for line in lab_panel_reader:
        if "GEL" not in line[0]:
            if line[0] not in lab_panel_dict:
                lab_panel_dict[line[0]] = [line[-1]]
            else:
                lab_panel_dict[line[0]].append(line[-1])

def panel_match_scoring(a_lab_panel):
    best_match = ''
    second_best_match = ''
    third_best_match = ''
    top_score = 0
    second_top = 0
    third_top = 0
    for panel_id, a_panel in panel_app_dict.items():
        score_list = []
        for a_gene in a_panel:
            if a_gene in a_lab_panel:
                score_list.append(1)
            length_score = len(score_list)
            score = length_score/len(a_panel)
        if score > top_score:
            top_score = score
            best_match = panel_id
        elif score > second_top:
            second_top = score
            second_best_match = panel_id
        elif score > third_top:
            third_top = score
            third_best_match = panel_id
    return print("The best match is " + best_match + ", the second best match is " + second_best_match + ", and the third best match is " + third_best_match)

#to find a match add the lab/gemini panel to the search below
#e.g.
panel_match_scoring(lab_panel_dict['Hereditary Spastic Paraplegia Adult Onset'])