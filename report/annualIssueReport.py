from github import Github
from annualReport import AnnualReport
import csv
import logging


class AnnualIssueReport(AnnualReport):

    def getIssues(self, repo):
        '''
        get all the issues from repo
        '''

        issues = repo.get_issues(state='all')
        
        return issues

    def fileHeader(self):
        '''
        return file header
        '''
        return ['repo_name','repo_url','issue','issue_url','date_created','date_closed']


    def generateSummarizeReport(self, openInMonth: list, closedInMonth: int):

        fileName = self.reportName('summarize.txt')
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov','Dec']

        with open(fileName, 'w+') as f:

            f.write('Issues Opened In:\n')

            for month,count in zip(months,closedInMonth):
                f.write(month +": "+str(count)+'\n')

            f.write('Issues closed In:\n')
            
            for month,count in zip(months,openInMonth):
                f.write(month +": "+str(count)+'\n')
      

    def generateReport(self):
        '''
        generate repo
        '''
        fileName = self.reportName('details.csv')

        writer = csv.writer(open(fileName, 'w+'))

        writer.writerow(self.fileHeader())

        openInMonth = [0] * 12 
        closedInMonth = [0] * 12 


        count = 0

        for repo in self.repos:
            repoName = repo.name
            repoUrl = repo.html_url

            issues = self.getIssues(repo)

            for issue in issues:
                issueTitle = str(issue.title) 
                issueUrl =  str(issue.html_url) 
                startDate = str(issue.created_at)
                endDate = str(issue.closed_at) if issue.closed_at else ""

                if self.filterbyYear(startDate, endDate, self.year):
                    count += 1
                    writer.writerow([repoName, repoUrl, issueTitle, issueUrl, startDate, endDate])

                    openInMonth[self.getMonth(startDate)] += 1

                    if endDate:
                        closedInMonth[self.getMonth(endDate)] += 1


        self.generateSummarizeReport(openInMonth,closedInMonth)


        logging.debug('{} data inserted'.format(count))

