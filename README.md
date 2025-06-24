# ATP Core Talent 2025
# Core Talent AI Coder Challenge: Camera Movement Detection

**Detecting Significant Camera Movement Using Image Recognition**

---

## Scenario

Imagine you are tasked with building a component for a smart camera system. Your goal is to detect **significant movement**—for example, if someone moves or tilts the camera, or if the entire camera is knocked or shifted. This is different from simply detecting moving objects in the scene.

---

## Approach

  * First, I needed to understand the code, so I asked both ChatGPT and Gemini to translate it into Java to have a better grasp of the concept.
  * I asked the AI bots how I can detect camera movements by using OpenCV.
  * After some research, I chose to implement Farneback's Optical Flow Algorithm.
  * I learned the basic concepts of Farneback's Algorithm and implemented it properly, and started testing.
  * While trying to optimize the threshold, I realized that the lower thresholds could catch object movements, so I coded a function named **detect_object_movement** to detect object movements.
  * Also, I changed the code so that if the uploaded frame is already gray-scaled, it does not try to make the frame gray-scaled.
  * In the end, I decided on proper thresholds and deployed the project on **Streamlit**.

---

## How to Run

  * To run the project on your **localhost**, run this command on your terminal:
  * **streamlit run C:\*[fill here with your file directory]*\2025\camera-movement-detection\app.py [ARGUMENTS]**
  * Or just click [*HERE*](https://atpcoretalentsrd.streamlit.app/).
  * _You can convert MP4 and GIF from [here](https://ezgif.com/split)_.

---

## Used Samples

  * Used sample gifs and video is in **sample_gifs** and **sample_video** directory with their outputs (20 fps and used while testing the sample video).
  * ***Video:*** I had to split the video in order to split it into JPG. The first 10 seconds have a significant movement, roughly between 5 and 10 seconds. I split the video at 20fps. Thus, the significant move starts at the 102nd frame (5.1 seconds). But in the second half of the video, there is no shaking, so there is no output about significant movement. Both parts have moving objects.
  * **GIF 1:** I chose this GIF to test the impact of changing lights on the app because light changes are not a move. There is no significant movement as expected.
  * **GIF 2:** I chose this GIF to test whether a significant movement of a large object counts as a significant camera move. Especially this GIF helped me a lot with threshold tuning.
  * **GIF 3:** In this gif, the person does not stop, so I want to test the app's performance. 
  * **GIF 4:** This GIF includes both moving scenarios, so it is a good example.  
