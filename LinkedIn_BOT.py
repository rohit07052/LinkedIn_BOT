from selenium import webdriver
from time import sleep
import re

class Linkedin:
    
    def __init__(self,username,password):
        
        self.driver = webdriver.Chrome()
        self.driver.get("https://linkedin.com")
        
        sleep(2)
        #maximizing the window
        self.driver.maximize_window()
        
        #selecting username/email text input type
        self.driver.find_element_by_xpath("/html/body/main/section[1]/div[2]/form/div[2]/div[1]/input")\
        .send_keys(username)

        sleep(1)
        
        #selecting password input type
        self.driver.find_element_by_xpath("/html/body/main/section[1]/div[2]/form/div[2]/div[2]/input")\
        .send_keys(password)
        
        sleep(1)

        #clicking signin button
        self.driver.find_element_by_xpath("/html/body/main/section[1]/div[2]/form/button")\
        .click()
        
        sleep(1)
        # i am not a robot..


        #going to network section
        self.driver.find_element_by_xpath("/html/body/div[9]/header/div[2]/nav/ul/li[2]/a")\
        .click()
        
        sleep(3)
        #self.driver.find_element_by_xpath("/html/body/div[9]/header/div[2]/nav/ul/li[2]/a")\
        #.click()
        #sleep(1)
        # click on the message to close
        self.driver.find_element_by_xpath("/html/body/div[9]/aside/div[1]/header").click()
        sleep(3)
        # go to the manage section
        self.driver.find_element_by_xpath("/html/body/div[9]/div[4]/div/div/div/div/div/div/div[1]/section/header/a")\
        .click()


        #navigation part over
        
        # method for getting the list of connection request
        # from your institution/company

    
    def listSameInst(self,regularExpr):
        
        #self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        try:
            recievedUl = self.driver.find_element_by_xpath("/html/body/div[8]/div[3]/div/div/div/div/div/div/section/div[2]/section/div/ul")
            liElements = recievedUl.find_elements_by_tag_name("li")#.find_element_by_css_selector("div.display-flex ph2 pt1 pb1")
            listOfDesc = []
            for li in liElements:
    ##            div1 = i.find_element_by_css_selector("div.display-flex.ph2.pt1.pb1")
    ##            div2 = i.find_element_by_css_selector("div.display-flex.ph2.pt1.pb1 > div.display-flex.flex-1.align-items-center.pl0")
    ##            div3 = i.find_element_by_css_selector("div.display-flex.ph2.pt1.pb1 > div.display-flex.flex-1.align-items-center.pl0 > div")
    ##            div4 = i.find_element_by_css_selector("a.invitation-card__link.ember-view")
                div5 = li.find_element_by_css_selector("span.invitation-card__subtitle.t-14.t-black--light.t-normal")
                div6 = li.find_element_by_css_selector("span.invitation-card__title.t-16.t-black.t-bold")
                inst = div5.get_attribute('innerHTML')
                string = (div5.get_attribute('innerHTML'))
                regex = re.compile(regularExpr,flags = re.IGNORECASE|re.MULTILINE)
                #regex = re.compile(r"internship",flags = re.IGNORECASE|re.MULTILINE)
                
                searchInst = regex.search(string)
                if searchInst:
                    listOfDesc.append(div6.get_attribute('innerHTML'))
                    accept = li.find_element_by_css_selector("button.invitation-card__action-btn.artdeco-button.artdeco-button--2.artdeco-button--secondary.ember-view")
                    print(accept.get_attribute('innerHTML'))
                    accept.click()
                sleep(1)
            print(listOfDesc)

            
        except:
            pass

        
    def withdraw(self,timelimit):
        try:
            # go to the sent section
            self.driver.find_element_by_xpath("/html/body/div[8]/div[3]/div/div/div/div/div/div/section/div[1]/div/button[2]")\
            .click()
            # selecting all of the sent requests
            sleep(2)
            sentUl = self.driver.find_element_by_xpath("/html/body/div[8]/div[3]/div/div/div/div/div/div/section/div[2]/div[2]/ul")
            sleep(1)
            sentLi = sentUl.find_elements_by_tag_name("li")
            
            listOfsent = []
            for li in sentLi:
                #   get the time 
                time = li.find_element_by_css_selector("div > div.display-flex.flex-1.align-items-center.pl0 > div > time")

                #  strip the white spaces           
                printThis = str(time.get_attribute('innerHTML')).strip()  

                #  put it in a list
                timeSplit = list(printThis.split())

                # list for setting precedence of time
                prec = ['minute','minutes','hour','hours','day','days','week','weeks','month','months','year','years']

                # get the precedence
                timePrec = prec.index(timeSplit[1])

                # if time crosses your given time
                t1,t2 = timelimit.split()
                t1 = int(t1)
                t3 = prec.index(t2)
                if timePrec>=t1 and int(timeSplit[0])>t2:

                    # get the withdraw button
                    print(li.find_element_by_css_selector("span.invitation-card__title.t-16.t-black.t-bold").get_attribute('innerHTML')) #for debugging purposes
                    
                    withdrawButton = li.find_element_by_css_selector("button.invitation-card__action-btn.artdeco-button.artdeco-button--muted.artdeco-button--3.artdeco-button--tertiary.ember-view")
                    withdrawButton.click()

                    
                    sleep(3)
                    #confirmWithdraw = li.find_element_by_css_selector("button.artdeco-modal__confirm-dialog-btn.artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view")

                    # get the new body to access the confirm withdraw button
                    newHTMLbody = self.driver.find_element_by_css_selector("body.render-mode-BIGPIPE.nav-v2.theme.theme--classic.ember-application.boot-complete.icons-loaded.artdeco-modal-is-open")

                    # confirm click on the withdraw button
                    confirmWithdraw = newHTMLbody.find_element_by_css_selector("button.artdeco-modal__confirm-dialog-btn.artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view")
                    
                    print(confirmWithdraw.get_attribute('innerHTML')) # for debugging purposes
                    
                    confirmWithdraw.click()
                    
                    sleep(2)
                    
                    
                sleep(1)
            
        except:
            pass
        
                
myObj = Linkedin('drakecoste@mywrld.top','dontforget')
sleep(2)

# set the regular expression for selecting ......
regularExpr = r"(asansol)+\s(engineering)\s(college)+"

myObj.listSameInst(regularExpr)
sleep(3)
gettimelimit = '5 hours'  # set time limit (small time limit for testing purposes)
myObj.withdraw(gettimelimit)

