Feature: Search
    A search area where you can search articles

    Scenario: search keyword selenium
        Given navigate to the home page of the TestProject Test Automation Blog
        When I keyin the keyword in the keyword search field and click Enter on keyboard in the keyword search field
        Then search results title contain the keyword that I searched for