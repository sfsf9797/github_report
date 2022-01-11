from report import annualIssueReport
from github import Github
import argparse

if __name__ == '__main__':
    # Create the parser
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', type=str, required=True)
    parser.add_argument('--year', type=str, nargs='?', default=2021)
    parser.add_argument('--accessToken', type=str, nargs='?', default=None)


    # Parse the argument
    args = parser.parse_args()

    githubArgs = {'login_or_token':args.accessToken}

    g = Github(**githubArgs)

    annualIssueReport1 = annualIssueReport.AnnualIssueReport(args.name,g,args.year)
    annualIssueReport1.generateReport()