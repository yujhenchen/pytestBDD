Feature: Search
    A search area where you can search articles

    Scenario: search keyword of articles
        Given navigate to the home page of the TestProject Test Automation Blog
        When I keyin <keyword> in the search field and click Enter in the keyword search field
        Then search results title contain <keyword>

        Examples: Keywords
            | keyword |
            | selenium |
            | appium |