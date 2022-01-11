from abc import ABC, abstractmethod
from github import Github 
import logging


logging.basicConfig(filename='logger.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')



class Report(ABC):
    '''
    abstract class for repo
    '''
        

    @abstractmethod
    def fileHeader(self):
        '''
        return file header
        '''
        pass 

    @abstractmethod
    def generateReport(self):
        '''
        abstract method to generate report
        '''
        pass 

class GithubReport(Report):
    '''
    abstract class for github repo
    '''

    def __init__(self, userName: str, githubApi: Github):
        self.g = githubApi
        self.userName = userName
        self.basePath = './output'

    @property
    def userName(self):
        return self._userName 

    @userName.setter
    def userName(self, userName):
        '''
        set up github userName and repos
        '''
        try:
            user = self.g.get_user(userName)
            self._userName = userName
            self.repos = user.get_repos()
        except Exception as e:
            logging.exception(e)
            raise e

            

    def fileHeader(self):
        '''
        return file header
        '''
        pass 

    def generateReport(self):
        '''
        abstract method to generate report
        '''
        pass 




    
