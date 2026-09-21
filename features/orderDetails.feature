Feature: Order Details


    Test related to Order Details

Scenario Outline: Scenario Outline name: Verify the order success message shown in order details page
    Given place the item order with <username> and <password>
    And the user is on landing page
    When login to portal with <username> and <password>
    And Navigate to orders page
    And Select the order ID
    Then the order message is successfully displayed
    Examples:
        | username              | password    |
        | mahashakti@gmail.com  | Sonusanu@1  |
        | soumyashree@gmail.com | Sonusanu@1  |