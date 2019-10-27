import click
import teamtrees


@click.command(help="Get the amount of trees planted by TeamTrees!")
@click.option("-u", "--url", help="The link to TeamTrees website.", default="https://teamtrees.org/")
def teamtrees_(url):
    print(teamtrees.get_trees_count(url))


if __name__ == "__main__":
    teamtrees_()
