#!/usr/bin/env/ python
import os
import sys
import csv
lab_panel_dict = {}
panel_app_dict = {}
directory = '/home/katherine/projects/panel_comparison/panels_unzip'

#put panelapp panels into a dictionary
for filename in os.listdir(directory):
    filepath = os.path.join(directory, filename)
    panel_app_panel = open(filepath)
    panel_app_reader = csv.reader(panel_app_panel, delimiter='\t')
    for line in panel_app_reader:
        if line[0] not in panel_app_dict:
            panel_app_dict[line[0]] = [line[-1]]
        else:
            panel_app_dict[line[0]].append(line[-1])

#put gemini panels into a dictionary
with open('gemini_panels_200522') as lab_panel:
    lab_panel_reader = csv.reader(lab_panel, delimiter='\t')
    for line in lab_panel_reader:
        if "GEL" not in line[0]:
            if line[0] not in lab_panel_dict:
                lab_panel_dict[line[0]] = [line[-1]]
            else:
                lab_panel_dict[line[0]].append(line[-1])

#output the best matches

#create a function to generate scores for how well the panels match:
def scoring(lab_panel_panel, panel_app_panel):
    matching_genes = []
    #compute number of lab panel genes in panel app panel:
    for gene in lab_panel_panel:
        if gene in panel_app_panel:
            matching_genes.append(gene)
            
    number_of_matches = len(matching_genes)

    #calculate the percentage of lab panel genes covered by panel app panel:
    lab_genes_in_pa_panel = number_of_matches/len(lab_panel_panel)
    pa_panel_coverage = number_of_matches/len(panel_app_panel)
    score = lab_genes_in_pa_panel * pa_panel_coverage
    return score, lab_genes_in_pa_panel, pa_panel_coverage
                


def panel_matching():

    #first create empty dictionary for best matches, and populate it with the gemini panels as keys and empty dicts as values.
    matches = {}
    key_list = lab_panel_dict.keys()
    for key in key_list:
        matches[key] = []
    for lab_panel_id, lab_panel_panel in lab_panel_dict.items():
        for panel_app_id, panel_app_panel in panel_app_dict.items():
                
            # check if exact match, if there is an exact match - this should be the only value for that key in the dict
            if lab_panel_panel == panel_app_panel:
                matches[lab_panel_id] = [panel_app_id, 1, 1, 1]
                break
            # if not, call the function to generate comparison scores:
            else:
                score, lab_coverage, pa_surplus = scoring(lab_panel_panel, panel_app_panel)
                top_score = 0
                second_top = 0
                third_top = 0
                fourth_top = 0

                # discount all panels with a score of 0
                if score == 0:
                    continue
                if score > top_score and panel_app_id not in matches[lab_panel_id]:
                    top_score = score          
                    matches[lab_panel_id].append([panel_app_id, round(score, 4)])
                elif score > second_top and panel_app_id not in matches[lab_panel_id]:
                    second_top = score
                    matches[lab_panel_id].append([panel_app_id, round(score, 4)])
                elif score > third_top and panel_app_id not in matches[lab_panel_id]:
                    matches[lab_panel_id].append([panel_app_id, round(score, 4)])
                elif score > fourth_top and panel_app_id not in matches[lab_panel_id] and len(matches[lab_panel_id] < 6):
                    matches[lab_panel_id].append([panel_app_id, round(score, 4)])


    return matches

matches = panel_matching()

list_of_v = panel_app_dict.values()

#show matches as a csv file, matching the lab panels with their closest panelapp match
with open ('best_matches.csv', 'w') as best_matches_variable:
    best_match_list =[]
    fields = ['Lab panel', 'Scoring data']
    for key, value in matches.items():
        new_line = {'Lab panel':key, 'Scoring data':value}
        best_match_list.append(new_line)
    output = csv.DictWriter(best_matches_variable, fieldnames=fields)
    output.writeheader()
    for match in best_match_list:
        output.writerow(match)