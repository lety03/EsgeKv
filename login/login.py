from kivy.app import App
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.button import MDRoundFlatButton
from kivymd.uix.button import MDFillRoundFlatIconButton
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.clock import Clock, mainthread
import json


manager = ScreenManager()
# nomeProduto = ''
# qntProduto = ''
# qntIdeal = ''
#tela de login do usuario
class LoginWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.rows = 2
        self.subgrid = GridLayout()
        self.subgrid.size_hint_y = 0.5
        # self.subgrid.size_hint_min_x
        print("metodo init login: "+str(self.manager))
        self.add_widget(self.subgrid)
        pass
    def Acessar(self):
        
        nome = self.ids.nome.text
        senha = self.ids.senha.text
        print("metodo acessar antes: "+str(self.manager.current))
        if (nome == 'edna' and senha == '1234'):
            self.ids.msg.text += ", "+nome
            # manager.current = 'home'
            manager.switch_to(HomeWindow())
            print("metodo acessar: "+str(self.manager.current))
            pass
        else:
            self.ids.msg.text = 'Usuário ou senha inexistente'
        pass


#tela da home do app
class HomeWindow(Screen):
    # self.add_widget(Label(text="Bem vindo(a) ao ESGE", font_size='18sp')index=2)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)      
              
        # self.add_widget(self.ExibirProdutos(), len(self.children))
        # print(self)
        pass

    def ExibirAlterarProduto(self, instance):

        if(instance != ''):
            print(': chegou aqui'+str(instance.text))

    def ExibirProdutos(self):
        #Declarando layouts Grid e Scroll
        self.subscroll = ScrollView(do_scroll_y=True,bar_color=(.8, .7, .7, .9))
        self.subgrid = GridLayout(size_hint_y=None)
        self.subscroll.size_hint = ("0.3dp", 1)
        
        # Montando campo com os produtos
        # fruits = ["apple", "banana", "cherry","apple", "banana", "cherry","apple", "banana", "cherry", "banana", "cherry","apple", "banana", "cherry","apple", "banana", "cherry", "banana", "cherry","apple", "banana", "cherry","apple", "banana", "cherry", "banana", "cherry","apple", "banana", "cherry","apple", "banana", "cherry"]
        fruits = [["apple", 1, 4], ["banana",2,2], ["cherry",3,4],["apple", 4 , 6],[ "banana", 5 ,4], ["cherry",6,4],["apple", 7 , 6],[ "banana", 8 ,4], ["cherry",9,4],["apple", 10 , 6],[ "banana", 11 ,4], ["cherry",11,4],["apple", 12 , 6],[ "banana", 13 ,4], ["cherry",14,4],["apple", 15 , 6],[ "banana", 15 ,4], ["cherry",3,4],["apple", 5 , 6],[ "banana", 4 ,4]]
        self.cols = 1
        qntProdutos = len(fruits)
        self.subgrid.rows = qntProdutos
        self.subgrid.cols = 1
        # self.ExibirAlterarProduto("","","")
        # nomeProduto = ''
        # qntProduto = 0
        # qntIdeal = 0
        '''
        TENTANDO TRAZER DADOS DO CAMPO ALTERAÇÃO SELECIONADO PARA OUTRA FUNÇÃO
        '''
        # for x in fruits:
        #     nomeProduto = ''
        #     qntProduto = 0
        #     qntIdeal = 0
        #     nomeProduto = x[0]
        #     qntProduto = x[1]
        #     qntIdeal = x[2]           
        #     idProduto = 'id'+x[0]

        #     btnAlterar = MDRectangleFlatButton(text='', id=idProduto , on_press=LoginAlterarProdutoWindow(name='AlterarProduto').AlterarProduto, on_release=lambda x:Clock.schedule_once(lambda x:manager.switch_to(LoginAlterarProdutoWindow(name='AlterarProduto')), 3), font_size='10sp')        
        #     
        #     btnAlterar.subfloat = GridLayout()
        #     btnAlterar.subfloat.cols = 3
        #     btnAlterar.subfloat.add_widget(Label(text=nomeProduto,font_size='10sp',padding=(10, 10), size_hint_x=1))
        #     btnAlterar.subfloat.add_widget(Label(text=str(qntProduto),font_size='10sp',padding=(10, 10), size_hint_x=1))
        #     btnAlterar.subfloat.add_widget(Label(text=str(qntIdeal),font_size='10sp',padding=(10, 10), size_hint_x=1))
        #     btnAlterar.size_hint_x = 10
        #     btnAlterar.size_hint_y = None
        #     btnAlterar.size = '200dp','200dp'
        #     btnAlterar.add_widget(btnAlterar.subfloat)
            
        #     self.subgrid.add_widget(btnAlterar)

        # Retornando os layouts, a Grid fica dentro do Scroll 
        self.subgrid.bind(minimum_height = self.subgrid.setter("height"))
        self.subscroll.add_widget(self.subgrid)
        self.subscroll.size_hint_y =0.59
        self.subscroll.size_hint_x = 1
        self.subscroll.index = 3
        self.subscroll.pos = 0,0
        return self.subscroll

    



#tela de cadastro de produto
class CadastroProdutoWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.rows = 8
        self.subgrid = GridLayout()
        self.add_widget(self.subgrid)
        pass

    def DeletarWid(self):
        print(self.children[0])
        # manager.current = 'home'
        self.remove_widget(self.children[0])
        print(self.ids.nomeProduto.text)

