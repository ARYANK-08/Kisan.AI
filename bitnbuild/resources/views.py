from django.shortcuts import render
import google.generativeai as genai
import re
r = dict()
def chat_with_ai(request):
    global r
    if request.method == 'POST':
        cropType = request.POST.get('cropType')
        landArea = request.POST.get('landArea')
        season = request.POST.get('season')
        soilquality = request.POST.get('soilquality')


        response = get_ai_response(cropType,landArea,season,soilquality)
        
        # Read out the response using pyttsx3
        extracted_resources = extract_resources(response)
        r = extracted_resources
        print(r)
        return render(request, 'resources/ai.html', {'cropType': cropType,'landArea': landArea,'season': season, 'response': response})
    return render(request, 'resources/ai.html', {})

# def read_aloud(text, language='en'):
#     print('hi')
#     engine = pyttsx3.init()
#     engine.setProperty('rate', 150)  # Speed of speech, adjust as needed
#     engine.setProperty('volume', 0.9)  # Volume level, adjust as needed
#     engine.setProperty('voice', f'{language}_mbrola')  # Use the appropriate voice for the language
#     engine.say(text)
#     engine.runAndWait()


def get_ai_response(cropType,landArea,season,soilquality):
    genai.configure(api_key="AIzaSyA4uR6gq5njTMtQXJwSpIdq_zC1LA1ugS0")  # Set up your API key
    generation_config = {  # Your generation config
        "temperature": 0.1,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 2048,
    }
    safety_settings = [  # Your safety settings
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        # Add other settings as needed
    ]
    model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                  generation_config=generation_config,
                                  safety_settings=safety_settings)
    convo = model.start_chat(history=[])
    context = "Act as a farmer helper who is using his resourse and planting crops .You are taking input as crop type, land area he is using in sq. metres,the soil quality and the season he is planting the crop in summer spring autumn winter and the output given is what all resourses are needed to plant this in what quantity For example a rice crop in some amount of area then output should be what all is needed and in what quantity (kgs) how many kgs of rice crops will i needd to plant in this much area . Output should be the name and the quantity. Also provide tools needed for the farmer"
    message = f"{context} Croptype : {cropType}, LandArea : {landArea}, Soil Quality : {soilquality},season : {season}, "
    response = convo.send_message(message)
    answer = convo.last.text
    # print(f'hi{answer}')
    return convo.last.text # Assuming 'message' contains the response text

def extract_resources(response_text):
    pattern = r"(?P<resource>\w+:\s+)(?P<quantity>\d+\s+\w+)"
    matches = re.findall(pattern, response_text)

    # Create a dictionary from the matches
    resources_dict = {match[0].strip(): match[1].strip() for match in matches}

    print(f'Hello {resources_dict}')
    return resources_dict

# Call the function with the response

# Output the extracted resources
def order(request):
    global r
    print(f'shar{r}')
    return render(request,'resources/order.html',{"resources": r})





