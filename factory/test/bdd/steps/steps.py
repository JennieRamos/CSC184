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
    #os.system('python factory.py')
    assert True

@step(u'Then the web resources is available "([^"]*)"')
def then_the_web_resources_is_available_group1(step, web_resources):
    web_resources_path = os.path.exists('/var/www/html')
    assert_equal(web_resources_path, True)

@step(u'Given I visit the webpage')
def given_i_visit_the_webpage(step):
    assert True

@step(u'Then I can see the ff. "([^"]*)"')
def then_i_can_see_the_ff_group1(step, files):
    files_path = os.path.exists('/home/jennie/Documents/CSC184/factory/')
    assert_equal(files_path, True)




