Feature: showing off behave

  Scenario: run a simple test
     Given we have behave installed
      When we implement a test
      Then behave will test it for us!

  Scenario: run a project simple test
      Given a project with name p1
      When we look for the name
      Then it is p1

  Scenario: run a task simple test
      Given a task with name t1 and project name p1
      When we look for the task name
      Then it is t1


  Scenario: Setup Table
     Given a set of project:
        | proyecto  | tarea	|
        | proy1     | t1	|   		  
   
    When nothing happens
    Then we will find that "t1" belongs to the proyecto: "proy1"

  Scenario: add hours
      Given a developer
      When we add hour
      Then we will find an hour created
      

 Scenario: add hour validation
      Given a developer
      When we try to add hours with not project
      Then it show message "El proyecto es obligatorio"

      Given a developer
      When we try to add hours with black project
      Then it show message "El proyecto es obligatorio"

      Given a developer
      When we try to add a not integer quantity value
      Then it show message "La cantidad de horas debe ser un valor positivo mayor a uno"

      Given a developer
      When we try to add more than 24 hours
      Then it show message "La cantidad de horas debe ser menor a 24"

      Given a developer
      When we try to we try to add hours vith no date
      Then it show message "La fecha es obligatoria"

      Given a developer
      When we try to add hours vith invalid date format
      Then it show message "La fecha es obligatoria"


      Given a developer
      When we try to add hours vith None task index
      Then it show message "La tarea es obligatoria"

      Given a developer
      When we try to add hours vith invalid task index
      Then it show message "La tarea es obligatoria"

      Given a developer
      When we try to add hours to a task we are not assigned to
      Then it show message "La tarea: tarea0 no esta a cargo de este desarrollador"

      Given a developer
      When we try to add more than 24 hours of work for the same day
      Then it show message "La cantidad total de horas cargadas por dia debe ser menor o igual a 24"

      Given a developer
      When we try to add hour with invalid task
      Then it show message "La tarea: tarea3 no esta disponible"