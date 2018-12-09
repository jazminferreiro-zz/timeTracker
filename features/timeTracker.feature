Feature: showing off behave

  Scenario: run a simple test
     Given we have behave installed
      When we implement a test
      Then behave will test it for us!

  Scenario: Setup Table
     Given a set of project:
        | proyecto  | tarea	|
        | proy1     | t1	|   		  
        | proy2     | t2	|
        | proy1		| t3	|
    When we hacemos algo
    Then we will find el proyecto "proy1"
      

