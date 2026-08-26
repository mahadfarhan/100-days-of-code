import pandas

data = pandas.read_csv(
    "./squirrel central analysis/2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20260825.csv"
)

# Get counts of all different fur colours

unique_types = data["Primary Fur Color"].dropna().unique()
fur_dict = {"Fur Color": [], "Count": []}
for fur_type in unique_types:
    count_of_fur = int((data["Primary Fur Color"] == fur_type).sum())
    fur_dict["Fur Color"].append(fur_type)
    fur_dict["Count"].append(count_of_fur)

fur_dataframe = pandas.DataFrame(fur_dict)
fur_dataframe.to_csv("./squirrel central analysis/squirrel_count.csv")

# Alternate method

# fur_colors = data["Primary Fur Color"].value_counts()
# fur_colors.rename_axis("Fur Color", inplace=True)
# fur_dataframe = fur_colors.reset_index(name="Count")
# fur_dataframe.to_csv("./squirrel central analysis/squirrel_count.csv")
