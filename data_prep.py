import pandas as pd

df = pd.read_csv('case_names.csv', header = None)

df = df.rename(index=str, columns={0:'case_name'})

df[df['case_name'].str.contains('"')].count()

df['case_name'] = df['case_name'].replace(regex=True, to_replace=r'\"', value=r'')

df[df['case_name'].str.contains('"')].count()

df[~df['case_name'].str.contains(' v. ')].count()

df_1 = df.drop(df[~df['case_name'].str.contains(' v. ')].index)

new_df = df_1['case_name'].str.split(' v. ', n = 1, expand = True)

df_1['petitioner'] = new_df[0]
df_1['respondent'] = new_df[1]

petitioners = []
respondents = []

df_1['petitioner'].apply(lambda x: petitioners.append(x))
df_1['respondent'].apply(lambda x: respondents.append(x))

petitioners_string = ""

for petitioner in petitioners:
    petitioners_string = petitioners_string + " " + petitioner

respondents_string = ""

for respondent in respondents:
    respondents_string = respondents_string + " " + respondent

petitioners_string = petitioners_string[1:]
respondents_string = respondents_string[1:]

with open('petitioners.txt', 'w') as f:
    f.write(petitioners_string)

with open('respondents.txt', 'w') as f:
    f.write(respondents_string)
