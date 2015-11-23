Feature: Searching python on google

Background:
Given I am on Google Site

Scenario:  Searching python
    When I search for python
    Then I must see python on results
