## Begrüßung und allgemeine Fragen
* greet
# Wie darf ich Sie ansprechen?
# Wie lautet Ihr Vorname?
# Dankeschön. Wie lautet Ihr Nachname?
# Wie lautet Ihre Straße und Hausnummer?
# Nennen Sie mir bitte Ihre Postleitzahl.
# In welchem Ort wohnen Sie?
# Unter welcher Telefonnummer können wir Sie am besten erreichen?
# Wie lautet Ihre E-Mail Adresse?
# Handelt es sich bei Ihnen um eine gewerbliche Angelegenheit?
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

## Haftpflicht Versicherungsnehmer Kontaktdaten
> ask_liability_insurant_contact_details
# Wie lautet der Vorname des Versicherungsnehmers?
# Wie lautet der Nachname des Versicherungsnehmer?
# Falls vorhanden die Versicherungsnummer des Versicherungsnehmers.
> ask_kfz_questions

## Allgemeine KFZ fragen stellen
> ask_kfz_questions
# Wie lautet das Kennzeichen des geschädigten Autos? (z. B. ZO-E 1234)
# Wann hat der Schaden stattgefunden?
# Was war die Schadensursache? (z. B. Auffahrunfall oder Parkunfall)
# Wo hat sich der Schaden ereignet? (z. B. Autobahn, innerorts)
# Bitte schildern Sie uns kurz den Unfallhergang.
# Wo kann das Fahrzeug besichtigt werden?
> finish_questioning

## Abschließende Fragen, die nach jeder Sparte folgen
> finish_questioning
# Nutzer wird gefragt, ob eine Rückrufnummer festgelegt werden soll.
* set_callback_number("want_callback_number":"true")

