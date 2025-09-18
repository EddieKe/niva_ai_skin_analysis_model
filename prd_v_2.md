### Product Requirements Document (PRD)

**1. Introduction**
This document outlines the requirements for the second phase of our AI-powered skincare application: a Skin Health Tracking and Engagement system. The goal is to evolve the app from a one-time analysis tool into a habitual, long-term companion for users on their skincare journey. By allowing users to track their progress, log their routines, and receive personalized reminders, we aim to increase daily and weekly user engagement and retention.

**2. Problem Statement**
The current application provides a one-time skin analysis and product recommendation. This "one-and-done" experience does not encourage users to return to the app. To create a sustainable user base and build a valuable service, we need to provide features that help users actively monitor their skin health over time, proving the value of our recommendations and motivating continued use.

**3. Goals**
* **Primary Goal:** Implement a personal "skin diary" or photo journal to allow users to visually and quantitatively track their skin health over time.
* **Secondary Goal:** Introduce features that promote app habit formation, such as personalized reminders and progress notifications.
* **Tertiary Goal:** Use the tracked data to provide more personalized and dynamic recommendations over time.
* **Success Metrics:**
    * Increase in daily and weekly active users.
    * Average number of photos uploaded per user per month.
    * User retention rate (e.g., percentage of users who return after 30 days).

**4. Non-Goals**
* This phase will not include new AI models for skin analysis beyond what is already planned.
* The project will not integrate with physical devices (e.g., IoT skin sensors) in this phase.
* Social features (e.g., sharing progress, community forums) are out of scope for this phase.

**5. Target Users**
* **Committed Skincare Users:** Individuals who are already actively managing their skin health and are looking for a tool to help them track their progress.
* **Users with Specific Concerns:** Users with chronic skin conditions like acne or eczema who want to monitor their flare-ups and see the effectiveness of their treatments.

**6. User Stories**
* **As a user,** I want to take and store photos of my face over time so I can see the visual changes in my skin health.
* **As a user,** I want to be able to compare two photos from different dates side-by-side to easily see my before and after results.
* **As a user,** I want to log my daily routine and other factors (like diet and mood) so I can understand what affects my skin.
* **As a user,** I want to receive reminders to take a photo or perform my skincare routine so I can stay consistent.
* **As a user,** I want to see a visual graph of my skin metrics (e.g., acne severity) to track my progress over time.

**7. Functional Requirements**
* **F.1: Photo Diary:**
    * **F.1.1:** The app must allow users to capture a photo of their face.
    * **F.1.2:** Each photo must be automatically timestamped and saved securely within the app.
    * **F.1.3:** The app must have a dedicated section for viewing the photo history in a chronological format.
* **F.2: Comparison Tool:**
    * **F.2.1:** A feature to select two photos and display them side-by-side for comparison must be implemented.
* **F.3: Data Logging:**
    * **F.3.1:** Users must be able to add a daily diary entry or log to a photo, noting factors like products used, diet, or stress levels.
    * **F.3.2:** The app should record and store the AI's analysis results (skin type, tone, acne level) for each logged photo.
* **F.4: Personalized Dashboard:**
    * **F.4.1:** The app's main screen should display a summary of the user's progress.
    * **F.4.2:** This dashboard must include a simple graph or chart showing the changes in key metrics (e.g., acne severity over time).
* **F.5: Notifications and Reminders:**
    * **F.5.1:** Users must be able to set up personalized reminders for their morning and evening routines.
    * **F.5.2:** Reminders should be implemented using Flutter's notification packages, such as `flutter_local_notifications` or `firebase_messaging`, which can send messages even when the app is closed.

**8. Technical Requirements**
* **T.1: Database:** A backend database (e.g., Firebase, PostgreSQL) will be required to store user accounts, photos, AI analysis results, and daily log entries. Photos must be stored securely and privately.
* **T.2: API Endpoints:** New API endpoints will be needed to handle user-specific data, including:
    * `POST /api/user/photos`: To upload and save a new photo with its analysis.
    * `GET /api/user/photos`: To retrieve a user's photo history.
    * `POST /api/user/logs`: To save daily diary entries.
* **T.3: Frontend Development:**
    * Use Flutter packages like `image_picker` for photo capture.
    * Use a state management solution (e.g., Provider, Bloc) to handle the app's state, especially for the asynchronous API calls and data display.
    * Implement data visualization libraries (e.g., `fl_chart`) to create the progress graphs.
    * Use a package like `flutter_local_notifications` for scheduling local notifications.
* **T.4: Security:** All user data, especially photos and personal logs, must be encrypted and stored securely.

**9. Release Plan (Proposed Timeframe: 3-4 weeks)**
* **Week 1:**
    * Set up the backend database for user data storage.
    * Develop and test the API endpoints for photo and data logging.
* **Week 2:**
    * Develop the core Flutter UI for the photo diary and the ability to upload images.
    * Implement the logic to save the AI analysis results alongside each photo.
* **Week 3:**
    * Build the side-by-side comparison tool.
    * Develop the screens for daily data logging and progress graphs.
* **Week 4:**
    * Implement the personalized reminder system using push notifications.
    * Conduct final testing, bug fixing, and polish the user interface.
