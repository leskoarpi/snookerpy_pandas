import pandas as pd
#2
df = pd.read_csv('snooker.txt',encoding='latin2',sep=';')
#3
print(f'3. feladat: A világranglistán {df["Nev"].count()} versenyző szerepel')
#4
print(f'4. feladat: A versenyzők átlagosan {"%.2f" % df["Nyeremeny"].mean()} fontot kerestek.')
#5
print('5. feladat: A legjobban kereső kínai versenyző:')
for index in df.index:
    if df["Nyeremeny"][index] == df[df["Orszag"]=="Kína"].max()["Nyeremeny"]:
        print(f'\tHelyezés: {df["Helyezes"][index]}')
        print(f'\tNév: {df["Nev"][index]}')
        print(f'\tOrszag: {df["Orszag"][index]}')
        print(f'\tNyeremény: {df["Nyeremeny"][index] * 380}')
#6
if "Norvégia" in df['Orszag'].values:
    print('6. feladat: A versenyzők közt van norvég versenyző')
#7
df2 = df['Orszag'].value_counts()
print('7. feladat: Statisztika')
for i in df2.index:
    if df2[i] > 4:
        print(f'\t {i} - {df2[i]} fő')
