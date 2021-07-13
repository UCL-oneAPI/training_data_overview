import csv
from collections import Counter

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import math

def visualize_results():
    warning_num = {}  # the dictionary stored the number of all kinds of warnings
    warning_doc = {}  # the dictionary stored all projects contained the warning
    warning_docNum = {} # the dictionary stored the number of projects contained the warning
    project_warnings = {} # each project and the warnings contained

    index_warning_type = [] # store warning types (index) for graph
    value_warning_num = [] # store the number of warnings for graph

    index_warning = [] # store warning types (index) for graph
    value_doc_num = [] # store the number of projects
    warning_rows = get_rows()
    for row in warning_rows:
        # Todo: replace print with visualization
        print(f'warning type: {row[0]}. project name: {row[1]}. path to file: {row[2]}.')
        if row[0] not in warning_num:
            warning_num[row[0]] = 1
            index_warning_type.append(row[0])
        else:
            warning_num[row[0]] += 1

        if row[0] not in warning_doc:
            warning_doc[row[0]] = {row[1]}
        else:
            warning_doc[row[0]].add(row[1])

        if row[1] not in project_warnings:
            project_warnings[row[1]] = {}
            project_warnings[row[1]][row[0]] = 1
        else:
            if row[0] not in project_warnings[row[1]]:
                project_warnings[row[1]][row[0]] = 1
            else:
                project_warnings[row[1]][row[0]] += 1
    print(warning_num)
    print(warning_doc)
    print(project_warnings)

    for w, d in warning_doc.items():
        warning_docNum[w] = len(d)
        index_warning.append(w)
        value_doc_num.append(len(d))

    for w, n in warning_num.items():
        value_warning_num.append(n)

    k = Counter(warning_num)
    top_three = k.most_common(3)
    print(top_three) # The three most numerous warnings
    # the three dictionary that record the number of three warnings in each project
    plot_index = 3
    for i in top_three:
        f_dic = {}
        plot_labels = []
        plot_values = []
        for p, w in project_warnings.items():
            if i[0] in w:
                f_dic[p] = w[i[0]]
        sorted_dic = sorted(f_dic.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
        print(sorted_dic)
        for pro in sorted_dic:
            plot_labels.append(pro[0])
            plot_values.append(pro[1])
        plt.figure(plot_index)
        plt.title("All projects that contain the warning " + i[0])
        plot_index += 1
        plt.plot(plot_labels, plot_values)
        plt.xticks(rotation=90, fontsize=5)
        plt.savefig(i[0] + '.jpg')


    # generate histograms
    # pie chart
    fig_1 = plt.figure(1, figsize=(40, 40))
    f_index = 1
    for p, w in project_warnings.items():
        pie_labels = []
        pie_values = []
        for warn, num in w.items():
            pie_labels.append(warn)
            pie_values.append(num)

        ax = fig_1.add_subplot(math.ceil(math.sqrt(len(project_warnings))), math.ceil(math.sqrt(len(project_warnings))), f_index)
        ax.set_title('Project' + str(p))
        plt.pie(pie_values, labels=pie_labels,
                startangle=180,
                shadow=True, autopct='%1.1f%%')
        plt.savefig('Pie_chart.jpg')
        f_index += 1


    x = np.arange(len(index_warning_type))
    bar_width = 0.35
    plt.figure(2)
    plt.bar(x, value_warning_num, bar_width, align="center", color="red", label="The number of the warning", alpha=0.5) # the number of different kind of warnings
    plt.bar(x+bar_width, value_doc_num, bar_width, align="center", color="blue", label="The number of projects", alpha=0.5) # the warnings, and the number of projects contained the warnings
    plt.xticks(rotation=90, fontsize=7)
    plt.xticks(x + bar_width / 2, index_warning_type)
    plt.legend()
    plt.savefig('Histogram.jpg')

    plt.show()




def get_rows():
    with open('warnings_data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        warnings = []

        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                # skip header
                pass
            else:
                warnings.append([row[0], row[1], row[2]])
            line_count += 1

        return warnings


if __name__ == "__main__":
    visualize_results()
