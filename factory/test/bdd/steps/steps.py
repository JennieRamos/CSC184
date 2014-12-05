from lettuce import *
from nose.tools import assert_equal
from factory import *
from webtest import TestApp

@step(u'Given I use the domain "([^"]*)"')
def given_i_use_the_domain_group1(step, domain):
    given_domain = Domain(domain)
    assert_equal(given_domain.domain ,domain)

@step(u'When I run the factory.py')
def when_i_run_the_factory_py(step):
    assert True

@step(u'Then the web resources is available "([^"]*)"')
def then_the_web_resources_is_available_group1(step, group1):
    assert True
