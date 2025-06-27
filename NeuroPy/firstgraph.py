from NeuroCurveImports import *
print(NeuroCurveOG.info())
print(NeuroCurveOG.describe())
#print(NeuroCurveOG['BMI'].sum())
histo = plt.hist(NeuroCurveOG['Diagnosis'])
#plt.ylim((0,10))
plt.show()
print(NeuroCurveOG['Diagnosis'].mean())