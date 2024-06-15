import cv2
import numpy as np

def sketch(frame):
    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Detect edges using Canny edge detection
    edges = cv2.Canny(blurred, 30, 100)
    
    # Invert the edges to create a sketch effect
    sketch = 255 - edges
    
    return sketch


cap = cv2.VideoCapture(0)
    
while True:
        # Capture frame-by-frame
    ret, frame = cap.read()
        
    if ret:
            # Process frame
        processed_frame = sketch(frame)
            
            # Display the processed frame
    cv2.imshow('Sketch', processed_frame)
        
        # Check for 'q' key press to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    # Release the capture
cap.release()
cv2.destroyAllWindows()