import re
import random
rules = {
    'greetings': [r'hi|hello|hey', ["Hello! How can I assist you today?", "Hi there! How can I help you?"]],
    'goodbye': [r'bye|goodbye', ["Goodbye! Have a great day!", "See you later!"]],
    'thanks': [r'thank you|thanks', ["You're welcome!", "No problem!"]],
    'opening_hours': [r'what are your opening hours|when do you open', ["We are open Monday to Friday from 9am to 6pm.", "Our opening hours are from 9am to 6pm, Monday to Friday."]],
    'location': [r'where are you located|what is your address', ["Our address is 123 Main St, City, Country.", "You can find us at 123 Main St."]],
    'product_info': [r'what products do you offer|what do you sell', ["We offer a variety of products including electronics, clothing, and accessories.", "Our products range from electronics to clothing and accessories."]],
    'delivery_info': [r'how long does delivery take|delivery time', ["Delivery usually takes 3-5 business days, but may vary depending on your location.", "Delivery time is typically 3-5 business days."]],
    'pricing': [r'how much does it cost|what is the price', ["For pricing information, please visit our website or contact our customer service.", "Prices vary depending on the product. You can check our website for specific prices."]],
    'contact_info': [r'how can I contact you|what is your phone number', ["You can contact us at 123-456-7890 or email us at info@example.com.", "Our phone number is 123-456-7890 and you can also reach us via email at info@example.com."]],
    'returns': [r'what is your return policy|can I return a product', ["Our return policy allows returns within 30 days of purchase. Please refer to our website for details.", "Yes, you can return a product within 30 days. Visit our website for our return policy."]],
    'order_status': [r'how can I track my order|where is my order', ["You can track your order status by logging into your account on our website.", "To track your order, enter your order number on our website's tracking page."]],
    'payment_methods': [r'what payment methods do you accept|how can I pay', ["We accept various payment methods including credit cards, PayPal, and bank transfer.", "You can pay for your order using credit card, PayPal, or bank transfer."]],
    'size_guide': [r'what size should I choose|do you have a size guide', ["You can find our size guide on our website to help you choose the right size.", "Check our website for a size guide to ensure the perfect fit."]],
    'customer_reviews': [r'what do customers say about you|do you have customer reviews', ["Our customers love our products! You can read their reviews on our website.", "Check out the customer reviews section on our website to see what people are saying."]],
    'shipping_cost': [r'how much does shipping cost|what is the shipping fee', ["Shipping costs vary depending on your location and the size of your order. Please proceed to checkout for shipping cost details.", "Shipping fees are calculated based on your location and order size. You can view the shipping cost at checkout."]],
}
def extract_intent(user_input):
   
    for intent, (pattern, _) in rules.items():
        if re.search(pattern, user_input, re.IGNORECASE):
            return intent
    return None

def respond_to_query(user_input):
   
    intent = extract_intent(user_input)
    if intent:
       
        responses = rules[intent][1]
        return random.choice(responses)
    else:
        
        return "I'm sorry, I didn't understand. Can you please rephrase your question?"

print("Chatbot: Hello! How can I assist you today?")
while True:
    user_input = input("User: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye! Have a great day!")
        break
    response = respond_to_query(user_input)
    print("Chatbot:", response)
