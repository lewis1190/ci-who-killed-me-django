# Who Killed Me - An Online Forum to Report Cheating

![WKM Logo Banner](./readme_docs/logo_banner.png)

![Desktop Screenshot](./readme_docs/intro_screenshots/desktop.png)

## Table of Contents

Placeholder

## Introduction

"Who Killed Me" is an online forum dedicated to people pointing out when they have lost to a cheater in a video game. If the user can upload a YouTube video, they can create a post on the site, fill out some details about the incident, and share it with the community. Other users can then view the post, comment on it, and vote on whether they believe the report is valid.

The site also has a "News" section, where users can read articles about cheating in video games, updates on anti-cheat measures, and other related topics. These news articles are controlled and edited solely by site staff.

The platform was created in Django `6.0.1`, and built with Python `3.12.10`.

"Who Killed Me" can be accessed at: [https://ci-who-killed-me-748af100a7b8.herokuapp.com/](https://ci-who-killed-me-748af100a7b8.herokuapp.com/)

The GitHub Projects board for this project can be found at: [https://github.com/users/lewis1190/projects/9](https://github.com/users/lewis1190/projects/9)

## Preview Screenshots

### Desktop

<details>

<summary>Desktop Screenshot (click to expand)</summary>

![Desktop Home Page](./readme_docs/screenshots/desktop/home.png)

![Desktop Report Detail Page](./readme_docs/screenshots/desktop/report_detail.png)

![Desktop User Profile Page](./readme_docs/screenshots/desktop/user_profile.png)

</details>

### Tablet (Simulated on an iPad A16)

<details>

<summary>Tablet Screenshot (click to expand)</summary>

![Tablet Home Page](./readme_docs/screenshots/tablet/home.png)

![Tablet Report Detail Page](./readme_docs/screenshots/tablet/report_detail.png)

![Tablet User Profile Page](./readme_docs/screenshots/tablet/user_profile.png)

</details>

### Mobile (Simulated on an iPhone 12 Pro)

<details>

<summary>Mobile Screenshot (click to expand)</summary>

![Mobile Home Page](./readme_docs/screenshots/mobile/home.png)

![Mobile Report Detail Page](./readme_docs/screenshots/mobile/report_detail.png)

![Mobile User Profile Page](./readme_docs/screenshots/mobile/user_profile.png)

</details>

## Features

During this project, I wanted to implement the basic features of a forum website, along with some additional functionality to enhance the user experience. Whilst I was able to implement what I wanted for MVP, some features remain unimplemented, that I aim to design and implement properly in future updates.

### Existing Features

- **User Authentication:** Users can register for an account, log in, and log out. Passwords are securely hashed using Django's built-in authentication system.

- **Report Creation:** Authenticated users can create new reports about cheating incidents, including details such as the game, platform, description, and a YouTube video link.

- **Commenting System:** Users can comment on reports to discuss the incident, share their opinions, or provide additional information.
- **Voting System:** Users can upvote or downvote reports to indicate whether they believe the report is valid or not. The total score is displayed on the report page.

- **User Profiles:** Each user has a profile page displaying their reports. They can also update their profile picture.

- **News Section:** A dedicated section for news articles about cheating in video games, managed by site staff.

### Future Features

- **Moderation System:** Users can report posts or comments that violate the nature of the site. Moderators should be able to review these reports and take appropriate action, such as removing content or banning users / deleting accounts for repeated infractions.

  -   This feature was partially implemented, with users being able to be assigned "moderator" status through the admin panel, but no reporting system was created. Moderators will have a "[Mod]" badge next to their username when signed in.

- **Enhanced User Profiles:** Users could have more detailed profiles. I'd like them to have a bio, share their game profiles and also view their comment history.

- **Expanded filtering:** Users should be able to filter reports by game and platform.

## User Stories

User stories were grouped into milestones on GitHub. Each milestone would be represent a functional area of the site, as seen here:

![User Story Milestones](./readme_docs/milestones.png)

Below is a full list of user stories that I created when planning this project. Each user story was expanded into a list of "Acceptance Criteria" and "Tasks" that must be satisfied to mark the story as complete.

For the full, expanded user stories, please see the [GitHub Projects board](https://github.com/users/lewis1190/projects/9) for this project.

- **User Functionality:**

  - As a new user, I want to create an account with a username and password so that I can access the forum.

  - As a superadmin, I want to access an admin panel so that I can manage users, roles, and system settings.

  - As a registered user, I want to log in with my credentials so that I can access my account.

  - As a logged-in user, I want to logout so that I can end my session and protect my account.

  - As a visitor, I want to see sign-in and sign-up options on the landing page so that I can easily create an account or log in.

  - As a logged-in user, I want to view my profile so that I can see my account information and my post history.

  - As the system, I want to assign user roles so that different users have appropriate access levels.

- **User Reports Implementation**

  - As a logged-in user, I want to create a post reporting a suspected cheater so that the community can review the evidence.

  - As a user, I want to view the complete details of a post so that I can see all the evidence and information about a reported cheater.

  - As a user, I want to search for posts about a specific in-game username so that I can find reports about particular players.

  - As a visitor, I want to see the top 5 most popular posts from the current month on the landing page so that I can quickly find trending reports.

  - As a logged-in user, I want to upvote or downvote posts so that I can indicate whether I find the report credible.

  - As a logged-in user, I want to comment on posts so that I can discuss the evidence and share opinions.

- **News Blog Implementation**

  -   As a site visitor, both logged in and not, I want to access the news reports that the site publishes.

- **Moderator Functionality Implementation**

  - As a moderator, I want to access a moderation panel so that I can review and manage user reports.

  - As a user, I want to report inappropriate posts or comments so that moderators can review them for violations.

## Planning / User Experience / UX Design

### Typography: Font Choices

When choosing a font, I wasn't too worried about sticking to a particular style or brand. I was much more focused on readability and accessibility between different devices and operating systems.

After a bit of online research, I discovered a CSS rule called `system-ui`, which allows the browser to choose a font based on the user's system. This means that Windows, iOS and Android will all resolve to different fonts, but each one will be optimized for readability on that specific system, and also feel familiar to the user.

Below is a simple table on what fonts will be resolved on each system:

| Operating System | Resolved Font          |
| ---------------- | ---------------------- |
| Windows 10       | Segoe UI               |
| Windows 11       | Segoe UI Variable      |
| macOS            | San Francisco (SF Pro) |
| iPhone (iOS)     | San Francisco (SF Pro) |
| iPad (iPadOS)    | San Francisco (SF Pro) |
| Android          | Roboto                 |

A bonus from this also ensures that the site will load faster, as the browser does not need to download any additional font files.

### Typography: Color Palette

![Color Palette](./readme_docs/color_palette.png)

When thinking about the kind of colors I'd like to use on the site, I drew on my experience as being a part of the target audience for this project. Many gaming platforms, such as Steam and Epic Games Store, use dark themes **by default**, with high contrast elements to make the content stand out.

The color palette shown above achieved exactly what I wanted. I used a pair of dark navy/blue colors for the background and foreground elements, with white for text. For accent text, a bright red was used, and green was the primary color used for the buttons.

### Wireframes

I used [Penpot](https://penpot.app/) to create wireframes for the main pages of the site. Penpot is an open-source design and prototyping tool, which allowed me to be very specific with my designs, without the cost of paid tools like Figma or Adobe XD.

For my sitemap, I use [Miro](https://miro.com/) to create a simple flowchart of how the pages would link together. I then took a screenshot of this and pasted it into Penpot, to keep everything in one place.

Please note that some areas of my site, such as the "News", "About" and "User Profile" pages were not included in the wireframes, as I wanted to see how the AI tools at my disposal could take my implemented features, and stay consistent with the existing designs to create these additional pages. More on this later in the ["How AI Was Used in This Project"](#how-ai-was-used-in-this-project) section.

The exported wireframes can be seen below:

---
<details>

<summary>Sitemap (Click to Expand)</summary>

![Sitemap](./readme_docs/wireframes/sitemap.webp)

</details>

---

<details>

<summary>Homepage (Click to Expand)</summary>

![Home Page](./readme_docs/wireframes/home.webp)

</details>

---

<details>

<summary>Sign Up / Log In (Click to Expand)</summary>

![Sign Up / Log In](./readme_docs/wireframes/sign_up_login.webp)

</details>

---

<details>

<summary>SuperAdmin Block Page (Click to Expand)</summary>

![SuperAdmin Block Page](./readme_docs/wireframes/superadmin_block_page.webp)

</details>

---

<details>

<summary>Top Posts Page (Click to Expand)</summary>

![Top Posts Page](./readme_docs/wireframes/top_posts_page.webp)

</details>

---

<details>

<summary>Username Search Results (Click to Expand)</summary>

![Username Search Results](./readme_docs/wireframes/username_search_results.webp)

</details>

---

<details>

<summary>View Moderation Reports (Click to Expand)</summary>

![View Moderation Reports](./readme_docs/wireframes/view_moderation_reports.webp)

</details>

---

<details>

<summary>New Post Page (Click to Expand)</summary>

![New Post Page](./readme_docs/wireframes/new_post_page.webp)

</details>

---

<details>

<summary>Post Details Page (Click to Expand)</summary>

![Post Details Page](./readme_docs/wireframes/post_details_page.webp)

</details>

---

### Database Design

When designing the database schema for this project, I used [dbdiagram.io](https://dbdiagram.io/) to create an Entity-Relationship Diagram (ERD).

The biggest advantage that this tool provided was the ability to use the DBML (Database Markup Language) to "code" my database structure, rather than using a visual-first platform with drag-and-drop features. This ensured that I took care with the relationships between tables. If something didn't work when coding in DBML, it definitely wasn't going to work when implementing the real models in Django.

Over the project, the ERD changed a few times as I adjusted the scope of my project in-line with time constraints and to avoid scope creep. Below is the initial ERD that I started with, and the ERD that reflects the current functionality of the platform.

#### Initial ERD

![Initial ERD](./readme_docs/erds/1/erd1.png)
*1. The initial ERD created at during my "design" phase.*

#### Final ERD

![Final ERD](./readme_docs/erds/2/erd2.png)
*2. The final ERD that reflects the current functionality of the platform.*

## Agile Project Management

The project was managed using Agile methodologies, with user stories and tasks tracked on a GitHub Projects board. As the assignment length was 3 weeks, I used the **scrum** framework to break the project down into 3 separate phases:

- **Phase / Week 1 - Planning and Design:** Gathering requirements, creating user stories, designing wireframes, and creating the ERD.

- **Phase / Week 2 - Development:** Setting up the development environment and repo, implementing core features, and conducting initial testing.

- **Phase / Week 3 - Testing, Deployment, Documentation:** Unit and manual testing, bug fixing, edge-case handling, deployment, and documentation.

### GitHub Projects Board

All user stories were tracked on a GitHub Projects board. The board was divided into four columns:

- **Backlog:** Any user story starts here, including those that may not be worked on for MVP.

- **Todo:** User stories that were planned to be worked on **soon**. For example, if I was working on the "New Blog" feature, all user stories within that milestone would be moved to this column.

- **In Progress:** User stories that were actively being worked on, fixed or tested.

- **Done:** User stories that are fully-satisfied, and deployed to Heroku. Any required database migrations have also been run.

### GitHub Repo Branch Methodology

![Git Branching Strategy](./readme_docs/github-branches.png)\
*1. All branches created during the course of this assignment.*

I decided to adopt the "Feature Branch" workflow for this project. I set myself the following rules:

- The `main` branch always contains production-ready code.

- The `develop` branch contains the latest completed features that are ready for manual testing before the next release. Once I'm satisfied with the changes, I would create a Pull Request from `develop` to `main`, and deploy the changes to Heroku.

- A `feat/*` branch would be created for each milestone within my project. For example, the news blog feature was implemented in a branch called `feat/news`.

- A `chore/*` branch would be created for any non-feature work, small bugs, UI tweaks, code formatting or fixing linting errors.

  -   I used a generic `chore/cleanup` branch for all of my tweaks, as having a branch for each small change would have caused a lot of additional administrative overhead for the project. However, if this were a larger project with multiple developers, the extra overhead would be required.

## Testing and Quality Assurance

### Ensuring Security

### Manual Testing

### Automated Testing - Unit Tests

### Lighthouse Auditing

### Validation Testing - HTML

### Validation Testing - CSS

### Validation Testing - JavaScript

### Validation Testing - Python

## How AI Was Used in This Project

## Deployment

## Credits
