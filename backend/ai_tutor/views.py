import google.generativeai as genai
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from decouple import config

class AITutorView(APIView):
    def post(self, request):
        user_message = request.data.get("message")
        if not user_message:
            return Response({"error": "Message is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        api_key = config('GEMINI_API_KEY', default='')
        
        # System prompt to give the AI a persona
        system_prompt = (
            "You are a helpful and expert AI Tutor for an online IT learning platform. "
            "You help students understand programming concepts, debug code, and guide them in their tech courses. "
            "Keep your explanations clear, concise, and friendly. Answer in the same language the student asks in."
        )

        if not api_key:
            return Response({
                "reply": f"[Mock AI] Hello! You said: '{user_message}'.\n\n(Please set GEMINI_API_KEY in backend/.env to enable real AI responses.)"
            })
            
        try:
            genai.configure(api_key=api_key)
            # Use gemini-1.5-flash for general fast text completion
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            # Combine system prompt with user message for stateless turn
            prompt = f"{system_prompt}\n\nStudent: {user_message}\nAI Tutor:"
            
            response = model.generate_content(prompt)
            return Response({"reply": response.text})
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
