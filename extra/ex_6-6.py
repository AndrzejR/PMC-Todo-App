filenames = ['doc.txt', 'report.txt', 'presentation.txt']
for name in filenames:
    file = open(name, 'w')
    file.write('Hello')
    file.close()

for to_read in filenames:
    file = open(to_read, 'r')
    content = file.read()
    print(content)