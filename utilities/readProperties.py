import configparser

config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")              ## Read data from config.ini file


class Readconfig:                        ## all url,username,passward so evry method create function/method
    @staticmethod
    def getApplicationURL():
        url = config.get('common info','baseurl')
        return url

    @staticmethod
    def getUseremail():
        username = config.get('common info','useremail')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info','password')
        return password