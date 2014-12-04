Feature: An application that download images

         As a user I wish to download images

         Scenario: Download image
         Given I input a url "http://localhost/pic.html"
         When I run the crawler.py
         Then the images will be downloaded "<images>"
         Examples:
              | images    |
              | diofel.jpg|
              | kay.jpg   |
              | onna.jpg  |
              | ron.jpg   |
         
         
         
