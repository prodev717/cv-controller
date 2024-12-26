# CV Controller

**CV Controller** is an innovative computer vision project that transforms physical movements detected via a webcam into keyboard inputs (W, A, S, D) to control games. By leveraging **OpenCV**, **Mediapipe**, and **keyboard**, this project allows users to simulate directional controls through body movements, making gaming hands-free and interactive.

---

## Features
- **Real-Time Movement Detection**:
  - Tracks body movements using Mediapipe's Pose module.
  - Detects directional motion (up, down, left, right) based on keypoint displacement.
  
- **Dynamic Game Controls**:
  - Simulates keyboard presses (`W`, `A`, `S`, `D`) corresponding to the detected movement direction.
  - Supports smooth, real-time control for games or applications requiring directional input.

- **Customizable Sensitivity**:
  - Includes a threshold parameter to adjust the sensitivity of movement detection.

---

## How It Works
1. **Input via Webcam**:
   - The webcam captures real-time video feed, which is processed to identify body landmarks.

2. **Landmark Tracking**:
   - The Mediapipe Pose solution identifies body landmarks, focusing on the nose as the primary movement point.

3. **Direction Detection**:
   - Compares the current and previous positions of the tracked landmark to calculate movement direction:
     - **Up (`W`)**: If the nose moves upward.
     - **Down (`S`)**: If the nose moves downward.
     - **Left (`A`)**: If the nose moves left.
     - **Right (`D`)**: If the nose moves right.

4. **Simulated Keyboard Input**:
   - Translates the detected direction into corresponding keyboard presses using the `keyboard` library.

5. **Visual Feedback**:
   - Displays movement details (e.g., distance, direction) on the video feed for real-time debugging and feedback.

---

## Key Components
- **OpenCV**:
  - Used for video feed capture and real-time visualization.
  
- **Mediapipe**:
  - Pose estimation to track body landmarks.

- **Keyboard Library**:
  - Simulates keyboard inputs for directional control.

---

## Use Cases
- **Gaming**:
  - Control games using body movements for an immersive, hands-free experience.
  
---

## How to Quit
- Press the `q` key to stop the application.

---

## Example Output
When movements are detected, the following feedback is displayed on the screen:
1. **Difference in Position (`dif`)**: The change in x and y coordinates.
2. **Distance (`dis`)**: The Euclidean distance between the current and previous positions.
3. **Movement (`mov`)**: The detected movement direction (`w`, `a`, `s`, or `d`).

---

## Notes
- The project is configured to detect movements using the nose landmark (`nodes[0]`), but it can be adjusted for other landmarks if needed.
- The threshold for movement detection can be modified via the `thresh` variable.

---

## Contributions
Contributions to improve or extend the functionality of this project are welcome! Feel free to open issues or submit pull requests.

---

## License
This project is open-source and available under the MIT License.
