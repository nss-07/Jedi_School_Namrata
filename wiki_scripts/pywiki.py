import sys
import wikipedia


def search_wiki(search_key):
    print("Searching wikipedia for", search_key)

    possible_key = wikipedia.search(search_key)[0] or None
    try:
        search_url = wikipedia.page(possible_key).url
    except:
        try:
            final_key = wikipedia.suggest(possible_key)
            search_url = wikipedia.page(final_key).url
        except:
            print("Ambiguous search keyword, please retry!")
            sys.exit(1)

    print(search_url)
    with open("wiki_search_log.txt", 'a') as logfile:
        logfile.write(search_url + "\n")
        logfile.close()
    sys.exit(0)


if __name__ == '__main__':
    search_key = ' '

    if len(sys.argv) == 1:
        search_keyword = input("Search key? ")
    else:
        search_keyword = search_key.join(sys.argv[1:])

    search_wiki(search_keyword)
