### Product Requirements Document (PRD)

**1. Introduction**
This document outlines the requirements for an enhanced AI-powered skincare recommendation system. The goal is to provide a more seamless and valuable user experience by automating the skin analysis process and directly providing personalized product recommendations and a tailored skincare routine, eliminating the need for manual form submission after a photo scan.

**2. Problem Statement**
The existing application requires users to manually input their skin tone, skin type, and concerns after a facial scan. This creates a disjointed user flow and diminishes the value of the AI analysis. Users want a comprehensive and automated experience where they can receive immediate, actionable feedback and product recommendations based on their image analysis, without redundant manual steps.

**3. Goals**
* **Primary Goal:** To create a seamless, end-to-end user experience where a single photo scan provides a complete skin analysis and personalized product recommendations.
* **Secondary Goal:** To leverage the existing AI models for skin tone, skin type, and acne severity to provide direct value to the user.
* **Success Metrics:**
    * Increase user engagement on the recommendation page.
    * Reduce user drop-off between the photo scan and the product recommendation page.
    * Positive user feedback on the automated and personalized nature of the new flow.

**4. Non-Goals**
* This update will not include the development of a new AI model for hydration level analysis.
* The project will not involve training the existing models on new data at this time.
* The project will not redesign the overall user interface of the frontend from scratch, but will modify existing screens to support the new flow.

**5. Target Users**
* **New Users:** Individuals new to skincare who are unsure of their skin type or concerns and are looking for a simple way to find suitable products.
* **Existing Users:** Users who want to quickly find new products or track their skin's condition over time with an effortless scan.

**6. User Stories**
* **As a user,** when I upload a photo, I want the system to automatically analyze my skin and provide a comprehensive report on my skin type, skin tone, and acne severity, so I don't have to guess and manually enter the information.
* **As a user,** I want to receive a list of personalized product recommendations (e.g., cleansers, moisturizers, makeup) immediately after the scan, so I can see what products are right for me without taking additional steps.
* **As a user,** I want to see a suggested skincare routine based on my analysis results, so I can learn how to properly use the recommended products.

**7. Functional Requirements**
* **F.1: API Integration:** The Flask backend's `/upload` endpoint must be modified to call the skin classification models (`prediction_skin`, `prediction_acne`, `identify_skin_tone`) and then pass these results to the recommendation engine functions (`recs_essentials`, `makeup_recommendation`).
* **F.2: Consolidated API Response:** The `/upload` endpoint will return a single, structured JSON response containing:
    * `skin_type` (e.g., "Oily")
    * `skin_tone` (e.g., "light to medium")
    * `acne_level` (e.g., "Moderate")
    * `general_skincare_recommendations` (list of recommended products)
    * `makeup_recommendations` (list of recommended products)
* **F.3: Frontend Flow:** The React frontend will make a single API call to the `/upload` endpoint after the user submits their photo.
* **F.4: Results Display:** The frontend will have a new "Results" page that displays the data received from the API call in a user-friendly format.
* **F.5: Dynamic Routine Generation:** The frontend will implement logic to construct a simple morning and evening skincare routine based on the `skin_type` and `acne_level` from the API response.

**8. Technical Requirements**
* **T.1: Backend Modification:** Modify the `app.py` file to chain the model predictions with the recommendation functions within the `SkinMetrics` resource.
* **T.2: API Endpoint:** The existing `/upload` endpoint will be enhanced, so a new endpoint is not necessary.
* **T.3: Frontend Development:** Update the React components to handle the new JSON structure from the API response and render the results page.
* **T.4: Dependencies:** Ensure all necessary Python and JavaScript libraries are installed and compatible for the new feature.
* **T.5: Skincare Routine Logic:** The frontend will contain conditional rendering or a simple function to display a routine. For example:
    * If `skin_type` is "oily", recommend a "gel-based cleanser."
    * If `acne_level` is "Severe", recommend an "acne spot treatment" at night.

**9. Release Plan (Proposed Timeframe: 3-4 days)**
* **Day 1:** Modify the backend (`app.py`) to chain the functions and return the consolidated JSON response. Test the new API endpoint using a tool like Postman to ensure it works correctly.
* **Day 2:** Update the React frontend to make the API call and receive the new data structure. Create a basic UI to display the received skin metrics and product recommendations.
* **Day 3:** Develop the logic on the frontend to display the tailored skincare routine based on the analysis results.
* **Day 4:** Perform end-to-end testing, bug fixing, and final polish of the user interface.
