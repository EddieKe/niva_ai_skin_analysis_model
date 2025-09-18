Product Requirements Document: Niva - The AI Beauty Therapist
1. Project Overview
Project Name: Niva: The AI Beauty Therapist

Vision: To build a revolutionary beauty platform that uses artificial intelligence to provide personalized skincare analysis, product recommendations, and expert advice, helping users achieve and maintain optimal skin health. The app's core mission is to empower users with scientific insights and provide them with a seamless, trustworthy digital beauty therapist experience.

App Naming: We will proceed with the name Niva: AI Beauty Therapist, as it accurately reflects the app's purpose and positions it as a professional, expert-led platform.

2. Remaining Features and Functionality
This phase of development focuses on enhancing the core AI functionality and user experience.

A. Refined Recommendation Logic

Objective: To ensure that all product recommendations (skincare and makeup) are highly accurate and relevant to the user's skin profile.

Skincare: The system will use the correctly built feature vector to recommend products based on a precise analysis of the user's skin type and concerns.

Makeup: The system will standardize skin tone and type labels to ensure the makeup_recommendation function returns a curated list of relevant products instead of an empty list.

B. Enhanced Skin Analysis

Objective: To improve the accuracy and reliability of the AI analysis by integrating more robust models and a preprocessing step.

Hair Removal Script: The hair removal script will be integrated as a preprocessing step to remove visual noise from images before they are fed into the skin analysis models. This will significantly improve the accuracy of both skin type and acne level detection by giving the models a cleaner image to analyze.

Skin Tone Classifier: The inaccurate KNN model for skin tone will be replaced with a more accurate, open-source model (e.g., one based on the Monk Skin Tone Scale) to provide correct and consistent results.

Skin Disease Identification (Disclaimer): The app will, as part of the analysis, identify if a user has skin conditions or issues (e.g., acne, pigmentation) and provide a severity score. It cannot and will not diagnose or recommend treatment for medical conditions like skin cancer. If the models detect patterns that could be concerning, the app will advise the user to seek a professional medical opinion. This approach is ethical and protects users from dangerous self-diagnosis.

C. Social Sharing Features

Objective: To allow users to easily share their results and progress, promoting the app through organic social media engagement.

Shareable Media: The app will generate various shareable media formats from a user's analysis report. This includes:

PDF Report: A detailed, printable PDF document of their full skin analysis and routine.

Images: Visually appealing image files for Instagram stories and feeds.

Videos: Short, animated videos for platforms like TikTok, showcasing a "before and after" effect or a summary of their results.

D. Core Integration with the Niva App

Objective: To seamlessly integrate all new and existing features into the Flutter app's architecture.

API Integration: The Flutter app will communicate with the Python backend via a REST API. The backend will return a single, consolidated JSON object containing all the analysis, routine, and product data.

Architecture: The app will adhere to clean architecture principles with distinct layers (presentation, domain, data) and use the Bloc state management pattern for a stable and scalable user experience.

Firebase: Firebase will be used for user authentication and data management, aligning with the app's existing tech stack.

3. User Interface (UI) and Responsiveness
UI Design: The app will have a "sleek, warm, and 2050" aesthetic. This means a clean, minimalist design with a warm color palette and intuitive, futuristic animations.

Responsiveness: The app will use a single codebase that is responsive to both a web app and an Android app. This will involve using Flutter's built-in widgets and layout builders to ensure the UI adapts gracefully to different screen sizes and orientations.

4. Deployment Plan
Web App: The Flutter app will be built for the web with the command flutter build web. The resulting build/web folder can be deployed to any static hosting service (e.g., Firebase Hosting, Vercel).

Android App: A release-ready APK or app bundle will be built with flutter build apk or flutter build appbundle. This can then be signed and uploaded to the Google Play Store.

5. Work Plan (1 Week, 8-hour days)
This work plan outlines a week-long sprint, with each day dedicated to a specific set of tasks.

Day 1: Backend Integration and Testing (8 hrs)

Integrate the hair removal script as a preprocessing step in app.py.

Integrate the new skin tone model into identify_skin_tone in app.py.

Finalize the recommendation logic for both skincare and makeup in app.py.

Test the backend API with a tool like Postman to ensure a single, valid JSON response.

Day 2: Core Frontend Development (8 hrs)

Update the Flutter app to handle the new, consolidated JSON response from the backend.

Create the UI components for displaying the skin analysis results and the new, detailed skincare routine.

Implement the initial screen for the "AI Beauty Therapist" name and branding.

Day 3: Social Sharing Feature (8 hrs)

Research and integrate a Flutter package for social sharing (e.g., share_plus).

Develop the logic to generate shareable content (e.g., a "Share Your Results" button that creates a summary image or a PDF).

Design a simple, sleek UI for the sharing options.

Day 4: UI/UX Refinement (8 hrs)

Focus on the visual aesthetics of the app, implementing the "sleek, warm, and 2050" design philosophy.

Ensure the layouts are responsive for both web and mobile views.

Check that all user flows are intuitive and free of friction.

Day 5: Testing and Bug Fixes (8 hrs)

Perform a full end-to-end test of the application on both the web and a local Android emulator.

Debug and fix any bugs or crashes that arise during testing.

Optimize for performance, such as image loading times and API response speeds.


Day 6: Final Testing and Quality Assurance (8 hours)
Hours 1-3: End-to-End Testing.

Conduct a full end-to-end test of the application on both the web and a local Android emulator.

Verify that the entire user flow, from image upload to product recommendations and social sharing, works as intended.

Test the AI models with a variety of images to ensure they provide consistent and logical results.

Hours 3-5: Bug Fixing and Optimization.

Address and fix any bugs or crashes that were identified during testing.

Optimize the performance of the Flutter app, particularly focusing on image loading speeds and UI responsiveness across different devices.

Hours 5-8: Code Freeze and Documentation.

Freeze the code to prevent any new features from being added.

Create a final requirements.txt file for the Python backend and a pubspec.lock file for the Flutter app to ensure all dependencies are locked down for production.

Write a simple deployment guide in a README.md file that includes the steps for deploying to Firebase Hosting and the Google Play Store.

Day 7: Deployment (8 hours)
Hours 1-4: Web App Deployment.

Build the Flutter app for web in release mode using flutter build web. This creates an optimized production build in the build/web directory.

Use the Firebase CLI to deploy the web app to Firebase Hosting. This involves the command firebase deploy from your project's root directory, which will upload the contents of the build/web folder.

Verify that the live web app is functioning correctly on the hosted URL.

Hours 4-7: Android App Deployment.

Generate a release build of the Android app using flutter build appbundle.

Sign the app bundle with your keystore and prepare it for submission to the Google Play Store.

Use the Google Play Console to upload the app bundle and submit it for review.

Hours 7-8: Post-Deployment and Monitoring.

Integrate a monitoring tool to track the app's performance and crash reports. Firebase Crashlytics is an excellent option for this.

Set up a continuous deployment (CD) pipeline (e.g., via GitHub Actions) to automate future updates.
