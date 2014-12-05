Feature: An application who access a web resources

         As a user, I want to access the  web resources

         Scenario: Access the web resources
         Given I use the domain "localhost"
         When I run the factory.py
         Then the web resources is available "<web_resources>"
         Examples:
               |   web-resources   |
               |http://google.com  |
               |http://facebook.com|

         
