from levels.models import User
#user = User(username=username, userKey=key)
#user.save()
def create_user(username, key):
    user = User(username=username, userKey=key)
    user.save()
    
def readCsv(filename):
        import csv
        rowsData = [] 
        with open(filename) as csvfile:
                readCSV = csv.reader(csvfile, delimiter=',')
                for row in readCSV:
                        #print(row)
                        rowsData.append(row)
        return rowsData
                        

