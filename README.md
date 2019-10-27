# teamtrees
Get the amount of trees planted by TeamTrees!

## How to install
```sh
$ pip install teamtrees
```

## Usage
You can either use the cli `teamtrees`: 
```sh
$ teamtrees --recent >> recent_donations.csv
$ teamtrees --top >> top_donations.csv
$ teamtrees # Get current amount of trees planted
```

Or through Python:
```python
import teamtrees

print(teamtrees.get_trees_count())
```
