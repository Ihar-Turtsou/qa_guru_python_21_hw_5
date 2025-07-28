import os
from selene import browser, have, be

def test_form_submission(setup_browser):
    browser.open('/automation-practice-form')
    browser.element('[id="firstName"]').type('Carla')
    browser.element('[id="lastName"]').type('Johnson')
    browser.element('[id="userEmail"]').type('Johnson@gmail.pom')
    browser.element('//input[@name="gender" and @value="Female"]/following-sibling::label').click()
    browser.element('[id="userNumber"]').type('7788995511')

    browser.execute_script('window.scrollBy(0, 500)')

    browser.element('[id = "dateOfBirthInput"]').click()
    browser.all('.react-datepicker__month-select option').element_by(have.exact_text('August')).click()
    browser.all('.react-datepicker__year-select option').element_by(have.exact_text('1995')).click()
    browser.element('[aria-label="Choose Saturday, August 5th, 1995"]').should(be.visible).click()

    browser.element('[id="subjectsInput"]').type('Maths').press_enter()
    browser.element('#subjectsInput').type('p')
    browser.all('.subjects-auto-complete__menu div').element_by(have.exact_text('Physics')).click()

    browser.element('//*[@id="hobbiesWrapper"]//label[contains(text(),"Reading")]').click()

    browser.element('[id="uploadPicture"]').send_keys(os.path.abspath('resources/Screenshot_2368.png'))

    browser.element('[id="currentAddress"]').set_value('South Street, PA, Philadelphia, 19147')

    browser.element('#state input').type('Haryana').press_enter()
    browser.element('#city input').type('Panipat').press_enter()

    browser.element('[id="submit"]').click()

    browser.element('.table-responsive').all('tr').should(
        have.exact_texts(
            'Label Values',
            'Student Name Carla Johnson',
            'Student Email Johnson@gmail.pom',
            'Gender Female',
            'Mobile 7788995511',
            'Date of Birth 05 August,1995',
            'Subjects Maths, Physics',
            'Hobbies Reading',
            'Picture Screenshot_2368.png',
            'Address South Street, PA, Philadelphia, 19147',
            'State and City Haryana Panipat',
        )
    )
    print('test finished')
    # breakpoint()
