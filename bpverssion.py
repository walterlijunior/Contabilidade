# Contas patrimoniais

# Contas do Ativo
#Contas do tipo "Bens" do Ativos
print('Insira o valor de todas as contas patrimôniais a seguir')
bcm = float(input('Valor da conta Banco Conta  Movimento: R$'))
caixa = float(input('Digite o vallor da conta Caixa: R$'))
estoque = float(input('Digite o valor da conta Estoque e Mercadorias: R$'))
floresta = float(input('Digite o valor da conta Florestas: R$'))
imoveis = float(input('Digite o valor da conta Imóveis: R$'))
maqeferr = float(input('Digite o valor da conta Máquinas e Ferramentas: R$'))
marepate = float(input('Digite o valor da conta Marcas e Patentes: R$'))
materia = float(input('Digite o valor da conta Matéria-Prima: R$'))
mov = float(input('Digite o valor da conta Móveis e Utensílios: R$'))
obra = float(input('Digite o valor da conta Obras em Andamento: R$'))
prop = float(input('Digite o valor da conta Propriedades para Investimentos: R$'))
semovente = float(input('Digite o valor da conta Semoventes: R$'))
veicuso = float(input('Digite o valor da conta Veículos de Uso: R$'))

#Total da soma dos Bens do Ativo
totalbens = bcm + caixa + estoque + floresta + imoveis + maqeferr + marepate + materia + mov + obra + prop + semovente + veicuso

print('O TOTAL DE BENS FORAM: R$ {:.2f}'.format(totalbens))

#Contas tipo "Direitos" do Ativo
print('OBS: A conta Fornecedores a Receber também pode ser chamada por Adiantamento a Fornecedores')
fornecedor = float(input('Digite o valor da conta Fornecedores a Receber: R$'))

aluguelr = float(input('Digite o valor da conta Alugéis a Receber: R$'))
client = float(input('Digite o valor da conta Clientes: R$'))

print('OBS: a conta (-) Depreciação Acumulada tem seu saldo de valor negativo, pois é uma oonta redutora.')
depreacum = float(input('Digite o valor da conta (-) Depreciação Acumulada: R$'))

print('OBS: A conta Duplicatas a Receber também pode ser chamada de Duplicatas emitidas pela empresa \n diferente de Duplicatas aceitas pela empresa.')
duplir = float(input('Digite o valor da conta Duplicatas a Receber: R$'))

print('OBS: A conta Empréstimos a Receber pode ser chamada de Empréstimos concedidos \n diferente de Empréstimos obtidos.')
emprr = float(input('Digite o valor da conta Empréstimos a Receber: R$'))

print('OBS: A conta ICMS a Recuperar e dirente de ICMS a Receber.')
icmsrecu = float(input('Digite o valor da conta ICMS a Recuperar: R$'))

invcoli = float(input('Digite o valor da conta Investimentos em Coligadas: R$'))
partcapi = float(input('Digite o valor da conta Participação Acionária no Capital de Empresas: R$'))

print('OBS: A conta Promissórias a Receber também pode ser chamada de Promissórias assinadas \n por terceiros.')
promissr = float(input('Digite o valor da conta Promissórias a Receber: R$'))

titulor = float(input('Digite o valor da conta Títulos a Receber: R$'))

#Total da soma dos Direitos do Ativo
totaldir = fornecedor + aluguelr + client + depreacum + duplir + emprr + icmsrecu + invcoli + partcapi + promissr + titulor
totalativo = totalbens + totaldir
print('O TOTAL DOS DIREITOS FORAM R$ {:.2f} '.format(totaldir))

print('O TOTAL DO ATIVO FOI DE R$ {:.2f}'.format(totalativo))


#Contas do Passivo
#Contas do tipo Obrigações Exigíveis

print('OBS: A conta Clientes a Pagar, também pode ser chamada de Adiantamento de Clientes.')
clientp = float(input('Digite o valor da conta Clientes a Pagar R$: '))

aluguelp = float(input('Digite o valor da conta Aluguéis a Pagar: R$'))
contprev = float(input('Digite o valor da conta Contribuição Previdênciária a Recolher: R$'))
divp = float(input('Digite o valor da conta Dividendos a Pagar: R$'))

print('OBS: A conta Duplicatas a Pagar também pode ser chamada de Duplicatas aceitas pela empresa')
duplip = float(input('Digite o valor da conta Duplicatas a Pagar: R$'))

print('OBS: A conta Empréstimos a Pagar, também pode ser chamada de Empréstimos obtidos.')
emprobt = float(input('Digite o valor da conta Empréstimos a Pagar: R$'))

fgtsr = float(input('Digite o valor da conta FGTS a Recolher: R$'))
finp = float(input('Digite o valor da conta Financiamentos a Pagar: R$'))
fornecp = float(input('Digite o valor da conta Fornecedores a Pagar: R$'))
icmsrecolh = float(input('Digite o valor da conta ICMS a Recolher: R$'))
imposr = float(input('Digite o valor da conta Impostos a Recolher: R$'))
imptaxr = float(input('Digite o valor da conta Impostos e Taxas a Recolher: R$'))
issrec = float(input('Digite o valor da conta ISS a Recolher: R$'))
jurosp = float(input('Digite o valor da conta Juros a Pagar: R$'))

print('OBS: A conta Promissórias a Pagar também pode ser chamada de Promissórias assinadas pela empresa')
promisspaga = float(input('Digite o valor da conta Promissórias a Pagar: R$'))

provi = float(input('Digite o valor da conta Provisões para Férias e 13° Salário: R$'))
salariop = float(input('Digite o valor da conta Salários a Pagar: R$'))
titulop = float(input('Digite o valor da conta Títulos a Pagar: R$'))

#Total da somas das Obrigações Exigíveis
totalobrexi = clientp + aluguelp + contprev + divp + duplip + emprobt + fgtsr + finp + fornecp + icmsrecolh + imposr + imptaxr + issrec + jurosp + promisspaga + provi + salariop + titulop
print('O TOTAL DAS OBRIGAÇÕES NÃO EXIGÍVEIS FORAM DE R$ {:.2f}'.format(totalobrexi))

#Passivo não exigível - Patrimônio Líquido
pl = totalativo - totalobrexi
print('O VALOR TOTAL DO PATRIMÔNO LÍQUIDO É DE R$ {:.2f}'.format(pl))

#Contas do Patrimônio Líquido
capitsoci = float(input('Digite o valor da conta Capital Social: R$'))

print('OBS: O valor do saldo da conta (-) Capital a Integralizar deve ser negativo, pois é uma conta redutora')
capint = float(input('Digite o valor da conta (-) Capital a Integralizar: R$'))

print('OBS: O valor do saldo da conta (-) Ações em Tesouraria deve ser negativo, pois é uma conta redutora')
actesou = float(input('Digite o valor da conta (-) Ações em Tesouraria: R$'))

reserleg = float(input('Digite o valor da conta Reserva Legal: R$'))

#Saldo do Lucro ou Prejuizo Acumulados
lpa = pl - capitsoci - capint - actesou - reserleg
print('o O saldo da conta Lucros ou Prejuizo Acumulado é de R$ {:.2f}'.format(lpa))

#Valo toatal do Passivo
totalpassr = totalobrexi + pl
print('O VALOR TOTAL DO MEU PASSIVO TOTAL É DE R$ {:.2f}'. format(totalpassr))
