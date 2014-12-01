from lettuce import *
from nose.tools import assert_equal
from crawler.crawler import *
from webtest import TestApp

from crawler_app import app


@step(u'Given I input a url "([^"]*)"')
def given_i_input_a_url_group1(step, url):
    url_image = Url_imageGet(url)
    assert_equal(url_image.url ,url)



