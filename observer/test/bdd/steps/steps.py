from lettuce import *
from nose.tools import assert_equal
from observer import *
from webtest import TestApp

@step(u'Given that an observer')
def given_that_an_observer(step):
	subject = Subject()

@step(u'When register as an "([^"]*)" to that subject')
def when_register_as_an_group1_to_that_subject(step, observer):
	subject = Subject()
	observer = USATimeObserver('usa_time_observer')
	subject.register_observer(observer)

@step(u'When unregister as an "([^"]*)"')
def when_unregister_as_an_group1(step, observer):
    subject = Subject()
    observer = USATimeObserver('jen')
    subject.unregister_observer(observer)

@step(u'Then it will be a subscriber to that object can see "([^"]*)"')
def then_it_will_be_a_subscriber_to_that_object_can_see_group1(step, notify):
    notify = os.path.isfile('/home/jennie/Documents/CSC184/observer/')
    assert(notify, True)











