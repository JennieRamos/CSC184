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


         Scenario: Access using the ftp
         Given I visit the webpage 'ftp.freebsd.org'
         When I run the factory.py
         Then I can see the ff. "<files>"
         Examples:
               | files                             |
               |CERT                         |
               |CTM -> development/CTM   |
			   |CVSup -> development/CVSup|
               |ERRATA|
               |ISO-IMAGES-amd64 -> releases/amd64/amd64/ISO-IMAGES|
               |ISO-IMAGES-i386 -> releases/i386/i386/ISO-IMAGES|
               |ISO-IMAGES-ia64 -> releases/ia64/ia64/ISO-IMAGES|
               |ISO-IMAGES-pc98 -> releases/pc98/ISO-IMAGES|
               |ISO-IMAGES-powerpc -> releases/powerpc/powerpc/ISO-IMAGES|
               |ISO-IMAGES-powerpc64 -> releases/powerpc/powerpc64/ISO-IMAGES|
               |ISO-IMAGES-sparc64 -> releases/sparc64/sparc64/ISO-IMAGES|
               |README.TXT|
               |TIMESTAMP|
               |branches|
               |development|
               |dir.sizes|
               |distfiles -> ports/distfiles|
               |doc|
               |ports|
               |releases|
               |snapshots|
               |tools|
               |updates|

        

         
