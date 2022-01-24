from django.test import LiveServerTestCase
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class AnimaisTestCase(LiveServerTestCase):

    # abre o google chrome para teste (precisa desse nome em específico setUp e desse caminho em específico para funcionar)
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    # fecha o google chrome (precisa desse nome em específico tearDown)
    def tearDown(self):
        self.browser.quit()

    # abre uma janela em branco de teste 
    def test_abre_janela(self):
        self.browser.get(self.live_server_url)

    # um test que vai falhar para teste
    def test_deu_ruim(self):
        """teste de exemplo de erro"""
        self.fail('teste deu ruim')