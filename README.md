# DanceZone Blog

(Developer: Simmi Keshri)

![AmIResponsive Image]

## Live website


## Purpose of the project

DanceZone began as a blog dedicated to exploring the vibrant and diverse world of dance. Due to the overwhelming interest from professional dancers and enthusiasts, it has grown into a full-fledged platform offering dance class bookings alongside its engaging blog content. This full-stack website, built using the Django web framework, aims to transform passionate readers into active participants by providing easy access to a variety of dance classes.

The DanceZone website offers a seamless experience for users, featuring a blog that covers various dance styles, tips for beginners and seasoned dancers alike, and cultural insights into dance traditions worldwide. Registered users can also enjoy the convenience of booking dance classes directly through the website. The app allows users to schedule classes for different styles—from classical forms like Bharatanatyam and Ballet to contemporary styles like Hip Hop and Salsa. 

DanceZone’s goal is to inspire, educate, and connect dance enthusiasts while offering a streamlined platform to learn and practice with expert instructors. Whether you're here to read, learn, or dance, DanceZone is your ultimate destination for everything dance!

## Table of contents

- [Epics and user stories](#epics-and-user-stories)
   * [Epics](#epics)
   * [User stories](#user-stories)

### Epics

1. Fully functioning home page
2. Database and admin setup
3. Register page and form
4. Login page and form
5. Navigation bar that looks different when logged in
6. Blog detail page that has different capabilities when logged in compared to when not logged 
   in
7. Log out page
8. Booking page for various dance styles, that can be only accessed when logged in. This 
   includes full front-end CRUD functionality for the user

### User stories

Open a post: As a Site User, I can click on a post so that I can read the full text.

AC1 When a blog post title is clicked on a detailed view of the post is seen.

View comments: As a Site User / Admin I can view comments on an individual post so that I can read the conversation

AC1 Given one or more user comments the admin can view them.
AC2 Then a site user can click on the comment thread to read the conversation.

Account registration: As a Site User I can register an account so that I can comment on a post.

AC1 Given an email a user can register an account.
AC2 Then the user can log in.
AC3 When the user is logged in they can comment.

Comment on a post: As a Site User I can leave comments on a post so that I can be involved in the conversation

AC1 When a user comment is approved
AC2 Then a user can reply
AC3 Given more than one comment then there is a conversation thread

Modify or delete comment on a post: As a Site User I can modify or delete my comment on a post so that I can be involved in the conversation

AC1 Given a logged in user, they can modify their comment
AC2 Given a logged in user, they can delete their comment

Booking of dance class: As a Site user I can book a class so that I can enjoy the dance style I want from the available dance style

AC1 As a user I should be able to choose from dance list available
AC2 As a user I Could choose from the date available to join the dance
AC3 As a user i could choose from the time slots available

Edit and delete dance class: As a SITE USER I can edit booking so that I Can change my choice accordingly

AC1 As a user I Can edit my preference
AC2 As a user I Can delete my booking if made mistake
AC3 As a user I Can view my bookings

Manage posts: As a Site Admin I can create, read, update and delete posts so that I can manage my blog content

AC1 Given a logged in user, they can create a blog post
AC2 Given a logged in user, they can read a blog post
AC3 Given a logged in user, they can update a blog post
AC4 Given a logged in user, they can delete a blog post

Create drafts: As a Site Admin I can create draft posts so that I can finish writing the content later

AC1 Given a logged in user, they can save a draft blog post
AC2 Then they can finish the content at a later time

Approve comments: As a Site Admin I can approve or disapprove comments so that I can filter out objectionable comments

AC1 Given a logged in user, they can approve a comment
AC2 Given a logged in user, they can disapprove a comment