Feature: An application that download images

         As a user I wish to download images

         Scenario: Download image
         Given I input a url "http://localhost/pic.html"
         When I see an image in the url
         Then the will be downloaded
         
         
