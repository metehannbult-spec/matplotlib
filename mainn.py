import matplotlib.pyplot as plt
goal_types = 'penaltı','kaleye atılan şut','serbest vuruş'
goals = [12,35,7]
colors = ['y','r','b']
plt.pie(goals,labels=goal_types,colors=colors)
plt.show()