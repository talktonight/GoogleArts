
# coding: utf-8

# In[7]:


# Importação de pacotes
from selenium import webdriver
import urllib.request as ur
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import numpy
import time
import os.path
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


# In[8]:


# Configurações de inicialização
chromeOptions = Options()
chromeOptions.add_argument("--start-maximized")
driver = webdriver.Chrome('/Users/veronicastocco/Downloads/chromedriver')


# In[9]:


# Insira a URL do quadro
base_url = "a-anuncia%C3%A7%C3%A3o/0wGwk67sv7eBJw"
class_code = "XkWAb-LmsqOc"
URL_quadro = "https://artsandculture.google.com/asset/"+base_url+"?ms=%7B%22x%22%3A0%2C%22y%22%3A0%2C%22z%22%3A16%2C%22size%22%3A%7B%22width%22%3A0%2C%22height%22%3A0%7D%7D"

# Abra o quadro
driver.get(URL_quadro)


# In[10]:


# Diminua o zoom até 25%


# In[11]:


# Rode novamente para ir para o quadro novamente
driver.get(URL_quadro)


# In[12]:


# Pegue as variáveis do quadro
url_ajustada = driver.current_url
time.sleep(5)
x = float(url_ajustada.split("%7B%22x%22%3A")[1].split("%2C%22y%22%3A")[0])
y = float(url_ajustada.split("%7B%22x%22%3A")[1].split("%2C%22y%22%3A")[1].split("%2C%22z%22%3A")[0])
z = float(url_ajustada.split("%7B%22x%22%3A")[1].split("%2C%22y%22%3A")[1].split("%2C%22z%22%3A")[1].split("%2C%22size%22%3A%7B%22width%22%3A")[0])
w = float(url_ajustada.split("%7B%22x%22%3A")[1].split("%2C%22y%22%3A")[1].split("%2C%22z%22%3A")[1].split("%2C%22size%22%3A%7B%22width%22%3A")[1].split("%2C%22height%22%3A")[0])
h = float(url_ajustada.split("%7B%22x%22%3A")[1].split("%2C%22y%22%3A")[1].split("%2C%22z%22%3A")[1].split("%2C%22size%22%3A%7B%22width%22%3A")[1].split("%2C%22height%22%3A")[1].split("%7D%7D")[0])

print(w)
print(h)
    
# Calcule os parâmetros necessários
xt = w 
yt = h 
nx = int((1-x)/w) + 1
ny = int((1-y)/h) + 1

# Número de imagens exibidos na tela
elems = driver.find_elements_by_class_name('XkWAb-LmsqOc')
n = len(elems[3:])

# Se der uma divisão por zero, rode novamente


# In[ ]:


base = "https://artsandculture.google.com/asset/"+base_url+"?ms=%7B%22x%22%3A"
erros = []
faltantes = []
for yi in range(nx):
    for xi in range(ny):
        driver.get(base + str(xt+xi*w)+"%2C%22y%22%3A"+str(yt+yi*h)+"%2C%22z%22%3A16%2C%22size%22%3A%7B%22width%22%3A"+str(w)+"%2C%22height%22%3A"+str(h)+"%7D%7D")
        time.sleep(5)
        for i in range(n):
            try:
                elems = driver.find_elements_by_class_name(class_code)
                string = elems[i+3].get_attribute(name='style')
                filename = "Imagens/%d - %d.png"%(int((int(string[string.find("(")+1:string.find("px, ")])+511)/512),int((int(string[string.find(", ")+2:string.find("px, 0px);")])+511)/512))
                if not os.path.isfile(filename):
                    driver.get(elems[i+3].get_attribute(name='src'))
                    time.sleep(1)
                    driver.get_screenshot_as_file(filename)
                    print(xi,yi,i,filename)
                    driver.get(base + str(xt+xi*w)+"%2C%22y%22%3A"+str(yt+yi*h)+"%2C%22z%22%3A16%2C%22size%22%3A%7B%22width%22%3A"+str(w)+"%2C%22height%22%3A"+str(h)+"%7D%7D")
                    time.sleep(2)
                else:
                    pass
            except:
                faltantes.append("%d\t%d\t%d\t%s"%(yi,xi,i,"Não encontrado"))

