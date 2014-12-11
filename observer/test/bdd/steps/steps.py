from lettuce import *
from nose.tools import assert_equal
from observer import *
from webtest import TestApp

@step(u'Given that I run the observer.py')
def given_that_i_run_the_observer_py(step):
    assert True

@step(u'When register as an "([^"]*)" to that subject')
def when_register_as_an_group1_to_that_subject(step, observer):
	subject = Subject()
	observer = USATimeObserver('usa_time_observer')
	subject.register_observer(observer)

@step(u'When I get the 24hr and 12hr time')
def when_i_get_the_24hr_and_12hr_time(step):
    subject = Subject()
    observer = USATimeObserver('')
    subject.unregister_observer(observer)

@step(u'Then there will be a record of time')
def then_there_will_be_a_record_of_time(step):
    notify = os.path.isfile('/home/jennie/Documents/CSC184/observer/')
    #assert(notify, True)
    a = open('file','r')
    for row in step.hashes:
        x = a.readline().splitlines()
        assert_equal(x, row.values())












