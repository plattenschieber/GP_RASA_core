## Begrüßung und Kontaktdaten aufnehmen, business affair true, Auto wurde beschädigt, Unfallgegner ist bei Zurich versichert, Rückruf erwünscht
* greet
  - utter_greet
  - action_ask_contact_details
  - slot{"requested_slot" : "form_of_address"}
* set_form_of_address{"form_of_address":"herr"}
  - action_ask_contact_details
  - slot{"form_of_address":"herr"}
  - slot{"requested_slot":"first_name"}
* set_first_name{"first_name":"max"} <!-- Regex nötig -->
  - action_ask_contact_details
  - slot{"first_name":"max"}
  - slot{"requested_slot":"surname"}
* set_surname{"surname":"mustermann"} <!-- Regex nötig -->
  - action_ask_contact_details
  - slot{"surname":"mustermann"}
  - slot{"requested_slot":"street_address"} 
* set_street_address{"street_address":"musterstrasse 11"} <!-- Regex nötig -->
  - action_ask_contact_details
  - slot{"street_address":"musterstrasse 11"}
  - slot{"requested_slot":"address_zip_code"}
* set_zip_code{"address_zip_code":"12345"} <!-- Regex nötig -->
  - action_ask_contact_details
  - slot{"address_zip_code":"12345"}
  - slot{"requested_slot":"address_city"}
* set_city{"address_city":"musterhausen"} <!-- Regex nötig -->
  - action_ask_contact_details
  - slot{"address_city":"musterhausen"}
  - slot{"requested_slot":"phone_number"}
* set_phone_number{"phone_number":"123456"} <!-- Regex nötig -->
  - action_ask_contact_details
  - slot{"phone_number":"123456"}
  - slot{"requested_slot":"e_mail"}
* set_e_mail{"e_mail":"max@mustermann.de"} <!-- Überprüfung nötig -->
  - action_ask_contact_details
  - slot{"e_mail":"max@mustermann.de"}
  - slot{"requested_slot":"business_affair"}
* confirm
  - action_ask_contact_details
  - slot{"business_affair":true}
  - action_ask_branch
  - slot{"requested_slot":"branch"}
* branch_selected{"branch": "kfz"}
  - action_ask_car_is_damaged
  - slot{"branch": "kfz"}
  - slot{"requested_slot":"car_is_damaged"}
* confirm 
  - action_ask_car_is_damaged
  - slot{"car_is_damaged":true}
  - slot{"requested_slot":"counterpart_is_insured"}
  - action_ask_counterpart_insured_at_zurich
* confirm
  - slot{"counterpart_is_insured":true}
  - slot{"requested_slot":"first_name_insured_party"}
  - action_ask_liability_contact_data
 * set_first_name_insured_party{"first_name_insured_party":"susi"}
  - slot{"first_name_insured_party":"susi"}
  - slot{"requested_slot":"surname_insured_party"}
  - action_ask_liability_contact_data
* set_surname_insured_party{"surname_insured_party":"sonnenschein"}
  - slot{"surname_insured_party":"sonnenschein"}
  - slot{"requested_slot":"insurance_number"}
  - action_ask_liability_contact_data
* set_insurance_number{"insurance_number":"1234567"}
  - slot{"insurance_number":"1234567"}
  - slot{"requested_slot":"license_plate"}
  - action_ask_kfz
* set_license_plate{"license_plate":"XXXX1234"}
  - slot{"license_plate":"XXXX1234"}
  - slot{"requested_slot":"date_of_damage"}
  - action_ask_kfz
* set_date_of_damage{"date_of_damage":"12.12.2012"}
  - slot{"date_of_damage":"12.12.2012"}
  - slot{"requested_slot":"cause_of_damage"}
  - action_ask_kfz
* set_cause_of_damage{"cause_of_damage":"auffahrunfall"}
  - slot{"cause_of_damage":"auffahrunfall"}
  - slot{"requested_slot":"damage_location"}
  - action_ask_kfz
* set_damage_location{"damage_location":"autobahn"}
  - slot{"damage_location":"autobahn"}
  - slot{"requested_slot":"description_of_accident"}
  - action_ask_kfz
* set_description_of_accident{"description_of_accident":"auto ist in anderes auto und peng"}
  - slot{"description_of_accident":"auto ist in anderes auto und peng"}
  - slot{"requested_slot":"current_location_of_car"}
  - action_ask_kfz
* set_current_location_of_car{"current_location_of_car":"musterstrasse"}
  - slot{"current_location_of_car":"musterstrasse"}
  - slot{"requested_slot":"is_callback_wanted"}
  - action_ask_is_callback_wanted
* confirm
  - slot{"is_callback_wanted":true}
  - slot{"requested_slot":"callback_phone_number"}
  - action_ask_callback_information
* set_callback_phone_number{"callback_phone_number":"2345678"}
  - slot{"callback_phone_number":"2345678"}
  - slot{"requested_slot":"reachability_date"}
  - action_ask_callback_information
* set_date_and_time_reachability{"reachability_date":"18.09.2018 18:00"}
  - slot{"reachability_date":"18.09.2018 18:00"}
  - utter_goodbye
  - action_send_email