#!/bin/bash

rm -R allure-results
rm -R reports/allure-results
mkdir -p reports/allure-results/history

for ((counter = 0; counter < 2; counter++));
do
  echo Test run no.: $((counter + 1))
  
  # 1. Remove old test results 
  rm -R reports/allure-results/*
  # rm -R allure-report/*

  # 2. Run tests
  python -m pytest --alluredir allure-results
  
  # 3. Copy previous history - REPORT HISTORY
  cp -r allure-report/history reports/allure-results/

  # 4. Generate a new report
  allure-2.28.0/bin/allure generate --clean allure-results

done
echo Finished test runs

cp -r reports/allure-results/* allure-results/
allure-2.28.0/bin/allure serve allure-results