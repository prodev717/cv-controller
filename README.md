# CV Controller

**CV Controller** is an innovative computer vision project that transforms physical movements detected via a webcam into interactive controls for gaming and desktop navigation. By leveraging **OpenCV**, **Mediapipe**, and **pydirectinput**, this project offers two main functionalities:
- Hands-free directional controls using body movements.
- Mouse control through hand gestures, complete with drag-and-drop support.

---

## Features
### 1. **Real-Time Movement Detection**
- Tracks body movements using Mediapipe's Pose module.
- Detects directional motion (up, down, left, right) based on keypoint displacement.

### 2. **Dynamic Game Controls**
- Simulates keyboard presses (`W`, `A`, `S`, `D`) corresponding to detected movement direction.
- Supports smooth, real-time control for games or applications requiring directional input.

### 3. **Mouse Control with Hand Gestures**
- Tracks hand movements using Mediapipe's Hand module.
- Converts wrist position into mouse movements with adjustable acceleration.
- Detects hand closure to enable drag-and-drop functionality:
  - **Hand Closed**: Activates drag mode.
  - **Hand Open**: Releases drag mode.

---

## How It Works
### Game Controls:
1. **Input via Webcam**:
   - Captures real-time video feed for body landmark tracking.
2. **Landmark Tracking**:
   - Uses the nose as the primary movement point.
3. **Direction Detection**:
   - Calculates movement direction based on the nose's position changes:
     - **Up (`W`)**: Nose moves upward.
     - **Down (`S`)**: Nose moves downward.
     - **Left (`A`)**: Nose moves left.
     - **Right (`D`)**: Nose moves right.
4. **Simulated Keyboard Input**:
   - Sends the detected direction as a keyboard press using the `pydirectinput` library.

### Hand Mouse Control:
1. **Hand Detection**:
   - Tracks hand landmarks using Mediapipe's Hands solution.
2. **Mouse Movement**:
   - Maps wrist movements to mouse cursor movements, with configurable acceleration:
     - **Acceleration Factor**: Adjusts cursor speed based on hand velocity.
3. **Drag-and-Drop**:
   - Detects hand closure to enable drag-and-drop:
     - **Mouse Down**: Hand closes.
     - **Mouse Up**: Hand opens.

---

## Key Components
- **OpenCV**:
  - Handles video feed capture and real-time visualization.
  
- **Mediapipe**:
  - Provides landmark detection for hands and pose estimation.

- **PyDirectInput**:
  - Simulates mouse movements, clicks, and drag-and-drop functionality.
  - Simulates keyboard inputs for directional control.

---

## Use Cases
- **Gaming**:
  - Hands-free gaming using directional controls.
- **Accessibility**:
  - Use hand gestures to replace traditional mouse functions.
- **Interactive Applications**:
  - Intuitive interaction with desktop environments.

---

## How to Quit
- Press the `q` key to stop the application.

---

## Output Display
1. **Game Controls**:
   - Displays movement details, such as position differences (`dif`), distance (`dis`), and movement direction (`mov`) on the video feed.
2. **Hand Mouse Control**:
   - Visualizes hand landmarks and tracks wrist position on the video feed.

---

## Notes
- The hand mouse control feature is designed for single-hand tracking.
- Adjustable parameters:
  - **Acceleration (`acc`)**: Controls cursor speed for normal movements.
  - **Drag Acceleration (`accd`)**: Adjusts speed during drag-and-drop.
  - **Hand Closure Sensitivity (`close`)**: Defines the threshold for detecting a closed hand.

---

## Contributions
Contributions to improve or extend the functionality of this project are welcome! Feel free to open issues or submit pull requests.

---

## License
This project is open-source and available under the MIT License.
