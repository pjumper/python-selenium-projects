# Created by stcra at 1/15/2024
Feature: Signin Test




 Scenario: User Signin
   Given Open Home Page
   When Click Signin
   And Click Signin Menu
   When Input chriscrayton20@gmail.com in email field
   And Input Newjob@24 in password field
   When Click Signin button
   And Click Signed in icon
   Then Verify Sign Out Link Present

 Scenario: Verify Incorrect Password Error
   Given Open Home Page
   When Click Signin
   And Click Signin Menu
   When Input chriscrayton20@gmail.com in email field
   And Input Newjob in password field
   When Click Signin button
   Then Verify That password is incorrect is present

 Scenario: Verify Incorrect Username Error
   Given Open Home Page
   When Click Signin
   And Click Signin Menu
   When Input chriscrayton@gmail.com in email field
   And Input Newjob@24 in password field
   When Click Signin button
   Then Verify We can't find your account. is present
