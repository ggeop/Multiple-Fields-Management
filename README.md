This repo presents an idea of fields management from/to different data sources.

# Requirements :triangular_ruler:
* Python 3.8.x (Tested in Python 3.8.5)
* Python Pandas

# Target Audience :loudspeaker:
* Data Engineers
* Data Scientists
* Data Analysts
* Software Engineers

# Problem :confused:
A very common headache in data processing from multiple sources is the managment of column names.
In a nutshell, few problems are:

* **Lack of naming convention**: Column names are not following the same convention or any convention at all.
* **Unefficient refactoring**: Hardcoded strings are all over the project. In refactoring, its possible to forgot to update something.
* **Column dublications**: Column names are not in the same place, so its possible the user will use similar column names for the same thing.

# Solution :ok_hand:
Organize all the fields (column names) in a cetral place by using a Python object (class).
The benefits from this strategy is the elimination of the above problems and much more (e.g adds fields logic)!!
A Python class gives the ability to use methods and also bound other metadata with fields (e.g type).

## An example :yum:
Below there is a simple example, but you can find more code examples in `examples.ipynb` Notebook

Let's say that we have a pandas dataframe with one column.

```{python}
input_df = pd.DataFrame({'dummy_column_1': [1,2,3,4]})
```
Output:
```
+----+----------------+
|    | dummy_column_1 |
|----+----------------|
|  0 |              1 |
|  1 |              2 |
|  2 |              3 |
|  3 |              4 |
+----+----------------+
```

Now, we want to create a new column `dummy_column_2`. The first step, is to create a new entity in `Field` class. For example:
```
dummy_field_2 = field(input_name='dummy_column_2', exported_name='Dummy Column 2')
```

Then we can use the new field in our dataframe.

```{python}
import Field
df[Fields.dummy_field_2.input_name] = 2
```
Output:
```
+----+----------------+------------------+
|    | dummy_column_1 |   dummy_column_2 |
|----+----------------+------------------|
|  0 |              1 |                2 |
|  1 |              2 |                2 |
|  2 |              3 |                2 |
|  3 |              4 |                2 |
+----+----------------+------------------+
```

Then at the end, after we have finished with the processing steps, we can rename the fields before we export the dataframe by leveraging field functions.


```{python}
field_renames = Field.get_renames()
df = df.rename(columns={field: field_renames[field] for field in input_df.columns})
```
Output:
```
+----+----------------+------------------+
|    |   Dummy Column |   Dummy Column 2 | <---- New column names
|----+----------------+------------------|
|  0 |              1 |                2 |
|  1 |              2 |                2 |
|  2 |              3 |                2 |
|  3 |              4 |                2 |
+----+----------------+------------------+
```

----

# Contributing
* Pull Requests (PRs) are welcome ☺️!

# Thanks!
Thanks for your time! This repo is just an idea, the above logic can be expanded and change the way you handle multiple data sources! Cheers :beers: