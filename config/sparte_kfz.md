## Begrüßung und allgemeine Fragen
* greet
# Wie darf ich Sie ansprechen?
* set_form_of_address{"form_of_address":"herr"}
# Wie lautet Ihr Vorname?
* set_forename{"forename":"max"}
# Dankeschön. Wie lautet Ihr Nachname?
* set_surname{"surname":"mustermann"}
# Wie lautet Ihre Straße und Hausnummer?
* set_address{"address_street":"musterstrasse", "address_street_number":"11"}
# Nennen Sie mir bitte Ihre Postleitzahl.
* set_zip_code{"address_zip_code":"12345"}
# In welchem Ort wohnen Sie?
* set_place{"address_place":"musterhausen"}
# Unter welcher Telefonnummer können wir Sie am besten erreichen?
* set_phone_number{"phone_number":"123456"}
# Wie lautet Ihre E-Mail Adresse?
* set_e_mail{"e_mail":"max@mustermann.de"}
# Handelt es sich bei Ihnen um eine gewerbliche Angelegenheit?
* is_business_affair{"business_affair":"false"}
# Welche in welcher Sparte möchten Sie einen Versicherungsfall melden
* branch_selected{"branch": "kfz"}
> follow_kfz_decision_tree

## Story, eigenes Auto beschädigt, Unfallgegner ist bei Zurich versichert und wird keine Rückrufnummer vereinbart
> follow_kfz_decision_tree
# Wurde das eigene Auto beschädigt?
* is_car_damaged{"car_is_damaged":"true"}
# Ist Ihr Unfallgegner bei der Zurich versichert?
* is_opponent_insured_at_zurich{"opponent_is_insured":"true"}
> ask_liability_insurant_contact_details

## Story, eigenes Auto nicht beschädigt, Schaden stammt vom eigenem Auto, man war selsbt am Steuer und wird keine Rückrufnummer vereinbart
> follow_kfz_decision_tree
# Wurde das eigene Auto beschädigt?
* is_car_damaged{"car_is_damaged":"false"}
# Wurde der Schaden von Ihrem Auto verursacht?
* is_damage_from_own_car{"damage_from_own_car":"true"}
# Wie lautet der Vorname des Versicherungsnehmers?
* set_forename_insured_party{"forename_insured_party":"susi"}
# Wie lautet der Nachname des Versicherungsnehmer?
* set_surname_insured_party{"surname_insured_party":"sonnenschein"}
# Falls vorhanden die Versicherungsnummer des Versicherungsnehmers.
* set_insurance_number{"insurance_number":"1234567"}
# Wie lautet der Vorname des Geschädigten?
# Wie lautet der Nachname des Geschädigten?
# Falls vorhanden geben Sie mir bitte die Telefonnummer des Geschädigten.
# Falls vorhanden bitte auch noch die Versicherungsnummer des Geschädigten.
> driver

## Saßen Sie selbst am Steuer?
> driver
* is_insured_party_driver{"insured_party_is_driver":"true"}
> finish_questioning

## Saßen Sie selbst am Steuer?
> driver
* is_insured_party_driver{"insured_party_is_driver":"true"}
# Bitte nennen Sie mir die Anrede des Fahrers.
# Wie lautet der Vorname des Fahrers?
# Wie lautet der Nachname des Fahrers?
# Wann ist das Geburtsdatum des Fahrers?
> finish_questioning

## Story, eigenes Auto nicht beschädigt, Schaden stammt vom eigenem Auto, man war selsbt am Steuer und wird keine Rückrufnummer vereinbart
> follow_kfz_decision_tree
# Wurde das eigene Auto beschädigt?
* is_car_damaged{"car_is_damaged":"false"}
# Wurde der Schaden von Ihrem Auto verursacht?
* is_damage_from_own_car{"damage_from_own_car":"false"}
> catastrophe

## Hat ein naturereignis es beschädigt?
> catastrophe
# TODO
# Wie lautet das Kennzeichen des geschädigten Autos? (z. B. ZO-E 1234)
* set_license_plate{"license_plate":"XXXX1234"}
# Wann hat der Schaden stattgefunden?
* set_date_of_damage{"date_of_damage":"12.12.2012"}
# Was war die Schadensursache? (z. B. Auffahrunfall oder Parkunfall)
* set_cause_of_damage{"cause_of_damage":"auffahrunfall"}
# Wo hat sich der Schaden ereignet? (z. B. Autobahn, innerorts)
* set_damage_lcoation{"damage_lcoation":"autobahn"}
# Bitte schildern Sie uns kurz den Unfallhergang.
* set_description_of_accident{"description_of_accident":"auto ist in anderes auto und peng"}
# Wo kann das Fahrzeug besichtigt werden?
* set_place_of_car{"place_of_car":"musterstrasse"}
# Bitte Schildern Sie uns die Sichtbaren Schäden am Fahrzeug.
# Gab es schon vorher sichtbare Schäden? Wenn ja welche?
> finish_questioning

## Hat ein naturereignis es beschädigt?
> catastrophe
# TODO

## Haftpflicht Versicherungsnehmer Kontaktdaten
> ask_liability_insurant_contact_details
# Wie lautet der Vorname des Versicherungsnehmers?
* set_forename_insured_party{"forename_insured_party":"susi"}
# Wie lautet der Nachname des Versicherungsnehmer?
* set_surname_insured_party{"surname_insured_party":"sonnenschein"}
# Falls vorhanden die Versicherungsnummer des Versicherungsnehmers.
* set_insurance_number{"insurance_number":"1234567"}
> ask_kfz_questions

## Allgemeine KFZ fragen stellen
> ask_kfz_questions
# Wie lautet das Kennzeichen des geschädigten Autos? (z. B. ZO-E 1234)
* set_license_plate{"license_plate":"XXXX1234"}
# Wann hat der Schaden stattgefunden?
* set_date_of_damage{"date_of_damage":"12.12.2012"}
# Was war die Schadensursache? (z. B. Auffahrunfall oder Parkunfall)
* set_cause_of_damage{"cause_of_damage":"auffahrunfall"}
# Wo hat sich der Schaden ereignet? (z. B. Autobahn, innerorts)
* set_damage_lcoation{"damage_lcoation":"autobahn"}
# Bitte schildern Sie uns kurz den Unfallhergang.
* set_description_of_accident{"description_of_accident":"auto ist in anderes auto und peng"}
# Wo kann das Fahrzeug besichtigt werden?
* set_place_of_car{"place_of_car":"musterstrasse"}
> finish_questioning

## Abschließende Fragen, die nach jeder Sparte folgen
> finish_questioning
# Nutzer wird gefragt, ob eine Rückrufnummer festgelegt werden soll.
* set_callback_number("want_callback_number":"true")

