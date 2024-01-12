import customtkinter as ctk
from tkinter import ttk
from textCleaning import *
import joblib
from collections import Counter

#Loading our custom models
classifierSA = joblib.load("Models/SA/classifier.pkl")
vectorizerSA = joblib.load("Models/SA/verctorizer.pkl")
classifierLD = joblib.load("Models/LD/classifier.pkl")
vectorizerLD = joblib.load("Models/LD/verctorizer.pkl")

#Declaring an array that contains the available languages to detect
languages = ['Arabic', 'Bulgarian', 'German', 'Modern Greek', 'English', 'Spanish', 'French', 'Hindi', 'Italian', 'Japanese', 'Dutch', 'Polish', 'Portuguese', 'Russian', 'Swahili', 'Thai', 'Turkish', 'Urdu', 'Vietnamese', 'Chinese']

class Main_Application:
    def __init__(self, master):
        #Initializing the main application window
        self.master = master
        self.master.title("Text Classification Project")
        self.master.geometry("800x410")
        self.master.resizable(width=False, height=False)

        #Creation of the GUI main window's elements
        self.big_title = ctk.CTkLabel(self.master, text="Text Classifiction Applications", font=('Calibri', 22, 'bold'))
        self.big_title.pack(pady=30)

        self.seperator1 = ttk.Separator(self.master, orient='horizontal')
        self.seperator1.pack(fill="x", padx=10)

        self.text = ctk.CTkLabel(self.master, text="Please feel free to choose an application", font=('Calibri', 18))
        self.text.pack(side='top', anchor='nw', padx=20, pady=8)

        self.btn1 = ctk.CTkButton(self.master, width=200, height=50, corner_radius=9, text="Sentiment Analyser", font=('Calibri', 16, 'bold'), command=self.btn1_page)
        self.btn1.pack(pady=(10, 20))
        self.btn2 = ctk.CTkButton(self.master, width=200, height=50, corner_radius=9, text="Language Detecter", font=('Calibri', 16, 'bold'), command=self.btn2_page)
        self.btn2.pack(pady=(10, 20))

        self.seperator2 = ttk.Separator(self.master, orient='horizontal')
        self.seperator2.pack(fill="x", padx=10)

        self.appearance_mode_label = ctk.CTkLabel(self.master, text="Appearance Mode:", font=('Calibri', 16))
        self.appearance_mode_label.pack(side='top', anchor='nw', padx=20, pady=(8,5))
        self.appearance_mode_optionemenu = ctk.CTkOptionMenu(self.master, values=["System", "Light", "Dark"],command=ctk.set_appearance_mode)
        self.appearance_mode_optionemenu.pack(side='top', anchor='nw', padx=45)

        self.about_btn = ctk.CTkButton(self.master, width=90, height=20, text="About", command=self.about_window)
        self.about_btn.pack(side='top', anchor='ne', padx=20, pady=(8,5))
    
    def about_window(self):
        #Creation of a new window to display some informations about the program and its developer
        newWindow = ctk.CTkToplevel(self.master)
        newWindow.title("About this project")
        newWindow.geometry("700x610")
        newWindow.resizable(width=False, height=False)
        ctk.CTkLabel(newWindow, text="About", font=('Calibri', 22, 'bold')).pack(pady=20)
        ttk.Separator(newWindow, orient='horizontal').pack(fill="x", padx=10)
        ctk.CTkLabel(newWindow, text="EN", font=('Calibri', 18, 'bold')).pack(side='top', anchor='nw', padx=20, pady=8)
        text = ctk.CTkTextbox(newWindow, width=800, height=195, corner_radius=9, font=('Calibri', 16), activate_scrollbars=False)
        text.insert(ctk.END, text="This application showcases two supervised text classification tools: Sentiment Analyzer and Language Detector.\n\nThe Sentiment Analyzer is designed to analyze text and determine whether it expresses a positive or negative sentiment. Additionally, it offers the option to display the step-by-step process of its sentiment analysis mechanism, providing transparency in the results.\n\nThe Language Detector, on the other hand, is used to identify the language of a given text. Furthermore, it includes the functionality to present the available languages supported by the model.")
        text.pack()
        ctk.CTkLabel(newWindow, text="FR", font=('Calibri', 18, 'bold')).pack(side='top', anchor='nw', padx=20, pady=8)
        text2 = ctk.CTkTextbox(newWindow, width=800, height=195, corner_radius=9, font=('Calibri', 16), activate_scrollbars=False)
        text2.insert(ctk.END, text="Cette application présente deux outils de classification de texte supervisés : l'analyseur de sentiments et le détecteur de langue.\n\nL'analyseur de sentiments est conçu pour analyser le texte et déterminer s'il exprime un sentiment positif ou négatif. De plus, il offre la possibilité d'afficher le processus étape par étape de son mécanisme d'analyse des sentiments, assurant la transparence des résultats.\n\nLe détecteur de langue, quant à lui, est utilisé pour identifier la langue d'un texte donné. De plus, il inclut la fonctionnalité de présentation des langues disponibles prises en charge par le modèle.")
        text2.pack()
        ttk.Separator(newWindow, orient='horizontal').pack(fill="x", padx=10, pady=10)
        ctk.CTkLabel(newWindow, text="©Copyright 2022-2023 | AMEZIANE Mohamed").pack(side="top", anchor="nw", padx=20)
        newWindow.attributes("-topmost", True)

    def btn1_page(self):
        #Emptying the GUI from the old elements and creating new elements for the sentiment analyser
        self.big_title.pack_forget()
        self.seperator1.pack_forget()
        self.seperator2.pack_forget()
        self.text.pack_forget()
        self.btn1.pack_forget()
        self.btn2.pack_forget()
        self.appearance_mode_label.pack_forget()
        self.appearance_mode_optionemenu.pack_forget()
        self.about_btn.pack_forget()

        self.big_title_btn1 = ctk.CTkLabel(self.master, text="Sentiment Analyser", font=('Calibri', 22, 'bold'))
        self.big_title_btn1.pack(pady=30)

        self.seperator1_btn1 = ttk.Separator(self.master, orient='horizontal')
        self.seperator1_btn1.pack(fill="x", padx=10)

        self.text_btn1 = ctk.CTkLabel(self.master, text="Please type in your Review here", font=('Calibri', 16))
        self.text_btn1.pack(side='top', anchor='nw', padx=20, pady=8)

        self.entry_review_btn1 = ctk.CTkEntry(self.master, placeholder_text="Your review ?", width=290, height=40, corner_radius=9)
        self.entry_review_btn1.pack(pady=10)

        self.btn_predict_btn1 = ctk.CTkButton(self.master, text="Predict", width=190, height=40, command=self.predict_review)
        self.btn_predict_btn1.pack(pady=5)

        self.polarity_predict_btn1 = ctk.CTkLabel(self.master, text="Polarity Prediction : ____", font=('Calibri', 18, 'bold'))
        self.polarity_predict_btn1.pack(side='top', anchor='nw', padx=65, pady=8)

        self.steps_checkbox_var_btn1 = ctk.IntVar()
        self.steps_checkbox_btn1 = ctk.CTkCheckBox(self.master, corner_radius=9, text="Show text's preprocessing steps", font=('Calibri', 16), variable=self.steps_checkbox_var_btn1, command=self.show_steps_area_btn1)
        self.steps_checkbox_btn1.pack(side='top', anchor='nw', padx=20, pady=8)
        self.steps_textarea_btn1 = ctk.CTkTextbox(self.master, height=350, width=800, activate_scrollbars=False, font=('Calibri', 16, 'bold'))
        self.steps_textarea_btn1.pack_forget()

        self.seperator2_btn1 = ttk.Separator(self.master, orient='horizontal')
        self.seperator2_btn1.pack(fill="x", padx=10, pady=10)
        
        self.back_button_btn1 = ctk.CTkButton(self.master, text="Back", command=self.main_page)
        self.back_button_btn1.pack(side='bottom', anchor='nw', padx=10, pady=20)

    def predict_review(self):
        #Function that will predict the input text weither it's positive or negative.
        text = self.entry_review_btn1.get()
        if text=='':
            #if the input is empty
            polarity_prediction = f"Text is empty !"
        else:
            new_text = textCleaner(text)
            text_vector = vectorizerSA.transform([new_text])
            prediction = classifierSA.predict(text_vector)
            prediction = "Positive !" if prediction[0] == 1 else "Negative !"
            polarity_prediction = f"Polarity Prediction: {prediction}"
        #displaying the sentiment result
        self.polarity_predict_btn1.configure(text=polarity_prediction)

    def show_steps_area_btn1(self):
        #if the checkbox is checked, the window size will increase and a textbox will appear
        if self.steps_checkbox_var_btn1.get() == 1 and self.entry_review_btn1.get() != '':
            self.master.geometry("800x710")
            self.steps_result()
            self.steps_textarea_btn1.pack(padx=10)
        else:
            #whenever the checkboc is unchecked, the textarea's value will be deleted and the size of the window will be back to normal
            self.steps_textarea_btn1.delete('1.0', ctk.END)
            self.steps_textarea_btn1.pack_forget()
            self.master.geometry("800x410")

    def steps_result(self):
        #Function that write down the result of eachstep of preprocessing the text in the textarea.
        text = self.entry_review_btn1.get()
        self.steps_textarea_btn1.insert(ctk.END, "Typed text : "+text+"\n\n")
        normalised = textNormaliser(text)
        self.steps_textarea_btn1.insert(ctk.END, "Normalised : "+normalised+"\n\n")
        tokens = str(textTokenizer(normalised))
        self.steps_textarea_btn1.insert(ctk.END, "Tokens : "+tokens+"\n\n")
        tokens_without_stopwords = str(stopwords_remover(textTokenizer(normalised)))
        self.steps_textarea_btn1.insert(ctk.END, "Tokens without stopwords : "+tokens_without_stopwords+"\n\n")
        stemmed = str(textStemmer(stopwords_remover(textTokenizer(normalised))))
        self.steps_textarea_btn1.insert(ctk.END, "Stemmed : "+stemmed+"\n\n")
        self.steps_textarea_btn1.insert(ctk.END, "Cleaned text : "+textCleaner(text))
    
    def btn2_page(self):
        #Emptying the GUI from the old elements and creating new elements for the language detector
        self.big_title.pack_forget()
        self.seperator1.pack_forget()
        self.seperator2.pack_forget()
        self.text.pack_forget()
        self.btn1.pack_forget()
        self.btn2.pack_forget()
        self.appearance_mode_label.pack_forget()
        self.appearance_mode_optionemenu.pack_forget()
        self.about_btn.pack_forget()

        self.master.geometry("460x500")

        self.big_title_btn2 = ctk.CTkLabel(self.master, text="Language Detecter", font=('Calibri', 22, 'bold'))
        self.big_title_btn2.pack(pady=30)

        self.seperator1_btn2 = ttk.Separator(self.master, orient='horizontal')
        self.seperator1_btn2.pack(fill="x", padx=10)

        self.text_btn2 = ctk.CTkLabel(self.master, text="Please type in your Text here", font=('Calibri', 16))
        self.text_btn2.pack(side='top', anchor='nw', padx=20, pady=10)

        self.entry_text_btn2 = ctk.CTkTextbox(self.master, width=400, height=80, border_width=2)
        self.entry_text_btn2.pack(side='top', anchor='nw', padx=40)

        self.detection_button_btn2 = ctk.CTkButton(self.master, text="Detect", height=40, font=('Calibri', 16, 'bold'), command=self.detect_lang)
        self.detection_button_btn2.pack(side='top', anchor='n', pady=15)

        self.detected_language_btn2 = ctk.CTkLabel(self.master, text="Your text's language : ____", font=('Calibri', 18, 'bold'))
        self.detected_language_btn2.pack(side='top', anchor='nw', padx=35, pady=15)

        self.langs_checkbox_var_btn2 = ctk.IntVar()
        self.langs_checkbox_btn2 = ctk.CTkCheckBox(self.master, corner_radius=9, text="Show available languages", font=('Calibri', 16), variable=self.langs_checkbox_var_btn2, command=self.show_langs)
        self.langs_checkbox_btn2.pack(side='top', anchor='nw', padx=20, pady=8)
        self.langs_textarea_btn2 = ctk.CTkTextbox(self.master, height=150, width=400, activate_scrollbars=False, font=('Calibri', 16, 'bold'))
        self.langs_textarea_btn2.pack_forget()

        self.seperator2_btn2 = ttk.Separator(self.master, orient='horizontal')
        self.seperator2_btn2.pack(fill="x", padx=10, pady=(20,10))

        self.back_button_btn2 = ctk.CTkButton(self.master, text="Back", command=self.main_page)
        self.back_button_btn2.pack(side='bottom', anchor="nw", padx=10, pady=20)

    def detect_lang(self):
        #Function that'll show what's the text input's language.
        text = self.entry_text_btn2.get("1.0", ctk.END)
        text = textCleanerMulti(text)
        text = vectorizerLD.transform(text.split())
        pred = classifierLD.predict(text)
        counter = Counter(pred)
        language_detected = counter.most_common(1)[0][0]
        #Displaying the language.
        self.detected_language_btn2.configure(text=f"Your text's language : {languages[language_detected-1]}")

    def show_langs(self):
        #if the checkbox is checked, the window size will increase and a textbox will appear
        if self.langs_checkbox_var_btn2.get() == 1 :
            self.master.geometry("460x600")
            self.langs_textarea_btn2.insert(ctk.END, str(languages))
            self.langs_textarea_btn2.pack(padx=10)
        else:
            #whenever the checkboc is unchecked, the textarea's value will be deleted and the size of the window will be back to normal
            self.langs_textarea_btn2.delete('1.0', ctk.END)
            self.langs_textarea_btn2.pack_forget()
            self.master.geometry("460x500")


    def main_page(self):
        #hide the old elements weither we're on sentiment analyzer or language detecter and repack the main application's elements.
        try:
            self.big_title_btn1.pack_forget()
            self.seperator1_btn1.pack_forget()
            self.seperator2_btn1.pack_forget()
            self.text_btn1.pack_forget()
            self.entry_review_btn1.pack_forget()
            self.btn_predict_btn1.pack_forget()
            if (self.steps_checkbox_var_btn1.get() == 1):
                self.steps_textarea_btn1.pack_forget()
            self.master.geometry("800x410")
            self.steps_checkbox_btn1.pack_forget()
            self.polarity_predict_btn1.pack_forget()
            self.back_button_btn1.pack_forget()
        except AttributeError:
            pass
        try:
            self.big_title_btn2.pack_forget()
            self.seperator1_btn2.pack_forget()
            self.seperator2_btn2.pack_forget()
            self.text_btn2.pack_forget()
            self.entry_text_btn2.pack_forget()
            self.detection_button_btn2.pack_forget()
            self.detected_language_btn2.pack_forget()
            if (self.langs_checkbox_var_btn2.get() == 1):
                self.langs_textarea_btn2.pack_forget()
            self.langs_checkbox_btn2.pack_forget()
            self.back_button_btn2.pack_forget()
            self.master.geometry("800x410")
        except AttributeError:
            pass
        
        self.big_title.pack(pady=30)
        self.seperator1.pack(fill="x", padx=10)
        self.text.pack(side='top', anchor='nw', padx=20, pady=8)
        self.btn1.pack(pady=(10, 20))
        self.btn2.pack(pady=(10, 20))
        self.seperator2.pack(fill="x", padx=10)
        self.appearance_mode_label.pack(side='top', anchor='nw', padx=20, pady=(8,5))
        self.appearance_mode_optionemenu.pack(side='top', anchor='nw', padx=45)
        self.about_btn.pack(side='top', anchor='ne', padx=20, pady=(8,5))

#Creation of an app's instance and running it.
root = ctk.CTk()
app = Main_Application(root)
root.mainloop()