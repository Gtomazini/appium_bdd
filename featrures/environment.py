'''
    before_scenario() - Antes de começar qualquer cenário ele vai iniciar o servidor do appium

    after_scenario() - Após a execução de todos os testes ele vai fechar o servidor do appium
'''
def before_scenario(context, scenario):
    context.driver.start_driver()

def after_scenario(context, scenario):
    context.driver.driver_quit()