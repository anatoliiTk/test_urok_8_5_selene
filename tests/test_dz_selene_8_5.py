import os.path

from selene import browser, command, have


def test_tools_qa():
    #заполнение формы
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('#firstName').type('Anatolii')
    browser.element('#lastName').type('Tkach')
    browser.element('#userEmail').type('tkach.vip@gmail.com')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').type('5503913933')
    browser.element('#dateOfBirthInput').click()
    browser.element('[class="react-datepicker__month-select"]').click().element('[value="2"]').click()
    browser.element('[class="react-datepicker__year-select"]').click().element('[value="1999"]').click()
    browser.element('[class="react-datepicker__day react-datepicker__day--008"]').click()
    browser.element('#subjectsInput').type('automated testing').press_enter()
    browser.element('[id="stateCity-label"]').perform(command.js.scroll_into_view)
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[id="uploadPicture"]').send_keys(os.path.abspath('image/kat.png.png'))
    browser.element('[id="currentAddress"]').type('Pushkin 22').perform(command.js.scroll_into_view)
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Delhi').press_enter()
    browser.element('[id="submit"]').press_enter()

    #проверка резльтата
    browser.element('.modal-title').should(have.text('Thanks for submitting the form'))
    browser.all('tbody td:nth-of-type(2)').should(have.exact_texts(
        'Anatolii Tkach',
        'tkach.vip@gmail.com',
        'Male',
        '5503913933',
        '08 March,1999',
        'Sports',
        'Kat.png.png',
        'Pushkin 22',
        'NCR Delhi'
    ))