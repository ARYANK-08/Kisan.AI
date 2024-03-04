from django.shortcuts import render, HttpResponse
from ultralytics import YOLO
import cv2
from inventory.models import Product
from django.shortcuts import get_object_or_404, render


def out_of_stock(request):
    if request.method == 'GET':
        # Initialize YOLO model
        model = YOLO('yolov8n.pt')
        banana_product = get_object_or_404(Product, name="Banana")
        # Check if bananas are in stock
        if banana_product.quantity_remaining > 0:
            # Decrease the quantity of bananas by 1
            banana_product.quantity_remaining -= 1
            qty = banana_product.quantity_remaining
            # send_report_via_sms(qty)

            banana_product.save()
            message = "Banana quantity decreased successfully."
        else:
            message = "No bananas left in stock."
        print(message)
        # Open video capture device
        cap = cv2.VideoCapture(0)  # Use appropriqqate videoqqq capture device

        while True:
            # Read frame from video capture device
            ret, frame = cap.read()
            
            # Perform object detection on the frame
            results = model(frame, show=True)

            # Wait for key press
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break  # Break the loop if 'q' key is pressed
            
        # Release video capture device and close all OpenCV windows
        cap.release()
        cv2.destroyAllWindows()
                # Retrieve the product by its name "Banana"
    

        # You can render a template here if yoqu want to show the result on a webpage
        # Or simply return an HttpResponseq


        return render(request, 'out_of_stock.html')

    else:
        return render(request, 'out_of_stock.html')



from twilio.rest import Client




def send_report_via_sms(qty):
    print(hi)