import gradio as gr
from ui.theme import BLUE_CIRCLE_ICON

def create_main_app():
    """Create and return components for the main application UI"""
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
                // Try to load chat history right away with multiple attempts
                (function() {
                    // Try immediately
                    if (window.populateChatHistory) {
                        window.populateChatHistory();
                    }
                    
                    // Try after a short delay
                    setTimeout(function() {
                        if (window.populateChatHistory) {
                            window.populateChatHistory();
                        }
                    }, 200);
                    
                    // Try after DOM is fully interactive
                    if (document.readyState === 'interactive' || document.readyState === 'complete') {
                        if (window.populateChatHistory) {
                            window.populateChatHistory();
                        }
                    } else {
                        document.addEventListener('DOMContentLoaded', function() {
                            if (window.populateChatHistory) {
                                window.populateChatHistory();
                            }
                        });
                    }
                    
                    // Final attempt after a longer delay
                    setTimeout(function() {
                        if (window.populateChatHistory) {
                            window.populateChatHistory();
                        }
                    }, 800);
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
            
            output = gr.Textbox(label="Response", show_label=True, visible=True, elem_classes=["response-box"])
    
    example_buttons = [example_1, example_2, example_3, example_4]
    return settings_btn, user_input, submit_btn, output, example_buttons

def create_settings_page():
    """Create and return components for the settings page UI"""
    with gr.Row(elem_classes=["full-width-header"]):
        back_btn = gr.Button("← Back", elem_classes=["back-button"])
        gr.HTML(f"""<div class="header-settings">Settings</div>""")
  
    with gr.Column(elem_classes=["settings-container"]):
        with gr.Group(elem_classes=["settings-panel"]):
            # Add a button to clear chat history
            clear_history_btn = gr.Button("Clear Chat History", variant="secondary", elem_classes=["clear-history-btn"])
            
        with gr.Group(elem_classes=["settings-panel"]):
            gr.HTML("""<div>Please upload the latest version of the Human Resources policies and procedures.</div>""")
            gr.File(label="Upload File")
    
    return back_btn, clear_history_btn