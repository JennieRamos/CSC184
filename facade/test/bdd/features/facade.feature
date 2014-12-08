Feature: An application that can get a temperature

         As a user, I want to get the temperature in London

         Scenario: Get the temperature
         Given that I can access the website 'http://api.openweathermap.org/data/2.5/forecast?q={},{}'
         When I run the facade.py
         Then I can get the cache with temperature in the 'myfile'
         Examples:
              | myfile |
              | 3.58   |
        

         
