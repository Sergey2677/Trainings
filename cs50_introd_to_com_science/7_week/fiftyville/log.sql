-- Keep a log of any SQL queries you execute as you solve the mystery.
-- Keep a log of any SQL queries you execute as you solve the mystery.

-- At first I was looking for a crime id
SELECT *
FROM crime_scene_reports
WHERE year = 2021
AND month = 7
AND day = 28
AND street = 'Humphrey Street';


-- Updating the search parameters with the exact date
SELECT *
FROM interviews
WHERE transcript
LIKE "%bakery%"
AND day = 28;


-- Compare the id of those who checked out of the parking lot and called someone in the time range of July 28, 2021 10:15-10:25 with the id of those who withdrew cash from the ATM
SELECT *
FROM atm_transactions
WHERE day =28
AND account_number
IN (
-- Select the account number from the bank accounts where the person's id is on the list of people who checked out of the parking lot and called in the time range of 10:15-10:25
SELECT account_number
FROM bank_accounts
WHERE person_id IN (
-- Select the identifier from the people table whose license plate belongs to the people who called and checked out of the parking lot at the same time
SELECT id
FROM people
WHERE license_plate IN (
-- Select license plates that meet the above parameters
SELECT bsl.license_plate
FROM bakery_security_logs AS bsl
JOIN people AS p
ON bsl.license_plate = p.license_plate
JOIN phone_calls AS pc
ON pc.caller = p.phone_number
WHERE (pc.duration < 60)
AND (bsl.year = 2021
AND bsl.month = 7
AND bsl.day = 28
AND bsl.hour = 10
AND bsl.minute BETWEEN 15 AND 25
AND bsl.activity = 'exit'))));


-- Find all the information about the people with the founded id
SELECT *
FROM people
WHERE id IN (
SELECT person_id
FROM bank_accounts
WHERE account_number IN ('49610011', '26013199'));

-- Find all flights` id of these passengers
SELECT *
FROM passengers
WHERE passport_number IN ('3592750733', '5773159633');

-- Find the earliest flight
SELECT *
FROM flights
WHERE id IN ('18', '24', '36', '54')
AND day = 29
ORDER BY hour
LIMIT 1;

-- The city the thief ESCAPED TO:
SELECT *
FROM airports
WHERE id = 4;

-- The THIEF is:
SELECT name
FROM people
WHERE passport_number = (
SELECT passport_number
FROM passengers
WHERE flight_id = 36
AND passport_number IN ('3592750733', '5773159633'));

-- Find ACCOMPLICE telephone number
SELECT *
FROM phone_calls
WHERE year = 2021
AND month = 7
AND day = 28
AND duration < 60
AND caller = (
SELECT phone_number
FROM people
WHERE passport_number = (
SELECT passport_number
FROM passengers
WHERE flight_id = 36
AND passport_number IN ('3592750733', '5773159633')));

-- FIND ACCOMPLICE name
SELECT name FROM people WHERE phone_number = '(375) 555-8161';
