import cv2

def open_webcam():
    # Open the first available webcam
    cap = cv2.VideoCapture(0)

    # Check if the webcam is opened successfully
    if not cap.isOpened():
        print("Failed to open the webcam.")
        return

    while True:
        # Read a frame from the video stream
        ret, frame = cap.read()

        # Check if a frame was successfully read
        if not ret:
            print("Failed to capture a frame from the webcam.")
            break

        # Display the frame in a window called "Webcam"
        cv2.imshow("Webcam", frame)

        # Wait for the 'q' key to be pressed to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture object and close the window
    cap.release()
    cv2.destroyAllWindows()

# Call the function to open the webcam
open_webcam()