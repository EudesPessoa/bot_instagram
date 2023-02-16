from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
from random import randint



def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=1300,1000', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,

    })
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()), options=chrome_options)

    return driver

def digitar_naturalmente(texto, elemento):
    for letra in texto:
        elemento.send_keys(letra)
        sleep(randint(1, 5)/20)


driver = iniciar_driver()
# ir até o instagram
driver.get('https://instagram.com')
sleep(5)

# Encontrando campo email
campo_email = driver.find_element(By.XPATH, "//input[@aria-label='Telefone, nome de usuário ou email']")
sleep(2)
campo_email.click()
seu_email = 'teste_email@gmail.com'
digitar_naturalmente(seu_email, campo_email)
sleep(5)

# Encontrando campo senha
campo_senha = driver.find_element(By.XPATH, "//input[@aria-label='Senha']")
sleep(1)
campo_senha.click()
sleep(3)
sua_senha = '123456'
digitar_naturalmente(sua_senha, campo_senha)
sleep(2)

# Clicar em login
btn_entrar = driver.find_element(By.XPATH, "//button[@class='_acan _acap _acas _aj1-']")
sleep(2)
btn_entrar.click()
sleep(10)

# Navegar até a página escolhida
# Coloque o link do instagram que desejar pela url
driver.get('https://www.instagram.com/xxxxxx/')
sleep(5)

# Encontrar e Clicar na Última postagem
postagem = driver.find_elements(By.XPATH,"//div[@class='_aagu']")
sleep(2)
postagem[0].click()
sleep(5)

# Curtir postagem caso não tenha sido
curtir = driver.find_elements(By.XPATH,"//*[local-name()='svg' and @aria-label='Curtir']")
sleep(5)
if curtir is not None:
    curtir[1].click()
    sleep(2)
else:
    pass

# Clicar no botão de postagem
btn_comentar = driver.find_elements(By.XPATH,"//*[local-name()='svg' and @aria-label='Comentar']")
sleep(3)
btn_comentar[1].click()
sleep(6)

# Clicar no campo de mensagem
campo_comentar = driver.find_element(By.XPATH,"//textarea[@aria-label='Adicione um comentário...']")
sleep(2)
campo_comentar.click()
sleep(4)

# Seu comentario aqui
comentario = 'Parabéns, SUPER Recomendo!!'
digitar_naturalmente(comentario, campo_comentar)
sleep(5)

# Clicar no botão publicar
btn_publicar = driver.find_element(By.XPATH,"//div[@class='x1i10hfl xjqpnuy xa49m3k xqeqjp1 x2hbi6w xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x1lku1pv x1a2a7pz x6s0dn4 xjyslct x1ejq31n xd10rxx x1sy0etr x17r0tee x9f619 x1ypdohk x1i0vuye xwhw2v2 xl56j7k x17ydfre x1f6kntn x2b8uid xlyipyv x87ps6o x14atkfc x1d5wrs8 x972fbf xcfux6l x1qhh985 xm0m39n xm3z3ea x1x8b98j x131883w x16mih1h xt0psk2 xt7dq6l xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 xjbqb8w x1n5bzlp x173jzuc x1yc6y37']")
sleep(3)
btn_publicar.click()
sleep(7)

# Fechar publicação
btn_fechar_puclicacao = driver.find_element(By.XPATH,"//div[@class='x78zum5 x6s0dn4 xl56j7k xdt5ytf']")
sleep(1)
btn_fechar_puclicacao.click()
sleep(6)

# Botão de sair
btn_sair = driver.find_elements(By.XPATH,"//*[local-name()='svg' and @aria-label='Configurações']")
sleep(1)
btn_sair.click()
sleep(2)

# Sair
btn_sair1 = driver.find_elements(By.XPATH,"//div[@class='_ab8w  _ab94 _ab99 _ab9h _ab9m _ab9p _abcm']")
sleep(1)
btn_sair1[6].click()
sleep(3)

# Fechar aba
driver.close()