#tela de alteração dos produtos
class LoginAlterarProdutoWindow(Screen, GridLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        scroll = self.ExibirItems()
        self.add_widget(scroll, len(self.children))
        # print('No init: '+str(self.children))
        

    def ExibirItems(self):
        self.scroll = ScrollView(always_overscroll=True,do_scroll_y=True,bar_color=(.8, .7, .7, .9))
        self.grid = GridLayout(size_hint_y=None)
        self.cols = 1
        self.scroll.size_hint = ("0.3dp", 1)
        fruits = [["apple", 1, 4], ["banana",2,2], ["cherry",3,4],["apple", 4 , 6],[ "banana", 5 ,4], ["cherry",6,4],["apple", 7 , 6],[ "banana", 8 ,4], ["cherry",9,4],["apple", 10 , 6],[ "banana", 11 ,4], ["cherry",11,4],["apple", 12 , 6],[ "banana", 13 ,4], ["cherry",14,4],["apple", 15 , 6],[ "banana", 15 ,4], ["cherry",3,4],["apple", 5 , 6],[ "banana", 4 ,4]]

        qntItem = len(fruits)      
        self.grid.cols  = 1
        self.grid.rows = qntItem
        
        for x in fruits:
            
            btnItem = MDRectangleFlatButton(text='' , on_press=self.ExibirAlterar)

            btnItem.gridBtn = GridLayout()
            btnItem.gridBtn.cols = 3
            btnItem.gridBtn.add_widget(Label(text=x[0],font_size='10sp',padding=(10, 10), size_hint_x=1))
            btnItem.gridBtn.add_widget(Label(text=str(x[1]), font_size='10sp',padding=(10, 10), size_hint_x=1))
            btnItem.gridBtn.add_widget(Label(text=str(x[2]), font_size='10sp',padding=(10, 10), size_hint_x=1))

            
            btnItem.size_hint_x = 1
            btnItem.size_hint_y = None
            btnItem.size = '100dp','100dp'

            btnItem.add_widget(btnItem.gridBtn)
            self.grid.add_widget(btnItem)

        self.grid.bind(minimum_height = self.grid.setter("height"))
        self.scroll.add_widget(self.grid)
        self.scroll.size_hint_y =1
        self.scroll.size_hint_x = 1
        self.scroll.pos = 0,0
        self.scroll.index = 1
        self.scroll.pos = 0,0
        return self.scroll
    
    def ExibirAlterar(self, instance):
        # Buscando os valores o item
        nomeAlt = instance.gridBtn.children[2].text
        qntItem = instance.gridBtn.children[1].text
        qntIdeal = instance.gridBtn.children[0].text

        # Limpando o layout
        self.clear_widgets()
        print(self.children)
        # print(self.children)

        # Adicionando o layout de alteração
        self.floatLy = FloatLayout()
        self.gridLy = GridLayout()
        self.gridLy.size_hint = .8, .8
        self.gridLy.cols = 1
        self.gridLy.rows = 8
        self.gridLy.add_widget(Label(text='Produto', size_hint_y=0.5))
        lbItem = TextInput(text=nomeAlt)
        lbItem.size_hint_y=None 
        lbItem.size = '50dp','30dp'
        self.gridLy.add_widget(lbItem)
        self.gridLy.add_widget(Label(text='Quantidade' , size_hint_y=0.5))
        lbAtual = TextInput(text=qntItem)
        lbAtual.size_hint_y=None 
        lbAtual.size = '50dp','30dp'
        self.gridLy.add_widget(lbAtual)
        self.gridLy.add_widget(Label(text='Quantidade Ideal', size_hint_y=0.5))
        lbIdeal = TextInput(text=qntIdeal)
        lbIdeal.size_hint_y=None 
        lbIdeal.size = '50dp','30dp'
        self.gridLy.add_widget(lbIdeal)
        btnSalvar = MDRectangleFlatButton(text='Salvar')
        btnHome = MDRectangleFlatButton(text='Voltar', on_press=lambda x:self.remove_widget(self.floatLy) , on_release=lambda x:self.__init__())
        btnSalvar.size_hint_x = 0.1
        btnSalvar.pos_hint = {'center_x': 0.5}
        btnHome.size_hint_x = 0.2
        btnHome.pos_hint = {'center_x': 0.5}
        self.gridLy.add_widget(btnSalvar)
        self.gridLy.add_widget(btnHome)
        self.gridLy.pos_hint =  {'center_x': 0.5, 'center_y': 0.5}
        self.gridLy.spacing = '10dp'
        self.floatLy.add_widget(self.gridLy)
        self.add_widget(self.floatLy)
        # return print(self.floatLy)
        

    def Excluir(self):
        # print(self.ids.labelTeste)
        # self.size_hint = 0,0
        # self.remove_widget(self.children[0])
        layouAlterar = self.children[0]
        layoutBtn = layouAlterar.children[0]
        print(layoutBtn)
        print(layoutBtn)
        # layoutBtn.size_hint = 1,1
        # self.add_widget(Button(text='voltar', on_press=self.ExibirAlterar, font_size='10sp')) 
        
        
class ExibirItems(RecycleView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        pass

#tela de busca de produtos
class BuscarProdutoWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        pass

class loginApp(MDApp):
    def build(self):
        # Crie a variavél/instanciar do screen manager
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = 'BlueGray'
        # manager.add_widget(HomeWindow(name='home'))
        manager.add_widget(LoginWindow(name='login'))
        manager.add_widget(HomeWindow(name='home'))
        
        manager.add_widget(LoginAlterarProdutoWindow(name='AlterarProduto'))
        
        manager.add_widget(CadastroProdutoWindow(name='CadastroProduto'))

        manager.add_widget(BuscarProdutoWindow(name='BuscarProduto'))

        return manager

    
if __name__=='__main__':
    loginApp().run()
        