Feature: Searching home on google

Background:
Given I am on Google Site

Scenario:  Searching home
    When I search for home
    Then I must see home on results
