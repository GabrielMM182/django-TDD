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

    def test_buscando_novo_animal(self):
        """Teste de um usuario encontra um animal pesquisando"""

        # Gabriel, deseja encontrar um novo animal, para adotar
        # Gabriel encontra o buscarAnimal e descide usar então vê no menu do site escrito Busca Animal.
        home_page = self.browser.get(self.live_server_url + '/')
        brand_element = self.browser.find_element_by_css_selector('.navbar')
        self.assertEqual('Busca Animal', brand_element.text)

        # Gabriel vê um campo para pesquisar animal pelo nome e então pesquisa pelo animal leão no input
        buscar_animal_input = self.browser.find_element_by_css_selector('input#buscar-animal')
        self.assertEqual(buscar_animal_input.get_attribute('placeholder'), 'Exemplo:leão')

        # Gabriel pesquisa pelo animal leão e clica no botão pesquisar em form
        buscar_animal_input.send_keys('leão')
        self.browser.find_element_by_css_selector('form button').click()

        # O site acaba exbindo 4 caracteristicas do animal pesquisado (usando elements pois vai ser mais de uma caracteristica)
        caracteristicas = self.browser.find_elements_by_css_selector('.result-description')
        self.assertGreater(len(caracteristicas), 3)

        # Gabriel acaba desistindo de adota um leão
        
