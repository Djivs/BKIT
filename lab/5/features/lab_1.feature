Feature: function getEquationRoots should be able to solve biquadratic equation
    In order to make sure the function
    solves equation correctly I have the following
    test scenarios:

    Scenario Outline: Test my function
        Given I have the numbers <A>, <B> and <C>
        When I solve the equation with those numbers
        Then I expect to get <N> roots

    Examples:
        | A | B | C | D |
        | 1 | 2 | 3 | 0 |