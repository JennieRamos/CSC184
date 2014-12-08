from lettuce import *
from nose.tools import assert_equal
from facade import *
from webtest import TestApp


@step(u'Given that I can access the website \'([^\']*)\'')
def given_that_i_can_access_the_website_group1(step, website):
    given_website = Website(website)
    assert_equal(given_website.website ,website)

@step(u'When I run the facade.py')
def when_i_run_the_facade_py(step):
    os.system('python facade.py')

@step(u'Then I can get the cache with temperature in the \'([^\']*)\'')
def then_i_can_get_the_cache_with_temperature_in_the_group1(step, myfile):
    cache_path = os.path.isfile('/home/jennie/Documents/CSC184/facade/' + myfile)
    assert_equal(cache_path, True)

