
# from tkinter.ttk import Style
import seaborn as sns
import matplotlib.pyplot as plt
# sns.set_theme(Style="ticks", color_codes=True )
titanic = sns.load_dataset("titanic")
p1=sns.countplot(x='sex',data=titanic,hue='class')
p1
plt.title("plot for class")
plt.show()

# # import libraries
# import seaborn as sns
# # import numpy
# import matplotlib.pyplot as plt
# p1 = sns.load_dataset("titanic")
# p1
# # draw a lineplot
# sns.barplot(x="class",y="fare", hue= "sex",data=p1,ci=None, saturation=0.5)
# # set title
# plt.title("Big Boat")
# plt.show()