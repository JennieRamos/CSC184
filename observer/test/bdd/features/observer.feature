Feature: An application to subscribe or unsubscribe

        Scenario: subscribe
        Given that an observer
        When register as an "<observer>" to that subject
        When unregister as an "<observer>"
        Then it will be a subscriber to that object can see "<notify>"
        |notify|
        |Adding usa_time_observer|
        |Observer usa_time_observer says: 2014-12-11 08:26:34AM|
		|Adding eu_time_observer|
		|Observer usa_time_observer says: 2014-12-11 08:26:36AM|
		|Observer eu_time_observer says: 2014-12-11 08:26:36|
		|Removing usa_time_observer|
		|Observer eu_time_observer says: 2014-12-11 08:26:38|


        