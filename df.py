from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import readdata
from time import sleep


def sendKey(driver,element,value):
    driver.find_element_by_id(element).clear()
    driver.find_element_by_id(element).send_keys(value)
    print(element+"录入成功")

def findele(drive,xpath,value):
    drive.find_element_by_xpath(xpath).clear()
    drive.find_element_by_xpath(xpath).send_keys(value)
    print(value+"录入成功")
#定位元素数据
iterms = {
    'BP_cmmdtyName' : readdata.goodsname,
    'cmModel' : readdata.goodsmodel,
    'VOLUM' : readdata.VOLUM,
    'BRGEW' : readdata.BRGEW,
}
# #接管浏览器
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(options=chrome_options)
driver.refresh()
#定位元素并输入内容
sendKey(driver, "BP_cmmdtyName", iterms['BP_cmmdtyName'])
sendKey(driver, "cmModel", iterms['cmModel'])
sendKey(driver, "VOLUM", iterms['VOLUM'])
sendKey(driver, "BRGEW", iterms['BRGEW'])
sendKey(driver, "005039", iterms['BP_cmmdtyName'])
driver.find_element_by_xpath("//*[@id='005039']").send_keys(readdata.goodsname)
for i in range(0, len(readdata.color)):
    driver.find_element_by_xpath("//*[@id='G00001']/td[2]/div[2]/div/span/input").send_keys(readdata.color[i])
    driver.find_element_by_xpath("//*[@id='G00001']/td[2]/div[2]/div/a").click()
    print("颜色型号"+readdata.color[i]+"录入成功")
    sleep(0.5)

driver.execute_script('window.scrollBy(0,400)')

for j in range(0, len(readdata.Glass)):
    driver.find_element_by_xpath("//*[@id='G00002']/td[2]/div[2]/div/span/input").send_keys(readdata.Glass[j])
    driver.find_element_by_xpath("//*[@id='G00002']/td[2]/div[2]/div/a").click()
    print("度数"+readdata.Glass[j]+"录入成功")
    sleep(0.5)

driver.execute_script('window.scrollBy(0,400)')
count = 1
for i in range(0, len(readdata.color)):
    for j in range(0,len(readdata.Glass)):
        if j == 0:
            driver.find_element_by_xpath(
                "//*[@id='newSubCmTbId']/tbody/tr[{}]/td[6]/span/input".format(count)).send_keys(readdata.gooid[count-1])
            print("颜色"+readdata.color[i]+"  度数"+readdata.Glass[j]+"商品编码录入成功")
            driver.find_element_by_xpath(
            "//*[@id='newSubCmTbId']/tbody/tr[{}]/td[4]/div/input".format(count)).send_keys(str(readdata.price))
            print("颜色"+readdata.color[i]+"  度数"+readdata.Glass[j]+"商品价格录入成功")
            count += 1
            sleep(0.5)
        else:
            driver.find_element_by_xpath(
                "//*[@id='newSubCmTbId']/tbody/tr[{}]/td[4]/span/input".format(count)).send_keys(readdata.gooid[count-1])
            print("颜色"+readdata.color[i]+"  度数"+readdata.Glass[j]+"商品编码录入成功")
            driver.find_element_by_xpath(
                "//*[@id='newSubCmTbId']/tbody/tr[{}]/td[2]/div/input".format(count)).send_keys(str(readdata.price))
            print("颜色"+readdata.color[i]+"  度数"+readdata.Glass[j]+"商品价格录入成功")
            sleep(0.5)
            count += 1
findele(driver,"//*[@id='000136']","非离子水凝胶")#材质
findele(driver,"//*[@id='005517']","22400BZX00427000")#批准文号
findele(driver,"//*[@id='005362']","PIA株式会社")#生产厂家
findele(driver,"//*[@id='015651']","22400BZX00427000")#医疗器械编号
findele(driver,"//*[@id='015652']","22400BZX00427000")#生产许可证编号
findele(driver,"//*[@id='supplierCmCodeP']",iterms['cmModel'])
findele(driver,"//*[@id='cmTitle']",iterms['BP_cmmdtyName'])
# driver.find_element_by_xpath("//*[@id='newSubCmTbId']/tbody/tr[{}]/td[6]/span/input".format(i+1)).send_keys(readdata.Glass[i])
# driver.find_element_by_xpath("//*[@id='newSubCmTbId']/tbody/tr[1]/td[6]/span/input").send_keys("374517263")
print("*************************全部EXCEL表格中的数据都已经录入成功*****************")
