## Begrüßung und allgemeine Fragen
* greet
  - utter_greet
  - utter_ask_form_of_address
* set_form_of_address{"form_of_address":"herr"} OR set_form_of_address{"form_of_address":"frau"} OR set_form_of_address{"form_of_address":"dr"} OR set_form_of_address{"form_of_address":"doktor"}
  - utter_ask_first_name
* set_first_name{"first_name":"max"} <!-- Regex nötig -->
  - utter_ask_surname
* set_surname{"surname":"mustermann"} <!-- Regex nötig -->
  - utter_ask_street_address
* set_street_address{"address_street":"musterstrasse", "address_street_number":"11"} <!-- Regex nötig -->
  - utter_ask_zip_code
* set_zip_code{"address_zip_code":"12345"} <!-- Regex nötig -->
  - utter_ask_city
* set_city{"address_city":"musterhausen"} <!-- Regex nötig -->
  - utter_ask_phone_number
* set_phone_number{"phone_number":"123456"} <!-- Regex nötig -->
  - utter_ask_e_mail
* set_e_mail{"e_mail":"max@mustermann.de"} <!-- Überprüfung nötig -->
> follow_business_affair

## Story, business affair ist true
> follow_business_affair
- utter_ask_business_affair
* is_business_affair{"business_affair":"ja"} OR is_business_affair{"business_affair":"richtig"} OR is_business_affair{"business_affair":"korrekt"} OR is_business_affair{"business_affair":"genau"}
  - action_set_business_affair
  - slot{"business_affair":"true"}
  - utter_ask_branch_selected
* branch_selected{"branch": "kfz"}
> follow_kfz_decision_tree

## Story, business affair ist false
> follow_business_affair
- utter_ask_business_affair
* is_business_affair{"business_affair":"nein"} OR is_business_affair{"business_affair":"falsch"}
  - action_set_business_affair
  - slot{"business_affair":"false"}
  - utter_ask_branch_selected
* branch_selected{"branch": "kfz"}
> follow_kfz_decision_tree

## Story, eigenes Auto beschädigt, Unfallgegner ist bei Zurich versichert und wird keine Rückrufnummer vereinbart
> follow_kfz_decision_tree
- utter_ask_own_car_damaged
* is_car_damaged{"car_is_damaged":"wahr"} OR is_car_damaged{"car_is_damaged":"beschädigt"} OR is_car_damaged{"car_is_damaged":"ja"}
  - action_is_car_damaged
  - utter_ask_counterpart_insured_at_zurich
* is_counterpart_insured_at_zurich{"counterpart_is_insured":"true"}
> ask_liability_insurant_contact_details

## Story, eigenes Auto nicht beschädigt, Schaden stammt vom eigenem Auto, man war selsbt am Steuer und wird keine Rückrufnummer vereinbart
> follow_kfz_decision_tree
- utter_ask_own_car_damaged
* is_car_damaged{"car_is_damaged":"falsch"} OR is_car_damaged{"car_is_damaged":"unbeschädigt"} OR is_car_damaged{"car_is_damaged":"nein"}
  - action_is_car_damaged
  - utter_ask_damage_caused_by_own_car
* is_damage_caused_by_own_car{"damage_from_own_car":"wahr"} OR is_damage_caused_by_own_car{"damage_from_own_car":"ja"} OR is_damage_caused_by_own_car{"damage_from_own_car":"richtig"}
  - utter_ask_first_name_other_insured_party
* set_first_name_other_insured_party{"first_name_insured_party":"susi"}
  - utter_ask_surname_other_insured_party
* set_surname_other_insured_party{"surname_insured_party":"sonnenschein"}
  - utter_ask_insurance_number
* set_insurance_number{"insurance_number":"1234567"}
  - utter_ask_first_name_of_victim
* set_first_name_of_victim{"first_name_injured_party":"susi"}
  - utter_ask_last_name_of_victim
* set_surname_of_victim{"surname_injured_party":"sonnenschein"}
  - utter_ask_insurance_number_of_victim
* set_phone_number_of_victim{"phone_number_injured_party":"987654321"}
  - utter_ask_insurance_number_of_victim
