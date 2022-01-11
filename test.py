from report import annualIssueReport
import unittest
from github import Github
from datetime import date
import pathlib as pl


class TestAnnualIssueReport(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestAnnualIssueReport, self).__init__(*args, **kwargs)
        self.g = Github()


    def test_get_username(self):
        '''
        test the userName setter
   
        '''

        userName = 'sfsf9797'
        annualReport = annualIssueReport.AnnualIssueReport(userName,self.g, 2020)
        self.assertEqual(userName, annualReport.userName)

    def test_filterbyYear(self):
        '''
        test the filterbyYear function
        '''

        startDate = '2021-04-05'
        endDate = '2021-05-05'
        year = '2021'

        self.assertTrue(annualIssueReport.AnnualIssueReport.filterbyYear(startDate,endDate,year))

    def test_filterbyYear2(self):
        '''
        test the filterbyYear function
        '''

        startDate = '2021-04-05'
        endDate = '2021-05-05'
        year = '2019'

        self.assertFalse(annualIssueReport.AnnualIssueReport.filterbyYear(startDate,endDate,year))

    def test_filterbyYear3(self):
        '''
        test the filterbyYear function
        '''

        startDate = '2019-04-05'
        endDate = '2021-05-05'
        year = '2019'

        self.assertTrue(annualIssueReport.AnnualIssueReport.filterbyYear(startDate,endDate,year))

    def test_generateReport(self):

        userName ='sfsf9797'
        year = '2019'
        basePath = './test_output'

        annualReport = annualIssueReport.AnnualIssueReport(userName,self.g, year)

        annualReport.basePath = basePath

        annualReport.generateReport()

        tdy = date.today()
        tdy = tdy.strftime("%d-%m-%Y")
         

        
        fileName = tdy+'_AnnualIssueReport_'+year+'_details.csv'

        path = pl.Path(basePath + '/' + fileName)
        self.assertEquals((str(path), path.is_file()), (str(path), True))





if __name__ == '__main__':
    unittest.main()
         

