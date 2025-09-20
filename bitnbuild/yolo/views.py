from django.shortcuts import render, get_object_or_404
from ultralytics import YOLO
import cv2
from inventory.models import Product
from twilio.rest import Client

# Initialize the YOLO model once, outside of the view function
model = YOLO('yolov8n.pt')

def out_of_stock(request):
    if request.method == 'GET':
        banana_product = get_object_or_404(Product, name="Banana")
        
        # Check if bananas are in stock
        if banana_product.quantity_remaining > 0:
            # Decrease the quantity of bananas by 1
            banana_product.quantity_remaining -= 1
            qty = banana_product.quantity_remaining
            # send_report_via_sms(qty)  # Uncomment this to send SMS report

            banana_product.save()
            message = "Banana quantity decreased successfully."
        else:
            message = "No bananas left in stock."
        
        print(message)

        # Open video capture device
        cap = cv2.VideoCapture(0)  # Use appropriate video capture device

        while True:
            # Read frame from video capture device
            ret, frame = cap.read()
            if not ret:
                print("Failed to grab frame.")
                break
            
            # Perform object detection on the frame
            results = model(frame, show=True)

            # Wait for key press
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break  # Break the loop if 'q' key is pressed
        
        # Release video capture device and close all OpenCV windows
        cap.release()
        cv2.destroyAllWindows()
        
        # Render a template to show the result on a webpage
        return render(request, 'out_of_stock.html')

    return render(request, 'out_of_stock.html')


def send_report_via_sms(qty):
    print(qty)  # Print the quantity
    # You can implement Twilio SMS logic here
