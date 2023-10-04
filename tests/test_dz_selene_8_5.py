import os.path

from selene import browser

def test_tools_qa():

    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('label[for="hobbies-checkbox-1"]').click()
    browser.element('#firstName').type('Anatolii')
    browser.element('#lastName').type('Tkach')
    browser.element('#userEmail').type('tkach.vip@gmail.com')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').type('550391393')
    browser.element('#dateOfBirthInput').click()
    browser.element('[class="react-datepicker__month-select"]').click().element('[value="2"]').click()
    browser.element('[class="react-datepicker__year-select"]').click().element('[value="1999"]').click()
    browser.element('[class="react-datepicker__day react-datepicker__day--008"]').click()
    browser.element('#subjectsInput').type('automated testing').press_enter()
    browser.element('[id="uploadPicture"]').send_keys(os.path.abspath('image/kat.png.png'))


