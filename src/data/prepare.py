import time
from datetime import datetime
import openpyxl
from selenium import webdriver

import categories as cl
from exception import NoDownloadPageError, NoGreenBoxError


class CrawlingManager:
    def __init__(self, url_base, url_n_lang, url_c_lang, url_os, url_page, page_num=1):
        """
        :param url_base: base url based on software public repository website
        :param url_n_lang: natural language
        :param url_c_lang: computer language
        :param url_os: operating system type - window, linux
        :param url_page: page representation
        :param page_num: integer for page. default value is one
        """
        self.url_base = url_base
        self.url_n_lang = url_n_lang
        self.url_c_lang = url_c_lang
        self.url_os = url_os
        self.url_page = url_page
        self.page_num = page_num

        self.item_idx = 1
        self.downloading_num = 0
        self.main_idx = 0
        self.sub_idx = 0

        self.item_e_stack = 0
        self.download_e_stack = 0

        self.wb = openpyxl.load_workbook('E:\\data\\label\\category_label.xlsx')
        self.sheet = self.wb['Sheet1']

    def run(self, main_category, sub_category, destDownload_num):
        """
        :param main_category: list for Top categories
        :param sub_category: list for subcategories
        :param destDownload_num: Total number of applications you want to download
        """

        for sub in sub_category:
            while len(sub) is not 0:
                self.print_information()
                path = "E:\\data\\sourceforge\\" + cl.directory[self.main_idx] + "\\" + sub[self.sub_idx]
                print("-- Download Location : ", path, " --")
                prefs = {"download.default_directory": path}
                options = webdriver.ChromeOptions()
                options.add_experimental_option("prefs", prefs)

                driver = webdriver.Chrome('C:\\Python\\chromedriver_win32\\chromedriver.exe', chrome_options=options)
                driver.implicitly_wait(2.5)

                advertising_idx = [1, 2, 8, 14]

                category_url = self.url_base + main_category[self.main_idx] + sub[self.sub_idx] + "/"
                option_url = self.url_n_lang + self.url_c_lang + self.url_os
                page_url = self.url_page + str(self.page_num)
                target_url = category_url + option_url
                print("enter url : ", (target_url + page_url))
                driver.get(target_url)

                while self.downloading_num is not destDownload_num:
                    if self.item_idx in advertising_idx:
                        self.item_idx += 1
                        continue
                    time.sleep(0.3)
                    self.itemSelectBehavior(driver, url=target_url)
                    if self.item_e_stack > 6:
                        break

                    self.downloadBehavior(driver)

                    self.item_e_stack = 0
                    self.download_e_stack = 0

                    driver.back()
                    time.sleep(0.3)

                    if self.item_idx == 29:
                        self.print_information()
                        try:
                            self.page_num += 1
                            self.item_idx = 1
                            driver.get(target_url + self.url_page + str(self.page_num))
                            if self.page_num > 20:
                                print("page is lager than 20. move a subcategory")
                                break
                        except Exception:
                            break
                    self.item_idx += 1

                    if self.download_e_stack > 6:
                        self.page_num += 1

                sub.remove(sub[self.sub_idx])
                print("-- move to next sub category --")
                self.page_num = 1
                self.item_idx = 1
                self.item_e_stack = 0
                self.download_e_stack = 0

                # time.sleep(60)
                driver.close()

            self.main_idx += 1
            print("-- Download Complete a Category files : ", main_category[self.main_idx], " --")
            print(datetime.now())
            time.sleep(0.3)

    def itemSelectBehavior(self, driver: webdriver, url):
        """
        :param driver: webdriver
        :param url: total url for renewal
        """
        # print("-- itemSelectBehavior() --")
        while self.item_idx < 30:
            try:
                # print("-- log : itemSelectionBehavior Try --")
                driver.find_element_by_xpath(
                    """//*[@id="pg_directory"]/div[5]/div[3]/div[3]/section/ul/li["""
                    + str(self.item_idx) + """]/div[2]/div/a""").click()
                time.sleep(0.3)
                break
            except Exception:
                # print("-- log : itemSelectionBehavior Exception occur --")
                self.item_e_stack += 1
                # print("item stack is ", self.item_e_stack)

                driver.get(url + self.url_page + str(self.page_num))
                time.sleep(0.3)
                if self.item_e_stack > 6:
                    break

    def downloadBehavior(self, driver: webdriver):
        """
        :param driver: webdriver
        """
        self.print_information()
        while self.item_idx < 30:  # Click Green Download Box
            try:
                label = []
                # print("-- log : downloadBehavior Try --")
                # driver.find_element_by_xpath(
                #     """//*[@id="pg_project"]/div[5]/div[2]/div[1]/div/section/div[2]/div[3]/a[1]""").click()
                # time.sleep(6)
                correct = []
                print("-- log : try to get category name")
                cate_name0 = driver.find_element_by_xpath("""
                                                //*[@id="pg_project"]/div[5]/div[2]/div[1]/div/article/section[2]/div[1]""").text
                cate_name0 = cate_name0.split('\n')[0]

                cate_name1 = driver.find_element_by_xpath("""
                                                 //*[@id="pg_project"]/div[5]/div[2]/div[1]/div/article/section[3]/div[1]""").text
                cate_name1 = cate_name1.split('\n')[0]

                cate_name2 = driver.find_element_by_xpath("""
                                                //*[@id="pg_project"]/div[5]/div[2]/div[1]/div/article/section[4]/div[1]""").text
                cate_name2 = cate_name2.split('\n')[0]

                cate_name3 = driver.find_element_by_xpath("""
                                                //*[@id="pg_project"]/div[5]/div[2]/div[1]/div/article/section[5]/div[1]""").text
                cate_name3 = cate_name3.split('\n')[0]

                correct.append(cate_name0)
                correct.append(cate_name1)
                correct.append(cate_name2)
                correct.append(cate_name3)
                corr_idx = correct.index("Categories")

                cate_name = driver.find_element_by_xpath("""
                                                //*[@id="pg_project"]/div[5]/div[2]/div[1]/div/article/section[""" + str((int(corr_idx) + 2)) + """]/div[1]""").text

                cate_name = cate_name.split('\n')[1:]
                cate_name = cate_name[0].split(',')

                time.sleep(0.3)
                self.downloading_num += 1
                driver.find_element_by_xpath("""
                //*[@id="top_nav_admin"]/ul/li[2]/a/span""").click()
                print("-- log : try to get file name")
                name = driver.find_element_by_xpath("""//*[@id="files"]/div[2]/div/a[1]/span[2]""").text
                time.sleep(0.3)
                label.append(name)
                label = label + cate_name

                for i in range(len(label)):
                    self.sheet.cell(self.downloading_num, i+1, label[i])
                time.sleep(0.3)
                self.wb.save('E:\\data\\label\\category_label.xlsx')
                time.sleep(0.3)

                print("-> The number of Downloaded file : %d" % self.downloading_num)
                break
            except Exception:
                self.download_e_stack += 1
                # print("download_stack is ", self.download_e_stack)
                # print("-- log : downloadBehavior Exception occur --")
                if self.download_e_stack > 3:
                    break

    def print_information(self):
        print(":: present processing information ::")
        print("item Index : ", self.item_idx)
        print("page Number : ", self.page_num)
