from selenium import webdriver
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(options=chrome_options)

for i in range(1,126):
     a = driver.find_element_by_xpath("//*[@id='subCmTb']/tbody/tr[{}]/td[6]/span/input[1]".format(i)).get_attribute('value')
     print("原本的值:"+a)
     s = a.split('.')
     driver.find_element_by_xpath("//*[@id='subCmTb']/tbody/tr[{}]/td[6]/span/input[1]".format(i)).clear()
     print("原值"+a+" 清空成功")
     a = driver.find_element_by_xpath("//*[@id='subCmTb']/tbody/tr[{}]/td[6]/span/input[1]".format(i)).send_keys(s[0])
     print("已经修改为"+s[0])
     print("**************************************************")
     print("**************************************************")

print("所有商品编码已经修正完成")
#//*[@id="subCmTb"]/tbody/tr[208]/td[6]/span/input[1]
#//*[@id="subCmTb"]/tbody/tr[64]/td[6]/span/input[1]
#//*[@id="subCmTb"]/tbody/tr[96]/td[6]/span/input[1]
#//*[@id="subCmTb"]/tbody/tr[128]/td[6]/span/input[1]
#//*[@id="subCmTb"]/tbody/tr[54]/td[6]/span/input[1]
#//*[@id="subCmTb"]/tbody/tr[196]/td[6]/span/input[1]
#//*[@id="subCmTb"]/tbody/tr[160]/td[6]/span/input[1]
#//*[@id="subCmTb"]/tbody/tr[224]/td[6]/span/input[1]
#//*[@id="subCmTb"]/tbody/tr[96]/td[6]/span/input[1]
#//*[@id="subCmTb"]/tbody/tr[96]/td[6]/span/input[1]
#//*[@id="subCmTb"]/tbody/tr[84]/td[6]/span/input[1]
#//*[@id="subCmTb"]/tbody/tr[84]/td[6]/span/input[1]
#//*[@id="subCmTb"]/tbody/tr[144]/td[6]/span/input[1]
#//*[@id="subCmTb"]/tbody/tr[168]/td[6]/span/input[1]
#//*[@id="subCmTb"]/tbody/tr[156]/td[6]/span/input[1]
#//*[@id="subCmTb"]/tbody/tr[125]/td[6]/span/input[1]
