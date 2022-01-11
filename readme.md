# Github Report
<div id="top"></div>
<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>

  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Github report is a project to generate a report about repos, issue created, issues closed in a given year.


### Built With



* [python](https://www.python.org)
* [docker](https://www.docker.com/)





<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running please follow these simple example steps.

### Prerequisites

A list things you need to install to use the software.

  ```sh
    docker v1.10 or above
    docker-compose v1.6.0 or above
    
    docker-compose -f "docker-compose.yml" up -d --build
   
  ```
  
### Installation


1.build the containers
   ```sh
   docker-compose -f "docker-compose.yml" up -d --build
   ```


<!-- USAGE EXAMPLES -->
## Usage

1.You could generate the report by running the following command
   ```sh
    docker-compose run  githubreport python  ./main.py --name sfsf97
    
    #name is the parameter for github user name
   ```
  or
           
    docker-compose run  githubreport python  ./main.py --name sfsf97    --accessToken mytoken --year 2019    

Where
accessToken is an optional parameter that can increase the rate limit.

All the report would be stored in the output folder.

2. To run unit tests
   ```sh
    docker-compose run --no-deps githubreport python  ./test.py 
    
   ```

## Design Choice
1. First, I need a program to call GitHub API for all the data. PyGithub library ([https://github.com/PyGithub/PyGithub](https://github.com/PyGithub/PyGithub)) provides me with all the functionalities I need or I might need in the future.
2. A transform and load pipeline which I can write in Python. Proposed to use CSV as the output format as It can be loaded into the database easily and also supported by Pandas for further analysis.
3. SOLID design principles for code maintainability and readability.
4. Enable the function to take input from CLI.
5. include logging for debug purpose.
6. Docker for easy deployment across different platforms.

    
<p align="right">(<a href="#top">back to top</a>)</p>