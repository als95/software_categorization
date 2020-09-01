import prepare
import categories as cl

# TODO : for crawling in python, we should use webdriver.
#        This program uses a chromeWebdriver and automatically download Java OpenSource projects
#        from SourceForge.net.
#        RTSE Kim minha
#        Updated : 2019. 11.

if __name__ == '__main__':
    url_base = "https://sourceforge.net/directory/"
    url_n_lang = "natlanguage:english/"
    url_c_lang = "language:java/"
    url_os = "os:windows/os:linux/"
    url_page = "?page="

    destDownload_num = 99999

    main_category = cl.main_category
    sub_category = [cl.dev_sub, cl.int_sub, cl.sci_sub, cl.sys_sub,
                    cl.bsi_sub, cl.com_sub, cl.mm_sub, cl.gm_sub]

    crawling = prepare.CrawlingManager(url_base, url_n_lang, url_c_lang, url_os, url_page)
    crawling.run(main_category, sub_category, destDownload_num)