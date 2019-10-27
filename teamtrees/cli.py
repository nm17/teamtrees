import click
import teamtrees
import io


@click.command(help="Get the amount of trees planted by TeamTrees!")
@click.option(
    "-u",
    "--url",
    help="The link to TeamTrees website.",
    default="https://teamtrees.org/",
)
@click.option("--top", help="Get top donations in csv format", is_flag=True)
@click.option("--recent", help="Get recent donations in csv format", is_flag=True)
def teamtrees_(url, top, recent):
    if top is True and not recent:
        strio = io.StringIO()
        teamtrees.get_top_donations(url).to_csv(strio)
        strio.seek(0)
        print(strio.read())
        exit()
    if recent is True and not top:
        strio = io.StringIO()
        teamtrees.get_recent_donations(url).to_csv(strio)
        strio.seek(0)
        print(strio.read())
        exit()
    print(teamtrees.get_trees_count(url))


if __name__ == "__main__":
    teamtrees_()
