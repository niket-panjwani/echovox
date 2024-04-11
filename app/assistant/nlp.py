from transformers import pipeline

class MeetingSchedulerClassifier:
    def __init__(self):
        # Load a pre-trained pipeline for text classification
        self.classifier = pipeline("text-classification", model="bert-base-uncased")

    def predict(self, text: str) -> bool:
        """
        Predicts whether the given text is about scheduling a meeting by combining
        keyword matching and pre-trained model classification.
        
        :param text: The input text to classify.
        :return: True if the text is about scheduling a meeting, False otherwise.
        """
        # First, check if the text contains specific keywords.
        if self.contains_meeting_keywords(text.lower()):
            return True
        
        # Use the pre-trained model for classification
        result = self.classifier(text)
        # Interpret the model's result
        # For demonstration, we assume any positive sentiment is about scheduling (which is a simplification)
        # You might want to adjust this logic based on your classification labels
        if result[0]['label'] == 'LABEL_1' and result[0]['score'] > 0.5:
            return True
        
        return False
    
    @staticmethod
    def contains_meeting_keywords(text: str) -> bool:
        """
        Checks if the text contains keywords commonly associated with scheduling a meeting.
        
        :param text: The text to check.
        :return: True if keywords are found, False otherwise.
        """
        keywords = ['schedule a meeting', 'set up a meeting', 'organize a meeting', 'meeting with', 'meeting at']
        return any(keyword in text for keyword in keywords)
