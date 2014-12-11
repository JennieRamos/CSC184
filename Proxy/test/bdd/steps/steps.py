from lettuce import *
from nose.tools import assert_equal
from proxy import *
from webtest import TestApp


@step(u'Given that I run the proxy.py')
def given_that_i_run_the_proxy_py(step):
    #os.system('python proxy.py')
    assert True
    
@step(u'When there are references')
def when_there_are_references(step):
     assert True

@step(u'Then I can see the number of references')
def then_i_can_see_the_references(step): 
    a = open('file','r')
    for row in step.hashes:
        x = a.readline().splitlines()
        assert_equal(x, row.values())

