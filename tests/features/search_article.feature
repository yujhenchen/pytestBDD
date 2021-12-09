Feature: Search
    A search area where you can search articles

    Scenario: search keyword selenium
        Given at the home page of the TestProject Test Automation Blog

        When I keyin the keyword
        And I click Enter on keyboard

        Then search results title contain the keyword that I searched for