Feature: An application to subscribe or unsubscribe

        As a user I want to see the time of sunscribe and unsubscribe

        Scenario: subscribe and unsubscribe
        Given that I run the observer.py
        When I get the 24hr and 12hr time
        Then there will be a record of time
        |time|
        |Adding usa_time_observer|
        |Observer usa_time_observer says: 2014-12-11 08:26:34AM|
		|Adding eu_time_observer|
		|Observer usa_time_observer says: 2014-12-11 08:26:36AM|
		|Observer eu_time_observer says: 2014-12-11 08:26:36|
		|Removing usa_time_observer|
		|Observer eu_time_observer says: 2014-12-11 08:26:38|


        