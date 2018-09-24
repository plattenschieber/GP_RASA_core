## Begrüßung und Kontaktdaten aufnehmen
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
> follow_business_affair

## Story, business affair ist true
> follow_business_affair
* confirm
  - action_ask_contact_details
  - slot{"business_affair":true}
  - action_ask_branch
  - slot{"requested_slot":"branch"}
* branch_selected{"branch": "kfz"}
  - action_ask_car_is_damaged
  - slot{"branch": "kfz"}
  - slot{"requested_slot":"car_is_damaged"}
> follow_kfz_decision_tree

## Story, business affair ist false
> follow_business_affair
* deny
  - action_ask_contact_details
  - slot{"business_affair":false}
  - action_ask_branch
  - slot{"requested_slot":"branch"}
* branch_selected{"branch": "kfz"}
  - action_ask_car_is_damaged
  - slot{"branch": "kfz"}
  - slot{"requested_slot":"car_is_damaged"}
> follow_kfz_decision_tree

## Story, eigenes Auto beschädigt, Unfallgegner bei Zurich versichert
> follow_kfz_decision_tree
* confirm 
  - action_ask_car_is_damaged
  - slot{"car_is_damaged":true}
  - slot{"requested_slot":"counterpart_is_insured"}
  - action_ask_counterpart_insured_at_zurich
* confirm
  - action_ask_counterpart_insured_at_zurich
  - slot{"counterpart_is_insured":true}
  - slot{"requested_slot":"first_name_insured_party"}
  - action_ask_liability_contact_data
> ask_liability_insurant_contact_details

## Story, eigenes Auto beschädigt, Unfallgegner nicht bei Zurich versichert
> follow_kfz_decision_tree
* confirm 
  - action_ask_car_is_damaged
  - slot{"car_is_damaged":true}
  - slot{"requested_slot":"counterpart_is_insured"}
  - action_ask_counterpart_insured_at_zurich
* deny
  - action_ask_counterpart_insured_at_zurich
  - slot{"counterpart_is_insured":true}
  - utter_abbruch
  
## Haftpflicht Versicherungsnehmer Kontaktdaten
> ask_liability_insurant_contact_details
* set_first_name_insured_party{"first_name_insured_party":"susi"}
  - action_ask_liability_contact_data
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
> ask_kfz_questions

## Allgemeine KFZ fragen stellen
> ask_kfz_questions
* set_license_plate{"license_plate":"XXXX1234"}
  - action_ask_kfz
  - slot{"license_plate":"XXXX1234"}
  - slot{"requested_slot":"date_of_damage"}
* set_date_of_damage{"date_of_damage":"12.12.2012"}
  - action_ask_kfz
  - slot{"date_of_damage":"12.12.2012"}
  - slot{"requested_slot":"cause_of_damage"}
* set_cause_of_damage{"cause_of_damage":"auffahrunfall"}
  - action_ask_kfz
  - slot{"cause_of_damage":"auffahrunfall"}
  - slot{"requested_slot":"damage_location"}
* set_damage_location{"damage_location":"autobahn"}
  - action_ask_kfz
  - slot{"damage_location":"autobahn"}
  - slot{"requested_slot":"description_of_accident"}
* set_description_of_accident{"description_of_accident":"auto ist in anderes auto und peng"}
  - action_ask_kfz
  - slot{"description_of_accident":"auto ist in anderes auto und peng"}
  - slot{"requested_slot":"current_location_of_car"}
* set_current_location_of_car{"current_location_of_car":"musterstrasse"}
  - slot{"current_location_of_car":"musterstrasse"}
  - slot{"requested_slot":"is_callback_wanted"}
  - action_ask_is_callback_wanted
> finish_questioning

## Story, eigenes Auto nicht beschädigt
> follow_kfz_decision_tree
* deny
  - action_ask_car_is_damaged
  - slot{"car_is_damaged":false}
  - slot{"requested_slot":"damage_from_own_car"}
  - action_ask_is_damage_caused_by_own_car
