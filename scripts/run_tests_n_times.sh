#!/bin/bash

rm -R allure-results
rm -R allure-report

for ((counter = 0; counter < 3; counter++));
do
  echo Test run no.: $((counter + 1))
  
  # 1. Remove old test results 
  rm -R allure-results

  # 2. Run tests
  python -m pytest -n 2 --alluredir allure-results --browser firefox

  # 3. Copy previous history - REPORT HISTORY
  cp -r allure-report/history allure-results

  # 4. Generate a new report
  allure-2.28.0/bin/allure generate --clean allure-results

done
echo Finished test runs

allure-2.28.0/bin/allure serve allure-results