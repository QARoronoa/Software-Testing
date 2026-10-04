from faker import Faker


faker = Faker("FR_fr")

class BillingAddress:

    @staticmethod
    def formulaire_adress():
        return {
            "first_name": faker.first_name(),
            "last_name": faker.last_name(),
            "address": faker.street_address(),
            "city": faker.city(),
            "post_code": 92350
        }