## Generated Story -4594560859633041818
* greet
    - utter_greet
    - utter_ask_form_of_address
* set_form_of_address{"form_of_address": "Frau"}
    - slot{"form_of_address": "Frau"}
    - utter_ask_first_name
* set_first_name{"first_name": "Leonie"}
    - slot{"first_name": "Leonie"}
    - utter_ask_surname
* set_surname{"surname": "Kallabis"}
    - slot{"surname": "Kallabis"}
    - utter_ask_street_address
* set_street_address{"address_street": "EineStrasse", "address_street_number": "9"}
    - slot{"address_street": "EineStrasse"}
    - slot{"address_street_number": "9"}
    - utter_ask_zip_code
* set_zip_code{"address_zip_code": "51674"}
    - slot{"address_zip_code": "51674"}
    - utter_ask_city
* set_city{"address_city": "EineStadt"}
    - slot{"address_city": "EineStadt"}
    - utter_ask_phone_number
* set_phone_number{"phone_number": "12345678"}
    - slot{"phone_number": "12345678"}
    - utter_ask_e_mail
* set_e_mail{"e_mail": "leonie@kallabis.de"}
    - slot{"e_mail": "leonie@kallabis.de"}
    - utter_ask_business_affair
* is_business_affair{"business_affair": "False"}
    - slot{"business_affair": "False"}
    - utter_ask_own_car_damaged
* is_car_damaged{"car_is_damaged": "False"}
    - slot{"car_is_damaged": "False"}
    - utter_ask_damage_caused_by_own_car
* is_damage_caused_by_own_car{"damage_from_own_car": "True"}
    - slot{"damage_from_own_car": "True"}
    - utter_ask_license_plate
* set_license_plate
    - utter_ask_date_of_damage
* set_date_of_damage{"date_of_damage": "01.01.2019"}
    - slot{"date_of_damage": "01.01.2019"}
    - utter_ask_cause_of_damage
* set_cause_of_damage{"cause_of_damage": "RoteAmpel"}
    - slot{"cause_of_damage": "RoteAmpel"}
    - utter_ask_damage_location
* set_damage_location{"damage_location": "Ampel"}
    - slot{"damage_location": "Ampel"}
    - utter_ask_description_of_accident
* set_description_of_accident{"description_of_accident": "Ampel war halt rot."}
    - slot{"description_of_accident": "Ampel war halt rot."}
    - utter_ask_current_location_of_car
* set_current_location_of_car{"current_location_of_car": "TH Koeln"}
    - slot{"current_location_of_car": "TH Koeln"}
    - utter_ask_first_name_other_insured_party
* set_first_name_other_insured_party{"first_name_insured_party": "Max"}
    - slot{"first_name_insured_party": "Max"}
    - utter_ask_surname_other_insured_party
* set_surname_other_insured_party{"surname_insured_party": "Mustermann"}
    - slot{"surname_insured_party": "Mustermann"}
    - utter_ask_phone_number_of_victim
* set_phone_number_of_victim{"phone_number_injured_party": "98765431"}
    - slot{"phone_number_injured_party": "98765431"}
    - utter_ask_insurance_number_of_victim
* set_insurance_number_of_victim{"insurance_number_injured_party": "923848484"}
    - slot{"insurance_number_injured_party": "923848484"}
    - utter_ask_insured_party_driver
* is_insured_party_driver{"insured_party_is_driver": "true"}
    - slot{"insured_party_is_driver": "true"}
    - utter_ask_is_callback_wanted

