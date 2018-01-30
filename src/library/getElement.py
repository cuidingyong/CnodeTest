class MainPageElement(object):

    shouye = lambda x: x.find_element_by_xpath('/html/body/div[1]/div/div/ul/li[1]/a')
    xinshourumen = lambda x: x.find_element_by_xpath('/html/body/div[1]/div/div/ul/li[2]/a')
    api = lambda x: x.find_element_by_xpath('/html/body/div[1]/div/div/ul/li[3]/a')
    guanyu = lambda x: x.find_element_by_xpath('/html/body/div[1]/div/div/ul/li[4]/a')
    zhuce = lambda x: x.find_element_by_xpath('/html/body/div[1]/div/div/ul/li[5]/a')
    denglu = lambda x: x.find_element_by_xpath('/html/body/div[1]/div/div/ul/li[6]/a')
    fabuhuati = lambda x: x.find_element_by_css_selector('span.span-success')
    my_mainpage = lambda x: x.find_element_by_css_selector('a.dark')
    all_topic = lambda x: x.find_elements_by_class_name('topic_title')

class RegisterElement(object):
    username = lambda x: x.find_element_by_id('loginname')
    password = lambda x: x.find_element_by_id('pass')
    repassword = lambda x: x.find_element_by_id('re_pass')
    email = lambda x: x.find_element_by_id('email')
    register_button = lambda x: x.find_element_by_class_name('span-primary')
    checkpoint = lambda x: x.find_element_by_css_selector('div.alert.alert-success')


class LoginElement(object):

    checkpoint_loginpage = lambda x: x.find_element_by_class_name('active')
    username = lambda x: x.find_element_by_id('name')
    password = lambda x: x.find_element_by_id('pass')
    login_button = lambda x: x.find_element_by_class_name('span-primary')
    login_by_github = lambda x: x.find_element_by_class_name('span-info')
    forget_password = lambda x: x.find_element_by_id('forgot_password')
    checkpoint = lambda x: x.find_element_by_css_selector('#sidebar > div:nth-child(1) > div.inner > div > div > span.user_name > a')


class IssueElement(object):
    xuanzhebankuai = lambda x: x.find_element_by_css_selector('select#tab-value')
    share = lambda x: x.find_element_by_xpath('//option[@value="share"]')
    ask = lambda x: x.find_element_by_xpath('//option[@value="ask"]')
    job = lambda x: x.find_element_by_xpath('//option[@value="job"]')
    title = lambda x: x.find_element_by_id('title')
    # zhengwen = lambda x: x.find_element_by_class_name('CodeMirror-code')
    zhengwen = lambda x: x.find_elements_by_class_name('CodeMirror-code')
    tijiao = lambda x: x.find_elements_by_css_selector('input.span-primary.submit_btn')
    checkpoint_tijiao = lambda x: x.find_element_by_class_name('topic_full_title')

    lianjie = lambda x: x.find_element_by_css_selector('a.eicon-link')
    shangchuan = lambda x: x.find_element_by_css_selector('a.eicon-image')
    shangchuantupian = lambda x: x.find_element_by_name('file')
    checkpoint_tupian = lambda x: x.find_element_by_class_name('cm-tag')


class PersonalElement(object):
    first_topic = lambda x: x.find_element_by_xpath('//*[@id="content"]/div[2]/div[2]/div/a')
    delete_topic = lambda x: x.find_element_by_css_selector('i.fa.fa-lg.fa-trash')






