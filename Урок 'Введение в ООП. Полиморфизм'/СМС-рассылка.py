class Person:
    def __init__(self, name, patronymic, suname, telephone):
        self.name = name
        self.patronymic = patronymic
        self.surname = suname
        self.telephones = telephone

    def get_phone(self):
        if "private" in self.telephones:
            return self.telephones["private"]
        else:
            return None

    def get_work_phone(self):
        if "work" in self.telephones:
            return self.telephones["work"]
        else:
            return None

    def get_sms_text(self):
        return f"Уважаемый {self.name} {self.patronymic}! Примите у" \
            f"частие в" \
            f" нашем беспроигрышном конкурсе для физических лиц"


class Company:
    def __init__(self, name_of_company, type_of_company, telephones_of_company,
                 *workers_of_company):
        self.name_of_company = name_of_company
        self.type = type_of_company
        self.tel = telephones_of_company
        self.lst_workers = workers_of_company

    def get_phone(self):
        if "contact" in self.tel:
            return self.tel["contact"]
        else:
            for i in self.lst_workers:
                if i.get_work_phone():
                    return i.get_work_phone()
        return None

    def get_name(self):
        return self.name_of_company

    def get_sms_text(self):
        return f"Для компании {self.name_of_company} есть супе" \
            f"р предложение! Примите участие в нашем беспроигрышном " \
            f"конкурсе для {self.type}"


def send_sms(*args):
    for i in args:
        if isinstance(i, Person):
            if not i.get_phone():
                print(f"Не удалось отправить сообщение абоненту: {i.surname} "
                      f"{i.name} {i.patronymic}")
            else:
                print(f"Отправлено СМС на номер {i.get_phone()} с текстом:"
                      f" {i.get_sms_text()}")
        elif isinstance(i, Company):
            if not i.get_phone():
                print(f"Не удалось отправить сообщение абоненту: "
                      f"{i.name_of_company}")
            else:
                print(f"Отправлено СМС на номер {i.get_phone()} с текстом: "
                      f"{i.get_sms_text()}")
