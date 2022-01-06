import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size': 14})
import seaborn as sns
plt.rcParams['font.family'] = 'Times New Roman'

csfont = {'fontname': 'Times New Roman'}
sns.set_style("white")

def compute_pos(xticks, width, i):
    index = np.arange(len(xticks))
    n = 5
    correction = i-0.5*(n-1)
    return index + width*correction

def present_height(ax, bar):
    for rect in bar:
        height = rect.get_height()
        posx = rect.get_x()+rect.get_width()*0.5*1.6
        # posy = height*1.01
        posy = height + 1

        # ax.text(posx, posy, '%.3f' % height, rotation=90, ha='center', va='bottom')
        ax.text(posx, posy, '%.3f' % height, rotation=45, ha='center', va='bottom')



models = ['Live fingerprints', 'Base Network', 'Base Network + SegNet',
             'Base Network + SegNet + ID-Net', 'Base Network + SegNet + ID-Net + ID loss']
xticks = ['Evaluation results by Verifinger 10.0',
          'Evaluation results by NFIQ 2.0']
# xticks = ['Quality score by Verifinger 10.0']
scenarios = ['Live fingerprints', 'Base Network', 'Base Network + SegNet',
             'Base Network + SegNet + ID-Net', 'Base Network + SegNet + ID-Net + ID loss']
q_score_veri = [71.17, 34.01, 15.14, 76.70, 73.80]
q_score_veri_std =[20.25, 24.70, 14.22, 11.80, 14.50]

q_score_nfiq = [34.08, 9.98, 13.18, 41.55, 39.89]
q_score_nfiq_std = [15.01, 7.55, 9.19, 12.06, 11.54]

m_score = [325.56, 5.40, 4.77, 250.07, 329.54]
m_score_std = [208.10, 5.50, 6.71, 178.55, 196.06]

n_groups = 5

data = {scenarios[0]: q_score_veri[0],
        scenarios[1]: q_score_veri[1],
        scenarios[2]: q_score_veri[2],
        scenarios[3]: q_score_veri[3],
        scenarios[4]: q_score_veri[4]}

data = {scenarios[0]: [q_score_veri[0], q_score_nfiq[0]],
        scenarios[1]: [q_score_veri[1], q_score_nfiq[1]],
        scenarios[2]: [q_score_veri[2], q_score_nfiq[2]],
        scenarios[3]: [q_score_veri[3], q_score_nfiq[3]],
        scenarios[4]: [q_score_veri[4], q_score_nfiq[4]]}
data2 = {scenarios[0]: [q_score_veri_std[0], q_score_nfiq_std[0]],
        scenarios[1]: [q_score_veri_std[1], q_score_nfiq_std[1]],
        scenarios[2]: [q_score_veri_std[2], q_score_nfiq_std[2]],
        scenarios[3]: [q_score_veri_std[3], q_score_nfiq_std[3]],
        scenarios[4]: [q_score_veri_std[4], q_score_nfiq_std[4]]}

fig,ax = plt.subplots()
# colors = ['gray','salmon', 'orange', 'cadetblue', 'skyblue', 'lime']
colors = ['salmon', 'orange', 'cadetblue', 'skyblue', 'lime']
width = 0.17

for i, model in enumerate(models):
    pos = compute_pos(xticks, width, i)
    # bar = ax.bar(pos, data[model], alpha=0.5, width=width * 0.95, label=model, color=colors[i], yerr=q_score_veri_std[i])
    bar = ax.bar(pos, data[model],  yerr=data2[model], alpha=0.5, width=width * 0.95, label=model, color=colors[i], edgecolor='black', error_kw=dict(lw=0.5, capsize=5, capthick=0.5))

    present_height(ax, bar)  # bar높이 출력

ax.set_xticks(range(len(xticks)))
ax.set_xticklabels(xticks, fontsize=20, **csfont)
# ax.set_xlabel('Rank', fontsize=14, **csfont)

ax.set_ylim([0, 100])
ax.set_yticks([10, 20, 30, 40, 50, 60, 70, 80, 90,  100])
# plt.ylim(0, 100)
ax.yaxis.set_tick_params(labelsize=20)
ax.set_ylabel('Quality score', fontsize=20, **csfont)
#### 6. 범례 나타내기
ax.legend(scenarios
          , prop={"family":"Times New Roman",'size': 16}, loc='upper right', shadow=True, ncol=1)
#### 7. 보조선(눈금선) 나타내기
ax.set_axisbelow(True)
ax.yaxis.grid(True, color='gray', linestyle='dashed', linewidth=0.5)

#### 8. 그래프 저장하고 출력하기
# plt.tight_layout()
# plt.savefig('ex_barplot.png', format='png', dpi=300)
plt.show()

'''

scenarios = ['Live fingerprints', 'Base Network', 'Base Network + SegNet',
             'Base Network + SegNet \n+ ID-Net', 'Base Network + SegNet \n+ ID-Net + ID loss']
q_score_veri = [71.17, 34.01, 15.14, 76.70, 73.80]
q_score_veri_std =[20.25, 24.70, 14.22, 11.80, 14.50]

q_score_nfiq = [34.08, 9.98, 13.18, 41.55, 39.89]
q_score_nfiq_std = [15.01, 7.55, 9.19, 12.06, 11.54]

m_score = [325.56, 5.40, 4.77, 250.07, 329.54]
m_score_std = [208.10, 5.50, 6.71, 178.55, 196.06]

n_groups = 5

# fig, ax = plt.subplots()
fig = plt.figure(figsize=(10,8))
index = np.arange(n_groups)
bar_width = 0.35

for i in range(n_groups):
    rects2 = plt.bar(index*i, q_score_veri[i], bar_width, yerr=q_score_veri_std[i],
                     color='tomato', capsize=2, ecolor='k', label=scenarios[i])
    rects2 = plt.bar(index * i+bar_width, q_score_nfiq[i], bar_width, yerr=q_score_nfiq_std[i],
                     color='gold', capsize=2, ecolor='k', label=scenarios[i])

# rects2 = plt.bar(index, q_score_veri, bar_width, yerr=q_score_veri_std,
#                  color='tomato', capsize=2, ecolor='k', label='Quality score by Verifinger 10.0')
# rects2 = plt.bar(index+bar_width, q_score_nfiq, bar_width, yerr=q_score_nfiq_std,
#                  color='gold', capsize=2, ecolor='k', label='Quality score by NFIQ 2.0')
# rects2 = plt.bar(index, m_score, bar_width, yerr=m_score_std,
#                  capsize=3, ecolor='k', label='Matching score by Verifinger 10.0')

plt.xlabel('Scenarios', fontsize=15)
plt.ylabel('Quality score', fontsize=15)
plt.title('Quality evaluation results', fontsize=25)
plt.xticks(index + bar_width/2, scenarios, fontsize=15)
plt.ylim(0, 110)
plt.legend(fontsize=16)
plt.show()
'''