#coding=utf-8

from nose.tools import *
from behave import *

@given(u'我输入加数{number}')
def step_impl(context, number):
    context.driver.find_element_by_name('TextField1').send_keys(number)

@given(u'我输入被加数{number}')
def step_impl(context, number):
    num2 = context.driver.find_element_by_name('TextField2')
    num2.send_keys(number)

@when(u'我点击"计算"按钮')
def step_impl(context):
    context.driver.find_element_by_accessibility_id('ComputeSumButton').click()

@then(u'我应该看到结果是{number}')
def step_impl(context, number):
    sum = context.driver.find_element_by_name('Answer').text
    eq_(number, sum)

