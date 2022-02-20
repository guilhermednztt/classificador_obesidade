import streamlit as st
from functions import ClassificadorObesidade

class InterfaceClassificador:

    def __init__(self):
        st.set_page_config(page_title="Classificador de Obesidade")
        self.funcoes = ClassificadorObesidade()

    def questionario(self):
        alimentos_caloricos = st.sidebar.selectbox("Frequentemente consome alimentos de grandes calorias?", ["Não", "Sim"])
        consumo_vegetais = st.sidebar.selectbox("Com que frequência consome vegetais?", ["Sempre", "Às vezes", "Nunca"])
        refeicoes_principais = st.sidebar.selectbox("Quantas refeições principais por dia?", ["Entre 1 e 2", "3 refeições", "Mais que 3"])
        comida_entre_refeicoes = st.sidebar.selectbox("Você consome qualquer comida entre as refeições principais?", ["Não", "Às vezes", "Frequentemente", "Nunca"])
        agua_por_dia = st.sidebar.selectbox("Como está seu consumo de água por dia?", ["Menos de 1L", "Entre 1L e 2L", "Mais de 2L"])
        consumo_de_alcool = st.sidebar.selectbox("Sobre o consumo de bebidas alcoólicas: ", ["Não bebo", "Às vezes", "Frequentemente", "Sempre"])
        fumante = st.sidebar.selectbox("Você fuma?", ["Não", "Sim"])
        monitoramento_de_calorias = st.sidebar.selectbox("Tem  costume de monitorar o consumo diário de calorias?", ["Sim", "Não"])
        obesidade_na_familia = st.sidebar.selectbox("Existe casos de obesidade em sua família?", ["Não", "Sim"])
        atividades_fisicas = st.sidebar.selectbox("Com que frequência faz atividades físicas na semana", ["Não faço", "1 ou 2 dias", "3 ou 4 dias", "5 dias ou mais"])
        tempo_em_dipositivos = st.sidebar.selectbox("Qual é o tempo que você fica com dispositivos digitais?", ["De 0 a 2 horas", "De 3 a 5 horas", "Mais de 5 horas"])
        meio_de_transporte = st.sidebar.selectbox("Qual meio de transporte você geralmente usa?", ["Carro", "Moto", "Bicicleta", "Transporte público", "Caminhada"])
        genero = st.sidebar.selectbox("Seu gênero: ", ["Feminino", "Masculino"])
        idade = st.sidebar.number_input("Idade: ", step=1, value=21, min_value=0, max_value=110)
        altura = st.sidebar.number_input("Altura (em metros): ", step=0.01, value=1.78, min_value=0.01)
        peso = st.sidebar.number_input("Peso (em kg): ", step=0.01, value=57.80, min_value=0.01)

        respostas_da_pessoa = [
            genero, idade, altura, float(peso), obesidade_na_familia, alimentos_caloricos,
            consumo_vegetais, refeicoes_principais, comida_entre_refeicoes,
            fumante, agua_por_dia, monitoramento_de_calorias, atividades_fisicas,
            tempo_em_dipositivos, consumo_de_alcool, meio_de_transporte
        ]

        print("*******\n{}\n********".format(respostas_da_pessoa))

        resultado = self.funcoes.classificar_obesidade(respostas_da_pessoa)

        self.dados(resultado)

    def dados(slef, a):
        st.write(a)


obj = InterfaceClassificador()
obj.questionario()

