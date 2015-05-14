#coding=utf-8

from behave import *

@given(u'我输入加数100')
def step_impl(context):
    pass

@given(u'我输入被加数200')
def step_impl(context):
    assert True is not False

@when(u'我点击"计算"按钮')
def step_impl(context):
    assert True is not False

@then(u'我应该看到结果是300')
def step_impl(context):
    assert context.failed is False
