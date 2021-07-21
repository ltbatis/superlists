from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith ouviu falar de uma nova aplicacao online interssante
        # para lista de tarefas. Ela decide verificar sua homepage
        self.browser.get('http://localhost:8000')
        
        # Ela percebe que o titulo da pagina e o cabeçalho mencionam listas
        # de tarefas (to-do) 
        self.assertIn('To-Do lists', self.browser.title)
        self.fail('Finish the test!')

        # Ela é convidada a inserir um item de tarefa imediatamente

        # Ela digita "Buy peacock feathers" (comprar pena de pavao) em uma caixa
        # de texto (o hobby de Edith é fazer iscas para pesca com fly)

        # Quando ela tecla Enter a tela é atualizada, e agora a pagina lista
        # "#1: Buy Peacock Feathers"

        # Ainda continua havendo uma caixa de texto convidando-a a acrescentar
        # outro item. Ela escreve "Use peacock feather to make a fly"

        # A pagina é atualizada novamente e agora mostram dois itens na lista

        # Edith se pergunta se o site lembrará de sua lista. Então ela nota que
        # o site gerou um URL unico para ela --  há um pequeno texto explicativo
        # para isso

        # Ela acessa esse URL e sua de tarefas lista continua lá

        # Satisfeita, ela volta dormir
        
if __name__ == '__main__':
    unittest.main(warnings='ignore')

    


    
    