> ask_damage_caused_by_own_car

## Story, Schaden stammt nicht vom eigenen Auto
> ask_damage_caused_by_own_car
* deny
  - action_ask_is_damage_caused_by_own_car
  - slot{"damage_from_own_car":false}
  - utter_abbruch
  <!--TBD: Branch "catastrophe"-->

## Story, Schaden stammt vom eigenem Auto, man war selbst am Steuer 
> ask_damage_caused_by_own_car
* confirm
  - action_ask_is_damage_caused_by_own_car
  - slot{"damage_from_own_car":true}
  - slot{"requested_slot":"first_name_insured_party"}
  - action_ask_kfz_other_party
* set_first_name_other_insured_party{"first_name_insured_party":"susi"}
  - action_ask_kfz_other_party
  - slot{"first_name_insured_party":"susi"}
  - slot{"requested_slot":"surname_insured_party"}
* set_surname_other_insured_party{"surname_insured_party":"sonnenschein"}
  - action_ask_kfz_other_party
  - slot{"surname_insured_party":"sonnenschein"}
  - slot{"requested_slot":"insurance_number"}
* set_insurance_number{"insurance_number":"1234567"}
  - action_ask_insured_party_driver
  - slot{"insurance_number":"1234567"}
  - slot{"requested_slot":"insured_party_is_driver"}
> driver

## Saßen Sie selbst am Steuer? Ja
> driver
* confirm 
  - action_ask_insured_party_driver
  - slot{"insured_party_is_driver":true}
  - slot{"requested_slot":"license_plate"}
  - action_ask_kfz
> ask_kfz_questions

## Saßen Sie selbst am Steuer? Nein
> driver
* deny
  - action_ask_insured_party_driver
  - slot{"insured_party_is_driver":false}
  - slot{"requested_slot":"form_of_address_of_driver"}
  - action_ask_insured_party_driver_informations
* set_form_of_address_of_driver{"form_of_address_of_driver":"herr"}
  - action_ask_insured_party_driver_informations
  - slot{"form_of_address_of_driver":"herr"}
  - slot{"requested_slot":"first_name_of_driver"}
* set_first_name_of_driver{"first_name_of_driver":"maxi"}
  - action_ask_insured_party_driver_informations
  - slot{"first_name_of_driver":"maxi"}
  - slot{"requested_slot":"surname_of_driver"}
* set_surname_of_driver{"surname_of_driver":"mustermanni"}
  - action_ask_insured_party_driver_informations
  - slot{"surname_of_driver":"mustermanni"}
  - slot{"requested_slot":"birth_date_of_driver"}
* set_birth_date_of_driver{"birth_date_of_driver":"01.01.1990"}
  - action_ask_insured_party_driver_informations
  - slot{"birth_date_of_driver":"01.01.1990"}
  - slot{"requested_slot":"license_plate"}
  - action_ask_kfz
> ask_kfz_questions

## Abschließende Fragen, die nach jeder Sparte folgen
> finish_questioning
* confirm
  - action_ask_is_callback_wanted
  - slot{"is_callback_wanted":true}
  - slot{"requested_slot":"callback_phone_number"}
  - action_ask_callback_information
* set_callback_phone_number{"callback_phone_number":"2345678"}
  - action_ask_callback_information
  - slot{"callback_phone_number":"2345678"}
  - slot{"requested_slot":"reachability_date"}
* set_date_and_time_reachability{"reachability_date":"18.09.2018 18:00"}
  - action_ask_callback_information
  - slot{"reachability_date":"18.09.2018 18:00"}
  - utter_goodbye
  - action_send_email
  
## Abschließende Fragen, die nach jeder Sparte folgen
> finish_questioning
* deny
  - action_ask_is_callback_wanted
  - slot{"is_callback_wanted":false}
  - utter_goodbye
  - action_send_email