#### Single Responsability Principle (or Separation of Concerns)

#### Anti-Pattern: God Object. Contains too much responsabilities
# i.e: the save(), load(), download() methods might be used for several
# other classe. So, insted of adding these methods to every single class that
# requires it (which breaks DRY), we should make an abstraction of them.


class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')
    
    def remove_entry(self, pos):
        del self.entries[pos]
    
    def __str__(self):
        return '\n'.join(self.entries)


class PersistanceManager:
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()

    # def load(self, filename):
    #     pass

    # def download_from_web(self, uri):
    #     pass

if __name__ == "__main__":
    j = Journal()
    j.add_entry("I coded my first solid principle")
    j.add_entry("I created the github repo")
    # print(f'Journal entries:\n{j}')

    file = 'journal.txt'
    PersistanceManager.save_to_file(j, file)

    with open(file) as f:
        print(f.read())
