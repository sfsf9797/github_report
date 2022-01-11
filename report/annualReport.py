from  githubReport import GithubReport
from github import Github 
from datetime import date
import os 

class AnnualReport(GithubReport):

    def __init__(self, userName: str, githubApi: Github, year: int) -> None:
        super().__init__(userName, githubApi)
        self.year = str(year)

    def reportName(self, fileName: str):
        '''
        return fileName

        parameters
        ---------
        type: report type
        '''
        tdy = date.today()
        tdy = tdy.strftime("%d-%m-%Y")
        fileName = tdy+'_'+self.__class__.__name__+'_'+self.year + '_'+fileName

        return os.path.join(self.basePath,fileName)
    
    @staticmethod
    def filterbyYear(startDate: str, endDate: str, year: str):
        '''
        return True if either startDate or endDate is in the targeted year

        '''

        startYear = startDate.split('-')[0]
        endYear = endDate.split('-')[0] if endDate else '' #in some case, end date is None

        return startYear == year or endYear == year 

    @staticmethod
    def getMonth(date: str):
        '''
        return the month from the date
        '''

        month = int(date.split('-')[1]) - 1

        return month 


    def fileHeader(self):
        pass

    def generateReport(self):
        pass

 


                

        
