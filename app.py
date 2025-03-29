import gradio as gr

def dummy_function(*args):
    # This function would handle the actual HR assistant functionality
    return "This is where the HR assistant response would appear."

def show_settings_page():
    return gr.update(visible=True), gr.update(visible=False)

def show_main_page():
    return gr.update(visible=False), gr.update(visible=True)

# Color scheme variables
dark_bg = "#1A1D25"
darker_bg = "#151821"
button_blue = "#4C82FB"
purple_accent = "#9D5CF7"
card_bg = "#22252F"
text_color = "#FFFFFF"
muted_text = "#A0A0A0"
icon_blue = "#4C82FB"

with gr.Blocks(theme=gr.themes.Base(), 
               css=f"""
               #container {{background-color: {dark_bg};}}
               .gradio-container {{background-color: {dark_bg} !important;}}
               .main-panel {{background-color: {dark_bg};}}
               .left-panel {{background-color: {darker_bg}; border-radius: 10px; padding: 10px; margin: 15px;}}
               .example-questions {{background-color: {card_bg}; border-radius: 10px; padding: 15px; margin-bottom: 20px;}}
               .capabilities {{background-color: {card_bg}; border-radius: 10px; padding: 15px;}}
               .full-width-header {{background-color: {darker_bg}; padding: 15px; width: 100%; display: flex; justify-content: space-between; align-items: center;}}
               .header {{color: {text_color}; display: flex; align-items: center; font-size: 24px; font-weight: bold;}}
               .chat-icon {{color: {button_blue}; margin-right: 10px;}}
               .section-title {{color: {text_color}; font-size: 20px; margin-bottom: 15px;}}
               .history-item {{padding: 8px 0; color: {text_color};}}
               .question-button {{background-color: {card_bg}; color: {text_color}; text-align: left; padding: 12px; 
                                 border-radius: 8px; margin-bottom: 10px; border: none;}}
               .capability-card {{background-color: {darker_bg}; border-radius: 8px; padding: 15px; margin-bottom: 10px;}}
               .capability-title {{color: {text_color}; font-size: 16px; font-weight: 600;}}
               .capability-subtitle {{color: {muted_text}; font-size: 14px;}}
               .footer-bar {{background-color: {darker_bg}; padding: 10px; border-radius: 8px;}}
               .send-button {{background-color: {button_blue}; color: white; border-radius: 8px;}}
               .settings-button {{background-color: {button_blue}; color: white; border-radius: 8px; padding: 6px 12px; width: 100px;}}
               .back-button {{background-color: {button_blue}; color: white; border-radius: 8px; padding: 6px 12px; margin-bottom: 20px;}}
               .settings-panel {{background-color: {card_bg}; border-radius: 10px; padding: 20px; margin: 15px;}}
               .settings-container {{background-color: {dark_bg}; padding: 20px;}}
               """) as demo:
    
    # Create two pages: main app and settings
    main_app = gr.Group(visible=True)
    settings_page = gr.Group(visible=False)
    
    # Main application
    with main_app:
        # Full-width header with added settings button
        with gr.Row(elem_classes=["full-width-header"]):
            gr.HTML(f"""<div class="header"><span class="chat-icon">💬</span> GuideWell HR Assistant</div>""")
            settings_btn = gr.Button("Settings", elem_classes=["settings-button"])
        
        with gr.Row(elem_id="container"):
            # Left panel - Chat History
            with gr.Column(scale=1, elem_classes=["left-panel"]):
                with gr.Row():
                    gr.HTML(f"""<div class="section-title">Chat History</div>""")
                
                with gr.Column():
                    gr.HTML("""<div class="history-item">Previous question 1</div>""")
                    gr.HTML("""<div class="history-item">Previous question 2</div>""")
            
            # Right panel - Main content
            with gr.Column(scale=3, elem_classes=["main-panel"]):
                
                # Example Questions Section
                with gr.Group(elem_classes=["example-questions"]):
                    gr.HTML("""<div class="section-title">📌 Example Questions</div>""")
                    
                    with gr.Row():
                        with gr.Column(scale=1):
                            gr.Button("What is the policy for requesting paid time off?", elem_classes=["question-button"])
                            gr.Button("How do I update my direct deposit information?", elem_classes=["question-button"])
                        
                        with gr.Column(scale=1):
                            gr.Button("Could you explain the jury duty and court appearances policy?", elem_classes=["question-button"])
                            gr.Button("What are the steps for performance review submissions?", elem_classes=["question-button"])
                
                # Capabilities Section
                with gr.Group(elem_classes=["capabilities"]):
                    gr.HTML("""<div class="section-title">Capabilities</div>""")
                    
                    with gr.Row():
                        with gr.Column(scale=1):
                            with gr.Group(elem_classes=["capability-card"]):
                                gr.HTML("""
                                <div>
                                    <div class="capability-title">👥 Employee Self-Service</div>
                                    <div class="capability-subtitle">Manage your HR tasks efficiently</div>
                                </div>
                                """)
                            
                            with gr.Group(elem_classes=["capability-card"]):
                                gr.HTML("""
                                <div>
                                    <div class="capability-title">🛡️ Security & Compliance</div>
                                    <div class="capability-subtitle">Stay informed about compliance requirements</div>
                                </div>
                                """)
                        
                        with gr.Column(scale=1):
                            with gr.Group(elem_classes=["capability-card"]):
                                gr.HTML("""
                                <div>
                                    <div class="capability-title">📋 HR Policy & Procedure</div>
                                    <div class="capability-subtitle">Get instant answers about company policies</div>
                                </div>
                                """)
                            
                            with gr.Group(elem_classes=["capability-card"]):
                                gr.HTML("""
                                <div>
                                    <div class="capability-title">💲 Benefits & Compensation</div>
                                    <div class="capability-subtitle">Learn about your benefits package</div>
                                </div>
                                """)
                
                # Input and Chat Area
                with gr.Row(elem_classes=["footer-bar"]):
                    with gr.Column(scale=20):
                        user_input = gr.Textbox(
                            placeholder="Ask me anything about HR policies...",
                            show_label=False,
                        )
                    
                    with gr.Column(scale=1):
                        submit_btn = gr.Button("Send", elem_classes=["send-button"])
                
                output = gr.Textbox(label="Response", visible=False)
                
                # Connect the components
                submit_btn.click(dummy_function, inputs=[user_input], outputs=[output])
                user_input.submit(dummy_function, inputs=[user_input], outputs=[output])
    
    # Settings page
    with settings_page:
        with gr.Row(elem_classes=["full-width-header"]):
            back_btn = gr.Button("← Back", elem_classes=["back-button"])
            gr.HTML(f"""<div class="header">Settings</div>""")
        
        with gr.Column(elem_classes=["settings-container"]):
            with gr.Group(elem_classes=["settings-panel"]):
                gr.HTML("""<div class="section-title">Settings</div>""")
                gr.HTML("""<div>Text</div>""")
    
    # Set up navigation between pages
    settings_btn.click(show_settings_page, inputs=[], outputs=[settings_page, main_app])
    back_btn.click(show_main_page, inputs=[], outputs=[settings_page, main_app])

# Launch the app
if __name__ == "__main__":
    demo.launch()