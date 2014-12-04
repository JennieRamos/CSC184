from lettuce import *
from nose.tools import assert_equal
from crawler.crawler import *
from webtest import TestApp

from crawler_app import app


@step(u'Given I input a url "([^"]*)"')
def given_i_input_a_url_group1(step, url):
    url_image = Url_imageGet(url)
    assert_equal(url_image.url ,url)

@step(u'When I run the crawler.py')
def when_i_run_the_crawler_py(step):
    assert True

@step(u'Then the images will be downloaded "([^"]*)"')
def then_the_images_will_be_downloaded_group1(step, images):
    images_path = os.path.isfile('/home/jennie/Documents/CSC184/singleton/crawler/images/' + images)
    assert_equal(images_path, True)



    
    



    



