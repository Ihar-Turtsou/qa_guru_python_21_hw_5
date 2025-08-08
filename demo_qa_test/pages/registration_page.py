from selene import browser, have, be, by
from demo_qa_test import resource


class RegistrationPage:
    def open(self):
        browser.open('/automation-practice-form')
        browser.execute_script('window.scrollBy(0, 500)')
        return self

    def fill_first_name(self, value):
        browser.element('[id="firstName"]').type(value)
        return self

    def fill_last_name(self, value):
        browser.element('[id="lastName"]').type(value)
        return self

    def fill_birthday(self, month, year, day):
        browser.element('[id = "dateOfBirthInput"]').click()
        browser.all('.react-datepicker__month-select option').element_by(have.exact_text(month)).click()
        browser.all('.react-datepicker__year-select option').element_by(have.exact_text(year)).click()
        browser.all(f'.react-datepicker__day:not(.react-datepicker__day--outside-month)').element_by(have.exact_text(str(int(day)))).click()
        return self

    def fill_email(self, email):
        browser.element('[id="userEmail"]').type(email)
        return self

    def set_gender(self, value):
        browser.element('#genterWrapper').element(by.text(value)).click()
        return self

    def fill_phone_number(self, value):
        browser.element('[id="userNumber"]').type(value)
        return self

    def set_subject_by_enter(self, value):
        browser.element('[id="subjectsInput"]').type(value).press_enter()
        return self

    def set_subject_by_click(self, type_letter, value):
        browser.element('#subjectsInput').type(type_letter)
        browser.all('.subjects-auto-complete__menu div').element_by(have.exact_text(value)).click()
        return self

    def set_hobby(self, value):
        browser.element('#hobbiesWrapper').element(by.text(value)).click()
        return self

    def upload_picture(self, value):
        browser.element('[id="uploadPicture"]').send_keys(resource.path(value))
        return self

    def fill_current_address(self, value):
        browser.element('[id="currentAddress"]').set_value(value)
        return self

    def choose_location(self, state, city):
        browser.element('#state input').type(state).press_enter()
        browser.element('#city input').type(city).press_enter()
        return self

    def submit_form(self):
        browser.element('[id="submit"]').click()
        return self

    def should_have_registered_user_with(self,
                                   full_name,
                                   email,
                                   gender,
                                   phone_number,
                                   birthday,
                                   subjects,
                                   hobby,
                                   file_name,
                                   address,
                                   state_city):
        (browser.all('tbody tr td:nth-child(2)')
        .should(have.exact_texts(
            full_name,
            email,
            gender,
            phone_number,
            birthday,
            subjects,
            hobby,
            file_name,
            address,
            state_city
        )))
        return self
