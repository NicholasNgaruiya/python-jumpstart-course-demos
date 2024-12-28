import journal
# from journal import load,save,add_entry---style1
# from journal import * ---style2

def main():
    print_header()
    run_event_loop()


def print_header():
    print('------------------------------')
    print('         JOURNAL APP')
    print('------------------------------')


def run_event_loop():
    print('What do you want to do with your journal')
    cmd = 'EMPTY'
    journal_name = 'default'
    journal_data = journal.load(journal_name)
    while cmd != 'x' and cmd:
        cmd = input('[L]ist entries,[A]dd an entry,E[x]it: ')
        cmd = cmd.lower().strip()
        if cmd == 'l':
            list_entries(journal_data)

        elif cmd == 'a':
            add_entries(journal_data)
        elif cmd != 'x' and cmd:
            print("Sorry we don't understand '{}'.".format(cmd))

    print('Done Goodbye')
    journal.save(journal_name,journal_data)


def list_entries(data):
    print('Your journal entries:')
    entries = reversed(data)
    for idx,entry in enumerate(entries):
        print('*[{}] {}'.format(idx+1,entry))


def add_entries(data):
    text = input('Type your entry, <enter> to exit: ')
    journal.add_entry(text,data)
    # data.append(text)

#print("__file__ " + __file__) --full path to the actual file
#print("__name__" + __name__) --name of the file depending on caller

if __name__ == '__main__':
    main()