* set_insurance_number_of_victim{"insurance_number_injured_party":"9876543210"}
> driver

## Saßen Sie selbst am Steuer?
> driver
* is_insured_party_driver{"insured_party_is_driver":"true"}
> finish_questioning

## Saßen Sie selbst am Steuer?
> driver
* is_insured_party_driver{"insured_party_is_driver":"true"}
  - utter_ask_form_of_address_of_driver
  - utter_ask_first_name_of_driver
  - utter_ask_surname_of_driver
  - utter_ask_birth_date_of_driver
> finish_questioning

## Story, eigenes Auto nicht beschädigt, Schaden stammt vom eigenem Auto, man war selsbt am Steuer und wird keine Rückrufnummer vereinbart
> follow_kfz_decision_tree
- utter_ask_own_car_damaged
* is_car_damaged{"car_is_damaged":"false"}
  - utter_ask_damage_caused_by_own_car
* is_damage_caused_by_own_car{"damage_from_own_car":"false"}
> catastrophe

## Hat ein naturereignis es beschädigt?
> catastrophe
<!-- TODO -->
- utter_ask_license_plate
* set_license_plate{"license_plate":"XXXX1234"} <!-- Regex nötig -->
  - utter_ask_date_of_damage
* set_date_of_damage{"date_of_damage":"12.12.2012"} <!-- Duckling nötig -->
  - utter_ask_cause_of_damage
* set_cause_of_damage{"cause_of_damage":"auffahrunfall"} <!-- Regex nötig -->
  - utter_ask_damage_location
* set_damage_location{"damage_location":"autobahn"} <!-- Regex nötig -->
  - utter_ask_description_of_accident
* set_description_of_accident{"description_of_accident":"auto ist in anderes auto und peng"} <!-- Regex nötig -->
  - utter_ask_current_location_of_car
* set_current_location_of_car{"current_location_of_car":"musterstrasse"} <!-- Regex nötig -->
<!-- Bitte Schildern Sie uns die Sichtbaren Schäden am Fahrzeug. -->
<!-- Gab es schon vorher sichtbare Schäden? Wenn ja welche? -->
> finish_questioning

## Hat ein naturereignis es beschädigt?
> catastrophe
<!-- TODO -->

## Haftpflicht Versicherungsnehmer Kontaktdaten
> ask_liability_insurant_contact_details
- utter_ask_first_name_insured_party
* set_first_name_insured_party{"first_name_insured_party":"susi"}
  - utter_ask_surname_insured_party
* set_surname_insured_party{"surname_insured_party":"sonnenschein"}
  - utter_ask_insurance_number
* set_insurance_number{"insurance_number":"1234567"}
> ask_kfz_questions

## Allgemeine KFZ fragen stellen
> ask_kfz_questions
- utter_ask_license_plate
* set_license_plate{"license_plate":"XXXX1234"}
  - utter_ask_date_of_damage
* set_date_of_damage{"date_of_damage":"12.12.2012"}
  - utter_ask_cause_of_damage
* set_cause_of_damage{"cause_of_damage":"auffahrunfall"}
  - utter_ask_damage_location
* set_damage_location{"damage_location":"autobahn"}
  - utter_ask_description_of_accident
* set_description_of_accident{"description_of_accident":"auto ist in anderes auto und peng"}
  - utter_ask_current_location_of_car
* set_current_location_of_car{"current_location_of_car":"musterstrasse"}
> finish_questioning

## Abschließende Fragen, die nach jeder Sparte folgen, falls callback true
> finish_questioning
- utter_ask_is_callback_wanted
* set_is_callback_wanted{"is_callback_wanted":"ja"} OR set_is_callback_wanted{"is_callback_wanted":"gerne"}
  - action_set_callback
  - slot{"is_callback_wanted":"true"}

## Abschließende Fragen, die nach jeder Sparte folgen, falls callback false
> finish_questioning
- utter_ask_is_callback_wanted
* set_is_callback_wanted{"is_callback_wanted":"nein"} OR set_is_callback_wanted{"is_callback_wanted":"ungerne"}
  - action_set_callback
  - slot{"is_callback_wanted":"false"}
