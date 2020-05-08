def log(string):

    file = open('logs.txt', 'a+',encoding = 'utf-8')

    file.write(string)

    file.write("\n")
	
    file.close()


def logint(inte):

    file = open('logs.txt', 'ab+')

    file.write(inte)

    file.write("/n")

    file.close()
