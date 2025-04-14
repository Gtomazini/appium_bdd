import os
from support.capabilities import capabilities
from appium.options.android import UiAutomator2Options
from appium import webdriver
'''
    before_scenario() - Antes de começar qualquer cenário ele vai iniciar o servidor do appium

    after_scenario() - Após a execução de todos os testes ele vai fechar o servidor do appium

    base: https://github.com/serhatbolsu/appium-python-bdd/blob/master/features/environment.py
'''

def before_scenario(context, scenario):
    options = UiAutomator2Options()
    options.load_capabilities(capabilities)
    
    appium_server_url = 'http://localhost:4723'
    context.driver = webdriver.Remote(appium_server_url, options=options)

def after_scenario(context, scenario):
    context.driver.quit()