## if institution is not matched it goes to his/her account and checks again
# if then matched then it accepts but it makes the process slow
from selenium import webdriver
from time import sleep
import re

class Linkedin:
    
    def __init__(self,username,password):

        self.driver = webdriver.Chrome()

        
        self.driver.get("https://linkedin.com")
        print('Chrome opened')
        
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

        print('Logging in')

        #clicking signin button
        self.driver.find_element_by_xpath("/html/body/main/section[1]/div[2]/form/button")\
        .click()
        
        sleep(1)
        # i am not a robot..

        print('Logged In')

        #going to network section
        self.driver.find_element_by_xpath("//*[@id=\"mynetwork-nav-item\"]")\
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
        if 1:#try:
            
            recievedUl = self.driver.find_element_by_xpath("/html/body/div[8]/div[3]/div/div/div/div/div/div/section/div[2]/section/div/ul")
            liElements = recievedUl.find_elements_by_tag_name("li")#.find_element_by_css_selector("div.display-flex ph2 pt1 pb1")
            
            listOfDesc = []
            length = len(liElements)
            index = 0
            while length:
                sleep(2)

                a = self.driver.find_element_by_xpath("/html/body/div[8]/div[3]/div/div/div/div/div/div/section/div[2]/section/div/ul")
                b = a.find_elements_by_tag_name("li")
    ##            div1 = i.find_element_by_css_selector("div.display-flex.ph2.pt1.pb1")
    ##            div2 = i.find_element_by_css_selector("div.display-flex.ph2.pt1.pb1 > div.display-flex.flex-1.align-items-center.pl0")
    ##            div3 = i.find_element_by_css_selector("div.display-flex.ph2.pt1.pb1 > div.display-flex.flex-1.align-items-center.pl0 > div")
    ##            div4 = i.find_element_by_css_selector("a.invitation-card__link.ember-view")
                
                div5 = b[index].find_element_by_css_selector("span.invitation-card__subtitle.t-14.t-black--light.t-normal")
                div6 = b[index].find_element_by_css_selector("span.invitation-card__title.t-16.t-black.t-bold")
                
                inst = div5.get_attribute('innerHTML')
                
                string = (div5.get_attribute('innerHTML'))
                
                regex = re.compile(regularExpr,flags = re.IGNORECASE|re.MULTILINE)
                #regex = re.compile(r"internship",flags = re.IGNORECASE|re.MULTILINE)
                
                searchInst = regex.search(string)
                
                if searchInst:
                    
                    listOfDesc.append(div6.get_attribute('innerHTML'))
                    
                    accept = b[index].find_element_by_css_selector("button.invitation-card__action-btn.artdeco-button.artdeco-button--2.artdeco-button--secondary.ember-view")
                    print(accept.get_attribute('innerHTML'))
                    
                    accept.click()
    
                    
                
                else:
                    ## if not found go to that person's account and check there if it is not present there also then don't accept
                    

                    print('in the else section')
                    div5.click()  # going to his/her account

                    # get the details
                    
                    sleep(5)
                    
                    
                    
                    #institution = self.driver.find_element_by_css_selector("div.ph5.pb5 >div.display-flex.mt2 > div:nth-child(2) > ul")
                    
                    inst = self.driver.find_element_by_css_selector("body > div.application-outlet > div.authentication-outlet > div > div > div > div > div.pv-content.profile-view-grid.neptune-grid.two-column.ghost-animate-in > main > div.ember-view > section > div.ph5.pb5 > div.display-flex.mt2 > div:nth-child(2) > ul > li > a > span")
                    
                    
                    getInst = inst.get_attribute('innerHTML')

                    finalInst = getInst.strip()

                    searchAgain = regex.search(finalInst)

                    if searchAgain:
                        
                        againAccpt = self.driver.find_element_by_xpath("/html/body/div[8]/div[3]/div/div/div/div/div[2]/main/div[1]/section/div[2]/div[1]/div[2]/div/div/span[1]/div/button")
                        
                        againAccpt.click()
                        index -= 1
                        length -= 1
                        sleep(3)
                    
                    self.driver.execute_script("window.history.go(-1)")
                    sleep(10)
                sleep(1)
                index += 1
                length -= 1
            print(listOfDesc)
            
        #except:
            #pass


        
    def withdraw(self,timelimit):
        if 1:#try:
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
                print(t1,t3)
                print(timePrec,timeSplit[0])
                if t3<timePrec or (t3==timePrec and  int(timeSplit[0])>=t1):
                    print('in the if section')
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
            
##        except:
##            pass
        
                
myObj = Linkedin('nirtizerto@enayu.com','hellohello')
sleep(2)

# set the regular expression for selecting ......
regularExpr = r"(asansol)+\s(engineering)\s(college)+"

myObj.listSameInst(regularExpr)
sleep(3)
gettimelimit = '5 hours'  # set time limit (small time limit for testing purposes)
myObj.withdraw(gettimelimit)

