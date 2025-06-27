from NeuroCurveImports import *
print(NeuroCurveOG.info())
print(NeuroCurveOG.describe())
print(NeuroCurveOG.shape)
'''for i in NeuroCurveOG.columns:
    print(NeuroCurveOG[f'{i}'].isna().sum())'''
histo = plt.hist(NeuroCurveOG['Diagnosis'])
#plt.ylim((0,10))
plt.show()
print(NeuroCurveOG['Diagnosis'].mean(),NeuroCurveOG['Diagnosis'].median())