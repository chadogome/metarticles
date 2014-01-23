from peewee import SqliteDatabase

from clients.cli.cli import MetArticlesCLI

VERSION = 0
MINOR_VERSION = 0
REVISION = 1

VERSION_NUMBER = str(VERSION) + "." + str(MINOR_VERSION) + "." + str(REVISION)

def connectToDatabase(name):
    try:
        database = SqliteDatabase(name)
        database.connect()
    except(Exception):
        print("Error connecting to database " + name)

def main():
    connectToDatabase('../data/concepts.db')
    interpreter = MetArticlesCLI()
    interpreter.prompt="MetArticles> "
    interpreter.cmdloop("Welcome to MetArticles v" + VERSION_NUMBER)


if __name__ == '__main__':
    main()