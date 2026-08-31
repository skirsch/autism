"""Read-only CSV analysis; render monthly onset histogram with CDC 2025 reference."""
import csv
import hashlib
import json
from collections import Counter
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

source = Path(r'C:\Users\stk\Downloads\SOA2-Grid view.csv')
out = Path(__file__).resolve().parent
with source.open(encoding='utf-8-sig', newline='') as f:
    records = list(csv.DictReader(f))
valid, excluded = [], []
for row in records:
    try:
        age = float(row['Age at onset (in months)'])
        if not age.is_integer() or age < 0 or age > 1200:
            raise ValueError('invalid or implausible age')
        valid.append((row, int(age)))
    except ValueError:
        excluded.append({'number': row['number'], 'age': row['Age at onset (in months)']})

def vax(row):
    schedule = row['On schedule'].strip()
    return ((schedule not in ['', "Don't know"] and 'No vaccines were ever given' not in schedule)
            or 'Vaccination' in row['What happened?'] or 'Vaccination' in row['3 days before onset'])

counts = Counter(age for _, age in valid)
groups = {'all': counts,
          'VAX': Counter(age for row, age in valid if vax(row)),
          'USA_VAX': Counter(age for row, age in valid if vax(row) and row['Country']=='USA'),
          'NEVER': Counter(age for row, age in valid if 'No vaccines were ever given' in row['On schedule'])}
metadata = {'source': str(source), 'sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
            'rows': len(records), 'valid': len(valid), 'excluded': excluded,
            'age_0_60': sum(n for a,n in counts.items() if a<=60),
            'older_60': sum(n for a,n in counts.items() if a>60),
            'groups': {name: {'n':sum(c.values()),'top':c.most_common(8),
                            'at_reference_months':{a:c[a] for a in [0,2,3,4,6,12,15,18,24,48,60]}}
                       for name,c in groups.items()},
            'reference': 'CDC child schedule notes dated July 2, 2025; illustrative, not cohort-matched',
            'reference_url':'https://www.cdc.gov/vaccines/hcp/imz-schedules/child-adolescent-notes.html'}
out.joinpath('summary.json').write_text(json.dumps(metadata,indent=2),encoding='utf-8')

plt.rcParams.update({'font.size':11, 'axes.spines.top':False, 'axes.spines.right':False})
fig = plt.figure(figsize=(13,10), facecolor='white')
gs = fig.add_gridspec(3,1,height_ratios=[3.5,1.6,1.35], hspace=.58)
ax=fig.add_subplot(gs[0]); schedule=fig.add_subplot(gs[1],sharex=ax); tail=fig.add_subplot(gs[2])
blue='#28638d'; orange='#b65c15'
ax.bar(range(61),[counts[a] for a in range(61)],width=.9,color=blue)
ax.set_xlim(-.7,60.7); ax.set_ylim(0,max(counts.values())*1.22)
ax.set_xticks(range(0,61,3)); ax.set_ylabel('Number of onset reports')
ax.set_xlabel('Reported PARENT onset age (months; one-month bins)')
ax.set_title(f'Onset age 0–60 months: {metadata["age_0_60"]} reports',loc='left',pad=12)
ax.grid(axis='y',alpha=.18); ax.set_axisbelow(True)
for age in [3,12,15,18,24,48]:
    ax.text(age,counts[age]+1.3,str(counts[age]),ha='center',fontsize=11)

lanes=[('DTaP',[2,4,6],[(15,18),(48,72)]),
       ('MMR / varicella',[],[(12,15),(48,72)]),
       ('Hib / PCV',[2,4,6],[(12,15)])]
for i,(name,dots,bands) in enumerate(lanes):
    y=2-i
    schedule.scatter(dots,[y]*len(dots),s=45,color=orange,zorder=3)
    for low,high in bands:
        right=min(high,60)
        schedule.plot([low,right],[y,y],color=orange,lw=9,solid_capstyle='butt')
        if high>60: schedule.plot(60,y,marker='>',color=orange,markersize=9)
        schedule.text((low+right)/2,y+.20,f'{low}–{high} mo',ha='center',fontsize=9)
schedule.set_yticks([2,1,0],['DTaP','MMR / varicella','Hib / PCV'])
schedule.set_ylim(-.4,2.6);schedule.set_xticks(range(0,61,3))
schedule.set_xlabel('Recommended age (months); bars indicate ranges, not observed vaccination dates')
schedule.set_title('Selected CDC routine vaccine ages — 2025 reference',loc='left',pad=13)
schedule.spines['left'].set_visible(False)
schedule.tick_params(axis='y',length=0)

older={a:n for a,n in counts.items() if a>60}
tail.bar(list(older),list(older.values()),width=.9,color=blue)
tail.set_xlim(60.5,max(older)+3);tail.set_ylim(0,max(older.values())+1)
tail.set_xticks([72,96,120,144,168,192,216]);tail.yaxis.set_major_locator(MaxNLocator(integer=True))
tail.set_ylabel('Reports');tail.set_xlabel('Reported onset age (months; one-month bins)')
tail.set_title(f'Older onset ages: {sum(older.values())} reports (expanded vertical scale)',loc='left')
for age,n in older.items():
    tail.text(age,n+(.42 if age in [84,162] else .09),str(age),ha='center',fontsize=9,rotation=60)

fig.suptitle('Reported onset age and routine vaccination ages',x=.115,y=.975,ha='left',fontsize=18)
fig.text(.115,.935,f'{len(records)} survey records | {len(valid)} plotted | all vaccination statuses and countries',fontsize=11)
fig.subplots_adjust(left=.14,right=.97,top=.885,bottom=.15)
fig.text(.14,.045,'One implausible value (2,212 months) excluded; source unchanged. Reference schedule is not matched to each child’s era/country.\nSelected doses shown, not the full schedule. Hib infant doses vary by product. Coinciding ages do not establish causation.',fontsize=9,color='#444444')
fig.savefig(out/'onset_age_cdc_reference.png',dpi=170)
plt.close(fig)
print(json.dumps(metadata,indent=2))
