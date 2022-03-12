"""
We'll be using the pandas (short for panels of data) module to analyze a large dataset.
"""

"""
1. The conventional way to import the pandas module is below. Note that the "as pd" part is optional (but widely used).
import pandas as pd
"""
import pandas as pd

"""
2. This folder contains a large .csv (spreadsheet) file named ign.csv. Import the data stored in the csv as a dataframe to Python and store it in a variable. Try printing the data.
pd.read_csv('<filename/url>')
"""
data = pd.read_csv('ign.csv')
print("full data set:")
print(data)
print("\n")
"""
3. When you try to view the data on the console, you should notice that the row index appears twice. That's because if not specified, pandas will create it's own indices. In fact, when you look at the data, because it's so large, you can't even see the title of the game.

Change the dataframe so that the index are not integers starting from zero, but instead the title of the game. You'll have to go to the .csv file to find in which column the game titles are.
pd.read_csv('<filename/url>', index_col = <column number>)
"""
print("reordered data set w/ titles in front:")
reordered = pd.read_csv('ign.csv', index_col = 2)
print(reordered)
print("\n")
"""
4. Use <dataframe>.index and print the result to see a list of indices/row names. (Note: the console will not print all of them)
"""
print("list of rows:")
listofrows = reordered.index
print(listofrows)
print("\n")
"""
5. Use <dataframe>.columns and print the result to see a list of column names.
"""
print("list of columns:")
listofcolumns = reordered.columns
print(listofcolumns)
print("\n")
"""
6. In a pandas dataframe, columns are indexed by column name. For example, reviews['score_phrase'] returns a dataframe that contains only the index (the game title) and the score phrase given to that game.

Create a dataframe that only contains the score for each game. You can save it in a new dataframe variable, but you don't have to. Print that new dataframe.
"""
print("scores dataframe:")
onlyscore = reordered['score']
print(onlyscore)
print("\n")
"""
7. Use the following functions to find and print the indicated values based off score. Use the dataframe you created in #6.
<dataframe>.max()
<dataframe>.min()
<dataframe>.mean()
<dataframe>.median()
<dataframe>.std()  # standard deviation
"""
print("maximum value:")
print(onlyscore.max())
print("minimum value:")
print(onlyscore.min())
print("mean:")
print(onlyscore.mean())
print("median:")
print(onlyscore.median())
print("standard deviation:")
print(onlyscore.std())
print("\n")
"""
8. pandas has a function that returns a series indicating how many of each value is in a dataframe (<dataframe>.value_counts()). Use that function to find the counts in the platform, score, and release_month columns, and print the results. You will want to create 3 new dataframes that you can use value_counts() on.
"""
onlyplatform = reordered['platform']

onlyreleasemo = reordered['release_month']

countsplatform = (onlyplatform.value_counts())
countsscore = (onlyscore.value_counts())
countsreleasemo = (onlyreleasemo.value_counts())

print("platform counts:")
print(countsplatform)
print("score counts:")
print(countsscore)
print("release month counts:")
print(countsreleasemo)
print("\n")
"""
9. pandas supports Boolean indexing. For example, reviews[reviews['score'] < 1] would return a dataframe containing games that got a score below a 1.

Create 2 new dataframes, one with only games that got scores below 2, and one with only games that got scores of 10. Print both dataframes.
"""
print("scores below 2: ")
scoresbelow2 = reordered[reordered["score"]<2]
print(scoresbelow2)
print("\n")
print("scores equal to 10")
scoresequal10 = reordered[reordered["score"]==10]
print(scoresequal10)
"""
10. Save both the new dataframes you created in #9 to a csv file (it will make it much nicer to look at). Name the files 'trash.csv' and 'perfect.csv'
<dataframe>.to_csv('<filename>')
"""
scoresbelow2.to_csv("trash.csv")
scoresequal10.to_csv("perfect.csv")