import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
get_ipython().run_line_magic('matplotlib', 'notebook')

df = pd.read_csv("*Path to the file*")

display(df)


df.keys()


from itertools import permutations, combinations
from IPython.display import HTML, display

params = ['MOS', 'Speech Level Probe [dBov]', 'Missed Voice [%]', 'Start Delay [ms]', 'Delay Spread [ms]', 'Delay Deviation [ms]']
table = {}
for p in params:
    table[p] = {}
    for p1 in params:
        table[p][p1] = None
table
    
cmb = list(combinations(params, 2))
for p1, p2 in cmb:
    corr = df[p1].dropna().corr(df[p2].dropna())
    table[p1][p2] = corr
df_t = pd.DataFrame(table)
df_t
code = "<table style=\"font-size:16px\">"
code += "<thead><tr><th></th>"
for p1 in params[1:]:
    code += "<th>%s</th>"%p1
code += "</tr></thead><tbody>"
for p1 in params[:-1]:
    code += "<tr><th>%s</th>"%p1
    for p2 in params[1:]:
        code += ("<td>%.3f</td>"%table[p1][p2]) if (not table[p1][p2] is None) else "<td>-</td>"
    code += "</tr>"
code += "</tbody></table>"

display(HTML(code))

f, axes = plt.subplots(5, 1)
f.set_size_inches(19, 20)
plotIdx = 0
for p1, p2 in cmb:
    if p1 == 'MOS':
        axes[plotIdx].scatter(df[p2].dropna(), df[p1].dropna())
        axes[plotIdx].grid()
        axes[plotIdx].set_xlabel(p2, size = 20)
        axes[plotIdx].set_ylabel(p1, size = 20)
        plotIdx += 1

figure, axes = plt.subplots()
figure.set_size_inches(15, 10)

axes.hist(df["MOS"].dropna(), normed=True, cumulative=True, label='CDF', histtype='step', alpha=0.8, color='k', linewidth=4)

axes.grid();
axes.set_ylabel("CDF", size = 40);
axes.set_xlabel("MOS", size = 40);
plt.xticks(size = 25);
plt.yticks(size = 25);

