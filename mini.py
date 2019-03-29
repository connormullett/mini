
import click


@click.command()
@click.argument('f')
def mini(f):
    click.echo('making %s' % f)


if __name__ == '__main__':
    mini()

