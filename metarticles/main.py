from py2neo import neo4j

from clients.cli.cli import MetArticlesCLI
import db_operations

VERSION = 0
MINOR_VERSION = 0
REVISION = 1

VERSION_NUMBER = str(VERSION) + "." + str(MINOR_VERSION) + "." + str(REVISION)

def main():
    db_operations.initialise()
    db_operations.connect_to_database()
    interpreter = MetArticlesCLI()
    interpreter.prompt="MetArticles> "
    interpreter.cmdloop("Welcome to MetArticles v" + VERSION_NUMBER)


if __name__ == '__main__':
    main()