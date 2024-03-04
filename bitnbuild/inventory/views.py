from django.shortcuts import render,HttpResponse,redirect
from .models import Category
from .forms import ProductForm

def index(request):
    # send_expiration_via_sms()
    return render(request, 'index.html')

def ulogin(request):
    return render(request, 'pages/sign-in.html')

def dashboard(request):
    return render(request, 'pages/dashboard.html')

def add_inventory(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(display_inventory)
    else:
        form = ProductForm()
    categories = Category.objects.all()
    return render(request, 'inventory/add_inventory.html', {'form': form, 'categories': categories})


# def display_inventory(request):
#     # Retrieve all categories along with their associated products
#     categories = Category.objects.prefetch_related('product_set')

#     # Render the template with the categories and associated products
#     return render(request, 'inventory/inventory.html', {'categories': categories})
def display_inventory(request):
    # Retrieve all categories along with their associated products
    wood_present = Product.objects.filter(name='Wood', quantity_remaining__gt=0).exists()
    metal_present = Product.objects.filter(name='metal', quantity_remaining__gt=0).exists()
    categories = Category.objects.prefetch_related('product_set')

    # Render the template with the categories and associated products
    return render(request, 'inventory/inventory.html',{'categories': categories,'wood_present': wood_present, 'metal_present': metal_present})

import requests

from django.http import JsonResponse
import requests, json

from django.shortcuts import render

def weather_forecast(request):
    
    # Initialize empty dictionary for weather data
    weather_data = {}
    if request.method == 'POST':
        city = request.POST.get('city')
        api_key = '1a5f6c9013c1cf931b5512d06bbdd474'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'  # Query for weather data in Celsius

        try:
            response = requests.get(url)
            response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code.
            data = response.json()
            weather_data = {
                'city': city,
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon'],
            }
        except requests.RequestException:
            weather_data = {'error': 'Error fetching weather data'}

    # Sample data for weather predictions and farming advice
    city = city if 'city' in locals() else 'Your City'
    sample_weather_description = "scattered clouds"
    sample_rainfall = 0.5  # mm for the last hour
    
    # Sample Data for Next 1 Day, Week, Month
    sample_next_1_day = {
        "date": "February 26, 2024",
        "rainfall_prediction": 30,
        "sunlight_percentage": 60,
        "expected_rainfall": 5
    }
    
    sample_next_1_week = {
        "date_range": "February 26, 2024 - March 4, 2024",
        "average_rainfall_prediction": 25,
        "average_sunlight_percentage": 65,
        "expected_weekly_rainfall": 20
    }
    
    sample_next_1_month = {
        "date_range": "February 26, 2024 - March 26, 2024",
        "average_rainfall_prediction": 20,
        "average_sunlight_percentage": 70,
        "expected_monthly_rainfall": 80
    }
    
    # Additional Information for Farmers
    additional_info = {
        "soil_moisture_levels": "Monitoring soil moisture is crucial for optimal crop growth...",
        "crop_planning": "Depending on the rainfall prediction, farmers might opt to plant crops...",
        "pest_management": "Rainfall and humidity can influence pest populations...",
        "water_management": "Efficient water management strategies become essential..."
    }

    # Passing data to the template
    context = {
        "city": city,
        "sample_weather_description": sample_weather_description,
        "sample_rainfall": sample_rainfall,
        "sample_next_1_day": sample_next_1_day,
        "sample_next_1_week": sample_next_1_week,
        "sample_next_1_month": sample_next_1_month,
        "additional_info": additional_info,
        'weather_data': weather_data,
    }
    
    return render(request, 'weather_forecast.html', context)
# def get_weather_data(request):
#     api_key = '1a5f6c9013c1cf931b5q512d06bbdd474'  # Replace with your actual API key
#     city_name = 'Mumbai'  # Retrieve city name from GET parameters
    
#     if city_name:
#         base_url = "http://api.openweathermap.org/data/2.5/weather?"
#         complete_url = base_url + "appid=" + api_key + "&q=" + city_name

#         response = requests.get(complete_url)
#         data = response.json()

#         if data.get("cod") != "404":
#             main_data = data.get("main", {})
#             current_temperature = main_data.get("temp")
#             current_pressure = main_data.get("pressure")
#             current_humidity = main_data.get("humidity")
#             weather_description = data.get("weather", [{}])[0].get("description")
#             rainfall = data.get("rain", {}).get("1h", 0)  # Get rainfall in last hour, default to 0 if not available


#             sample_weather_description = "scattered clouds"

#             sample_rainfall = 0.5  # in mm for the last hour

#             # Sample Data for Next 1 Day
#             sample_next_1_day = {
#                 "date": "February 26, 2024",
#                 "rainfall_prediction": 30,  # in percentage
#                 "sunlight_percentage": 60,  # in percentage
#                 "expected_rainfall": 5  # in mm
#             }

#             # Sample Data for Next 1 Week
#             sample_next_1_week = {
#                 "date_range": "February 26, 2024 - March 4, 2024",
#                 "average_rainfall_prediction": 25,  # in percentage
#                 "average_sunlight_percentage": 65,  # in percentage
#                 "expected_weekly_rainfall": 20  # in mm
#             }

#             # Sample Data for Next 1 Month
#             sample_next_1_month = {
#                 "date_range": "February 26, 2024 - March 26, 2024",
#                 "average_rainfall_prediction": 20,  # in percentage
#                 "average_sunlight_percentage": 70,  # in percentage
#                 "expected_monthly_rainfall": 80  # in mm
#             }

#             # Additional Information for Farmers
#             additional_info = {
#                 "soil_moisture_levels": "Monitoring soil moisture is crucial for optimal crop growth. After a rainfall event, it's advisable to check the soil moisture to decide whether additional irrigation is needed.",
#                 "crop_planning": "Depending on the rainfall prediction, farmers might opt to plant crops that are more drought-resistant if a lower-than-average rainfall is expected, or choose crops that can thrive in wetter conditions if a higher-than-average rainfall is anticipated.",
#                 "pest_management": "Rainfall and humidity can influence pest populations. More rainfall can lead to higher humidity levels, which might increase the likelihood of certain pests and diseases. Farmers should be prepared to implement pest management strategies accordingly.",
#                 "water_management": "Efficient water management strategies become essential, especially in areas with variable rainfall predictions. Collecting rainwater, using drip irrigation systems, and planning the irrigation schedule based on weather forecasts can help in utilizing water resources more effectively."
#             }

#             return JsonResponse({
#                 "temperature": current_temperature,
#                 "pressure": current_pressure,
#                 "humidity": current_humidity,
#                 "description": weather_description,
#                 "rainfall": rainfall
#             })
#         else:
#             return JsonResponse({"error": "City not found"}, status=404)
#     else:
#         return JsonResponse({"error": "City parameter missing"}, status=400)

# tool crafting
from django.utils import timezone
from .models import Product,Category
def make_pickaxe_page(request):
    return render(request, 'inventory/make_pickaxe.html')

def make_pickaxe(request):
    if request.method == 'POST':
        wood_quantity = int(request.POST.get('wood_quantity', 0))
        metal_quantity = int(request.POST.get('metal_quantity', 0))

        # Get wood and metal resources
        wood_product = Product.objects.get(name='Wood')
        metal_product = Product.objects.get(name='metal')

        # Check if enough resources are available
        if wood_product.quantity_remaining >= wood_quantity and metal_product.quantity_remaining >= metal_quantity:
            # Deduct wood and metal from inventory
            wood_product.quantity_remaining -= wood_quantity
            metal_product.quantity_remaining -= metal_quantity

            # Save the changes
            wood_product.save()
            metal_product.save()

            # Retrieve the 'tools' category
            tools_category = Category.objects.get(name='Tools')

            # Create the pickaxe and add it to the inventory
            pickaxe = Product.objects.create(
                name='pickaxe',
                image='static/assets/img/pickaxe.jpg',
                price=300.00,  # Set the price according to your requirement
                quantity_total=1,
                quantity_remaining=1,  # Assuming one pickaxe is created per action
                date_bought=timezone.now(),  # You can set the date if needed
                date_expiration=timezone.now(),  # You can set the expiration date if needed
                category=tools_category,  # Set the category if needed
                # Set other fields as required
            )

            return redirect('display_inventory')
        else:
            # Handle insufficient resources error
            error_message = "Insufficient resources to make pickaxe."
            return render(request, 'error.html', {'error_message': error_message})

    # Handle GET requests or invalid form submissions
    return redirect('display_inventory')

from twilio.rest import Client



    
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from .models import Product

def generate_pdf(request):
    # Get all products from the database
    products = Product.objects.all()

    # Create a response object with PDF mime type
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="products_report.pdf"'

    # Create a PDF document
    doc = SimpleDocTemplate(response, pagesize=letter)
    elements = []

    # Product details as a list of lists
    product_data = [
        ["Product Name", "Price", "Quantity Total", "Date Bought", "Date Expiration", "Category", "Quantity Remaining"]
    ]

    for product in products:
        product_data.append([
            product.name,
            f"${product.price}",
            str(product.quantity_total),
            str(product.date_bought),
            str(product.date_expiration),
            product.category.name,
            str(product.quantity_remaining),
        ])

    # Create a table and add styles
    table = Table(product_data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    # Add the table to the document
    elements.append(table)
    doc.build(elements)

    return response

from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
import urllib.parse

load_dotenv()
genai.configure(api_key=(os.getenv("GOOGLE_API_KEY")))


def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    print(text)
    return text

def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    chunks = text_splitter.split_text(text)
    return chunks

def get_vector_store(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    index_path = os.path.join(settings.BASE_DIR, "faiss_index")
    vector_store.save_local(index_path)
    return index_path

def get_conversational_chain():
    prompt_template = """
    You are analyzing the data in the inventory given and answering all user questions. The context contains a table with the following
    product names, image, price, quantity_total, date_bought,date_expiration,category,quantity_remaining, Answer on the basis of this.

{context} (Provide the PDF containing the data for analysis)

Question:
{question}

Answer:
    """

    model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)

    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)

    return chain

def user_input(user_question):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    new_db = FAISS.load_local(os.path.join(settings.BASE_DIR, "faiss_index"), embeddings)
    docs = new_db.similarity_search(user_question)
    chain = get_conversational_chain()
    response = chain({"input_documents": docs, "question": user_question}, return_only_outputs=True)
    response_text = response["output_text"]
    if response_text == "":
        response_text = "It seems that the answer is out of context. Here is a general response: ..."
    return response_text

def gemini(request):
    if request.method == 'POST':
        # Handle PDF upload
        pdf_docs = request.FILES.getlist('pdf_files')
        raw_text = get_pdf_text(pdf_docs)
        text_chunks = get_text_chunks(raw_text)
        pdf_path = get_vector_store(text_chunks)  # Save the PDF path

        # Store the PDF path in the user's session
        request.session['pdf_path'] = pdf_path

        # Handle user question
        user_question = request.POST.get('user_question')
        response_text = user_input(user_question)


        # Return response
        return render(request, 'pages/gemini.html', {'response_text': response_text})
    else:
        return render(request, 'pages/gemini.html')