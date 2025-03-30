import gradio as gr

def question(user_question):
    """Handle the HR assistant functionality and store question in JavaScript"""
    print(f"User asked: {user_question}")
    # Return the response, we don't need to update the history HTML here
    # since it's handled by the JavaScript
    return "This is where the HR assistant response would appear."

def show_settings_page():
    return gr.update(visible=True), gr.update(visible=False)

def show_main_page():
    return gr.update(visible=False), gr.update(visible=True)

# Color scheme variables
dark_background = "#111827"
light_background = "#1f2937"
lighter_background = "#374151"
button_blue = "#4C82FB"
button_green = "#007b86"
purple_accent = "#9D5CF7"
card_bg = "#374151"
text_color = "#FFFFFF"
muted_text = "#A0A0A0"
icon_blue = "#4C82FB"

BLUE_CIRCLE_ICON = '<span style="display: inline-block; width: 18px; height: 18px; border: 5px solid #007b86; border-radius: 50%; vertical-align: middle; margin-right: 5px;"></span>'

with gr.Blocks(theme=gr.themes.Base(), 
    css=f"""
    .gradio-container {{background-color: {dark_background} !important;}}
    .main-panel {{padding-right: 15px; margin-right: 15px; background-color: {dark_background}; }}
    .left-panel {{background-color: {light_background}; border-radius: 10px; padding: 10px; margin: 15px;}}
    .example-questions {{background-color: {light_background}; border-radius: 10px; padding: 15px; margin-bottom: 20px; }}
    .full-width-header {{background-color: {light_background}; padding: 15px; width: 100%; display: flex; justify-content: space-between; align-items: center;}}
    .header {{
    display: flex;
    font-size: 24px;
    font-weight: bold;
    }}
    .header-settings {{
        align-items: center;
        text-align: center;
        font-size: 24px;
        font-weight: bold;
        padding-right: 100px;
    }}
    .header-text {{
        background-image: linear-gradient(to right, #007b86, #ffffff);
        background-size: 100%;
        background-clip: text;
        -webkit-background-clip: text;
        -moz-background-clip: text;
        -webkit-text-fill-color: transparent; 
        -moz-text-fill-color: transparent;
        display: inline-block; 
    }}
    .header-icons {{display: flex; align-items: center;}}
    .chat-icon {{color: {button_blue}; margin-right: 10px;}}
    .settings-icon {{color: {text_color}; font-size: 24px; cursor: pointer; transition: color 0.3s;}}
    .settings-icon:hover {{color: {button_blue};}}
    .section-title {{color: {text_color}; background-color: {dark_background}; padding: 10px; margin: 10px; font-size: 20px; margin-bottom: 15px;}}             
    .history-item {{padding: 8px 0; color: {text_color};}}
    .question-button {{background-color: {dark_background}; color: {text_color}; text-align: left; padding: 12px; 
                        border-radius: 8px; margin-bottom: 0px; border: none;}}    
    .capabilities {{background-color: {light_background}; border-radius: 10px; padding: 15px;}}
    .capability-card {{background-color: {dark_background}; border-radius: 8px; padding: 10px; margin: 10px;}}              
    .capability-title {{color: {text_color}; background-color: {dark_background}; font-size: 16px; font-weight: 600;}}
    .capability-subtitle {{color: {muted_text}; background-color: {dark_background}; font-size: 14px;}}
    .capability-group {{background-color: {dark_background}; }}
    .capability-row {{padding-right: 10px;  }}
    .capability-column {{  padding: 0 5px; }}
    .capability-column-divider {{ padding: 0 10px }}
    .footer-bar {{background-color: {light_background}; padding: 10px; border-radius: 8px; margin-top: 30px; margin-bottom: 30px;}}
    .send-button {{background-color: {button_green}; color: white; border-radius: 8px; margin-top: 10px; font-weight: 200;}}
    .back-button {{background-color: {button_green}; color: white; border-radius: 8px; padding: 6px 12px; margin-bottom: 20px; max-width: 30px;}}
    .settings-panel {{background-color: {card_bg}; border-radius: 10px; padding: 20px; margin: 15px;}}
    .settings-container {{background-color: {dark_background}; padding: 20px;}}
    .settings-btn {{background: none; border: none; color: {text_color}; font-size: 24px; width: 70px; align-self: flex-end; 
                    cursor: pointer; transition: color 0.3s; padding: 0; margin: 0;}}
    .settings-btn:hover {{color: {button_blue};}}
    """,
    head="""
    <script>
    // Function to update chat history that will be called when needed
    function populateChatHistory() {
        // Try to get questions from localStorage
        let questions = [];
        try {
            const storedQuestions = localStorage.getItem('userQuestions');
            if (storedQuestions) {
                questions = JSON.parse(storedQuestions);
            }
        } catch (e) {
            console.error('Error loading questions from localStorage:', e);
        }
        
        // Find the history container
        const historyContainer = document.getElementById('chat-history-items');
        if (!historyContainer) {
            console.error('Chat history container not found');
            return;
        }
        
        // Generate HTML for the questions
        let historyHTML = '';
        if (!questions || questions.length === 0) {
            historyHTML = '<div class="history-item">No previous questions</div>';
        } else {
            // Get the most recent questions first
            const recentQuestions = questions.slice(-10).reverse();
            
            for (const question of recentQuestions) {
                // Escape HTML to prevent XSS
                const escapedQuestion = String(question)
                    .replace(/&/g, '&amp;')
                    .replace(/</g, '&lt;')
                    .replace(/>/g, '&gt;')
                    .replace(/"/g, '&quot;')
                    .replace(/'/g, '&#039;');
                
                historyHTML += `<div class="history-item">${escapedQuestion}</div>`;
            }
        }
        
        // Update the container
        historyContainer.innerHTML = historyHTML;
    }
    
    // Set up the event listener for when the DOM is fully loaded
    document.addEventListener('DOMContentLoaded', function() {
        // Initial population of chat history
        setTimeout(populateChatHistory, 500);
        
        // Add submit event listener to populate chat history after submission
        const sendButton = document.querySelector('.send-button');
        if (sendButton) {
            sendButton.addEventListener('click', function() {
                // Wait a bit for the localStorage to be updated
                setTimeout(populateChatHistory, 500);
            });
        }
    });
    </script>
    """) as demo:
    
    #  Two pages: main app and settings
    main_app = gr.Group(visible=True)
    settings_page = gr.Group(visible=False)
    
    # Main application
    with main_app:
        with gr.Row(elem_classes=["full-width-header"]):
            # Create the header with title and settings button
            with gr.Column(scale=4):
                gr.HTML(f"""<div class="header"><span class="chat-icon">💬</span> <span class="header-text">GuideWell HR Assistant</span></div>""")
            
            # Instead of HTML/JS settings icon, use a gradio Button
            with gr.Column(scale=1):
                settings_btn = gr.Button("⚙️", elem_classes=["settings-btn"])
            
        with gr.Row(elem_id="container"):
            # Left panel - Chat History
            with gr.Column(scale=1, elem_classes=["left-panel"]):
                with gr.Row():
                    gr.HTML(f"""<div class="section-title">Chat History</div>""")
                
                with gr.Column():
                    # Here we just create a simple container for our JavaScript to target
                    gr.HTML("""
                    <div id="chat-history-items">
                        <div class="history-item">Loading chat history...</div>
                    </div>
                    
                    <script>
                    // Try to load chat history right away
                    (function() {
                        setTimeout(function() {
                            if (window.populateChatHistory) {
                                window.populateChatHistory();
                            }
                        }, 100);
                    })();
                    </script>
                    """)
            
            # Right panel - Main content
            with gr.Column(scale=3, elem_classes=["main-panel"]):

                # Example Questions Section
                gr.HTML(f"""<div class="section-title">Example Questions</div>""")
                with gr.Group(elem_classes=["capabilities"]):                   

                    with gr.Row(elem_classes=["capability-row"]):
                        with gr.Column(scale=1,elem_classes=["capability-column"]):
                            with gr.Group(elem_classes=["capability-card"]):
                                example_1 = gr.Button(
                                    "What is the policy for requesting paid time off?", 
                                    elem_classes=["question-button"]
                                )
                            
                            with gr.Group(elem_classes=["capability-card"]):
                                example_2 = gr.Button(
                                    "How do I update my direct deposit information?", 
                                    elem_classes=["question-button"]
                                )

                        with gr.Column(scale=1,elem_classes=["capability-column"]):
                            with gr.Group(elem_classes=["capability-card"]):
                                example_3 = gr.Button(
                                    "Explain the jury duty and court appearances policy?", 
                                    elem_classes=["question-button"]
                                )
                            
                            with gr.Group(elem_classes=["capability-card"]):
                                example_4 = gr.Button(
                                    "What are the steps for performance review submissions?", 
                                    elem_classes=["question-button"]
                                )
                            
                # Capabilities Section
                gr.HTML(f"""<div class="section-title">Capabilities</div>""")
                with gr.Group(elem_classes=["capabilities"]):                   

                    with gr.Row(elem_classes=["capability-row"]):
                        with gr.Column(scale=1,elem_classes=["capability-column"]):
                            with gr.Group(elem_classes=["capability-card"]):
                                gr.HTML(f"""
                                <div>
                                    <div class="capability-title"> 
                                        {BLUE_CIRCLE_ICON}Employee Self-Service</div>
                                    <div class="capability-subtitle">Manage your HR tasks efficiently</div>
                                </div>
                                """, elem_classes=["capability-group"])
                            
                            with gr.Group(elem_classes=["capability-card"]):
                                gr.HTML(f"""
                                <div>
                                    <div class="capability-title">{BLUE_CIRCLE_ICON} Security & Compliance</div>
                                    <div class="capability-subtitle">Stay informed about compliance requirements</div>
                                </div>
                                """, elem_classes=["capability-group"])

                        with gr.Column(scale=1,elem_classes=["capability-column"]):
                            with gr.Group(elem_classes=["capability-card"]):
                                gr.HTML(f"""
                                    <div>
                                        <div class="capability-title">{BLUE_CIRCLE_ICON} HR Policy & Procedure</div>
                                        <div class="capability-subtitle">Get instant answers about company policies</div>
                                    </div>
                                """, elem_classes=["capability-group"])
                            
                            with gr.Group(elem_classes=["capability-card"]):
                                gr.HTML(f"""
                                <div>
                                    <div class="capability-title">{BLUE_CIRCLE_ICON} Benefits & Compensation</div>
                                    <div class="capability-subtitle">Learn about your benefits package</div>
                                </div>
                                """,elem_classes=["capability-group"])

                # Input and Chat Area
                with gr.Row(elem_classes=["footer-bar"]):
                    with gr.Column(scale=30):
                        user_input = gr.Textbox(
                            placeholder="Ask me anything about HR policies...",
                            show_label=False,
                        )
                            
                    with gr.Column(scale=1):
                        submit_btn = gr.Button("SEND", elem_classes=["send-button"])
                output = gr.Textbox(label="Response", visible=False)
                
                # Connect the AI to the user inputs with localStorage saving
                submit_btn.click(
                    question, 
                    inputs=[user_input], 
                    outputs=[output],
                    js="""
                    function(user_question) {
                        try {
                            // Get existing questions from localStorage
                            let questions = [];
                            try {
                                const storedQuestions = localStorage.getItem('userQuestions');
                                if (storedQuestions) {
                                    questions = JSON.parse(storedQuestions);
                                }
                            } catch (e) {
                                console.error('Error parsing questions:', e);
                                questions = [];
                            }
                            
                            // Add the new question
                            if (user_question && user_question.trim() !== '') {
                                questions.push(user_question);
                                
                                // Save back to localStorage
                                localStorage.setItem('userQuestions', JSON.stringify(questions));
                                console.log('Saved question to localStorage:', user_question);
                                
                                // Manually call our populate function
                                setTimeout(function() {
                                    if (window.populateChatHistory) {
                                        window.populateChatHistory();
                                    }
                                }, 100);
                            }
                        } catch (e) {
                            console.error('Error saving to localStorage:', e);
                        }
                        
                        return user_question;
                    }
                    """
                )
                
                # Connect example questions to input field
                for example in [example_1, example_2, example_3, example_4]:
                    example.click(
                        fn=lambda text: text,
                        inputs=[example],
                        outputs=[user_input]
                    )

    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    # Settings page
    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    with settings_page:
        with gr.Row(elem_classes=["full-width-header"]):
            back_btn = gr.Button("← Back", elem_classes=["back-button"])

            gr.HTML(f"""<div class="header-settings">Settings</div>""")
      
        with gr.Column(elem_classes=["settings-container"]):
            with gr.Group(elem_classes=["settings-panel"]):
                gr.HTML("""<div>Please upload the latest version of the Human Resources policies and procedures.</div>""")
                gr.File(label="Upload File")
                
                # Add a button to clear chat history
                clear_history_btn = gr.Button("Clear Chat History", variant="secondary")
                
                # Add JS to clear localStorage when the button is clicked
                clear_history_btn.click(
                    fn=lambda: None,
                    inputs=[],
                    outputs=[],
                    js="""
                    () => {
                        localStorage.removeItem('userQuestions');
                        alert('Chat history cleared');
                        
                        // Update the display
                        if (window.populateChatHistory) {
                            window.populateChatHistory();
                        }
                    }
                    """
                )
    
    # Set up navigation between pages using the actual buttons
    settings_btn.click(show_settings_page, inputs=[], outputs=[settings_page, main_app])
    back_btn.click(show_main_page, inputs=[], outputs=[settings_page, main_app])

# Launch the app
if __name__ == "__main__":
    demo.launch()