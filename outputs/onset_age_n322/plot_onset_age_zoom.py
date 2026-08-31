"""Monthly 2–20-month crop and adjacent-month comparisons at requested ages."""
import csv
from collections import Counter
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

source=Path(r'C:\Users\stk\Downloads\SOA2-Grid view.csv')
with source.open(encoding='utf-8-sig',newline='') as f:
    rows=list(csv.DictReader(f))
counts=Counter(int(r['Age at onset (in months)']) for r in rows)
ages=list(range(2,21)); targets=[2,4,6,12,15,18]
fig,ax=plt.subplots(figsize=(11,5.5))
ax.bar(ages,[counts[a] for a in ages],width=.82,color='#28638d')
for a in targets:
    ax.axvline(a,color='#b65c15',alpha=.6,lw=1,linestyle='--',zorder=0)
    ax.plot(a,-2.5,marker='^',color='#b65c15',markersize=7)
for a in ages:
    ax.text(a,counts[a]+.7,str(counts[a]),ha='center',fontsize=11)
ax.set_xticks(ages);ax.set_xlim(1.4,20.6);ax.set_ylim(-4,max(counts[a] for a in ages)*1.16)
ax.set_yticks(range(0,51,10));ax.set_ylabel('Number of onset reports')
ax.set_xlabel('Reported PARENT onset age (months; one-month bins)',labelpad=10)
ax.grid(axis='y',alpha=.18);ax.set_axisbelow(True)
ax.spines[['top','right']].set_visible(False)
fig.suptitle('Onset age: 2–20 months',x=.09,ha='left',fontsize=17,y=.98)
fig.text(.09,.91,f'{sum(counts[a] for a in ages)} reports in view; all vaccination statuses and countries',fontsize=11)
fig.text(.09,.025,'Orange markers: requested comparison ages 2, 4, 6, 12, 15, 18 months.\nLocal peak = more reports than both adjacent months; month 1 is checked for the 2-month comparison.',fontsize=10)
fig.subplots_adjust(left=.09,right=.98,top=.85,bottom=.21)
fig.savefig(Path(__file__).with_name('onset_age_2_to_20.png'),dpi=170)
for a in targets:
    print(a,counts[a-1],counts[a],counts[a+1],counts[a]>max(counts[a-1],counts[a+1]))
print('IN_VIEW',sum(counts[a] for a in ages),'ROWS',len(rows))
