import matplotlib.pyplot as plt
import numpy as np

labels = ['Antibiotics', 'Appendectomy']
sizes = [47, 53]
colors = ['#ff9999','#66b3ff']
 
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.axis('equal')
plt.title('Treatment Assignment')
plt.show()


complications_antibiotics = 8.1
complications_appendectomy = 3.5

barWidth = 0.3
 
bars1 = [complications_antibiotics]
bars2 = [complications_appendectomy]

r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]

plt.barh(r1, bars1, color='#ff9999', height=barWidth, edgecolor='white', label='Antibiotics')
plt.barh(r2, bars2, color='#66b3ff', height=barWidth, edgecolor='white', label='Appendectomy')
 
plt.xlabel('Rate per 100 Participants')
plt.ylabel('Treatment Group')
plt.yticks([r + barWidth for r in range(len(bars1))], ['Complications'])
plt.legend()
plt.title('Complication Rates by Treatment Group')
plt.show()
