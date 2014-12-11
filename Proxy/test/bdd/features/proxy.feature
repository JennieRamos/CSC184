Feature: An application that would count of how many references

         As a user, I want to count how many references

        Scenario: the  number of references
        Given that I run the proxy.py
        When there are references
        Then I can see the number of references
        |references|
        |Created new object|
        |Count of references =  1|
		|Using cached object|
		|Count of references =  2|
		|Using cached object|
		|Count of references =  3|
		|Called sort method with args:|
		|[('self', <__main__.Proxy object at 0x7f5027830250>), ('reverse', True)]|
		|Deleting proxy2|
		|Deleted object. Count of objects =  2|
		|The other objects are deleted upon program termination|
		||Deleted object. Count of objects =  1|
		|Number of reference_count is 0. Deleting cached object...|
		|Deleted object. Count of objects =  0|
