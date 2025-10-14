import cv2
import os
import time
import argparse
from datetime import datetime
import tkinter as tk
from tkinter import messagebox, simpledialog

class ImageCapture:
    def __init__(self, output_dir="dataset", camera_id=0):
        """
        Initialize the image capture system
        
        Args:
            output_dir (str): Directory to save captured images
            camera_id (int): Camera device ID (usually 0 for default camera)
        """
        self.output_dir = output_dir
        self.camera_id = camera_id
        self.cap = None
        self.counter = 0
        
        # Create output directory if it doesn't exist
        os.makedirs(self.output_dir, exist_ok=True)
        
    def initialize_camera(self):
        """Initialize the camera"""
        self.cap = cv2.VideoCapture(self.camera_id)
        if not self.cap.isOpened():
            raise Exception(f"Could not open camera with ID {self.camera_id}")
        
        # Set camera resolution (optional)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        
        # Allow camera to warm up
        time.sleep(2)
        
    def capture_image(self, label=None):
        """
        Capture a single image from the camera
        
        Args:
            label (str): Optional label for the image
            
        Returns:
            str: Path to the saved image
        """
        if not self.cap:
            self.initialize_camera()
            
        ret, frame = self.cap.read()
        if not ret:
            raise Exception("Failed to capture image")
            
        # Generate filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.counter += 1
        
        if label:
            filename = f"{label}_{timestamp}_{self.counter}.jpg"
        else:
            filename = f"image_{timestamp}_{self.counter}.jpg"
            
        filepath = os.path.join(self.output_dir, filename)
        
        # Save the image
        cv2.imwrite(filepath, frame)
        print(f"Image saved: {filepath}")
        
        return filepath
    
    def capture_batch(self, count=10, interval=1, label=None):
        """
        Capture a batch of images at specified intervals
        
        Args:
            count (int): Number of images to capture
            interval (float): Interval between captures in seconds
            label (str): Optional label for the images
        """
        print(f"Capturing {count} images with {interval}s interval...")
        
        for i in range(count):
            self.capture_image(label)
            if i < count - 1:  # Don't wait after the last capture
                time.sleep(interval)
                
        print("Batch capture complete!")
    
    def preview_and_capture(self):
        """Show camera preview and capture on keypress"""
        if not self.cap:
            self.initialize_camera()
            
        print("Camera preview started. Press SPACE to capture, ESC to exit.")
        
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break
                
            # Display the frame
            cv2.imshow('Camera Preview', frame)
            
            key = cv2.waitKey(1) & 0xFF
            
            if key == 32:  # SPACE key
                self.capture_image()
            elif key == 27:  # ESC key
                break
                
        cv2.destroyAllWindows()
    
    def release_camera(self):
        """Release the camera resources"""
        if self.cap:
            self.cap.release()
            cv2.destroyAllWindows()

def main():
    parser = argparse.ArgumentParser(description='Camera Image Capture Tool')
    parser.add_argument('--output', type=str, default='dataset', help='Output directory for images')
    parser.add_argument('--camera', type=int, default=0, help='Camera ID (default: 0)')
    parser.add_argument('--batch', type=int, help='Number of images to capture in batch mode')
    parser.add_argument('--interval', type=float, default=1.0, help='Interval between captures in seconds (default: 1.0)')
    parser.add_argument('--label', type=str, help='Label for captured images')
    
    args = parser.parse_args()
    
    # Create capture instance
    capture = ImageCapture(output_dir=args.output, camera_id=args.camera)
    
    try:
        if args.batch:
            # Batch capture mode
            capture.capture_batch(count=args.batch, interval=args.interval, label=args.label)
        else:
            # Interactive mode with GUI
            root = tk.Tk()
            root.withdraw()  # Hide the main window
            
            # Ask user for mode
            mode = messagebox.askyesno("Capture Mode", 
                                      "Do you want to capture a batch of images?\n(Yes for batch, No for preview mode)")
            
            if mode:
                # Batch mode
                count = simpledialog.askinteger("Batch Capture", "How many images to capture?", 
                                               minvalue=1, maxvalue=100)
                if count:
                    interval = simpledialog.askfloat("Batch Capture", "Interval between captures (seconds):", 
                                                    minvalue=0.1, maxvalue=10.0, initialvalue=1.0)
                    label = simpledialog.askstring("Batch Capture", "Label for images (optional):")
                    capture.capture_batch(count=count, interval=interval, label=label)
            else:
                # Preview mode
                messagebox.showinfo("Preview Mode", 
                                  "Camera preview will open.\nPress SPACE to capture, ESC to exit.")
                capture.preview_and_capture()
                
    except Exception as e:
        print(f"Error: {e}")
    finally:
        capture.release_camera()

if __name__ == "__main__":
    main()